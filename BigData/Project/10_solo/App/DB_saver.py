import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import (QThread, pyqtSignal)
from PyQt5.QtWidgets import *
from collections import deque

import time

class DB_Saver(QThread):
    def __init__(self, signal, showtable):
        super().__init__()
        self.signal = signal
        self.showtable = showtable
        self.link_deque = deque()
        self.crawling_deque = deque()
        self.signal.closecon_signal.connect(self.close_con)
        self.deque_size = 9999
        self.search_word = None
        
        # 링크 받아옴.


    # [LINK, ONER_ID, MAINTEXT, LOVER, HASHTAG]
    def run(self):
        self.con = sqlite3.connect("insta.db")
        self.Cur = self.con.cursor()
        self.create_table()
        # 이거는 처음에 다 보이는거잖아. 근데 내가 지금 크롤링된 부분만 볼거니까 나중에 조건값에 맞는 것만 띄우자고.
        # if self.showtable is not None:
        #     self.load_data()
        # 1차 링크 받을 시그널. str으로 링크만 받는다.
        self.signal.link_saver_signal.connect(self.link_receiver)   # 링크 큐에 링크 추가.
        self.signal.data_saver_signal.connect(self.data_receiver)   # 데이터 큐에 데이터 추가.
        self.signal.link_crawl_end_signal.connect(self.crawl_sign)

        first_in = True
        link_count = 0  # 링크 데이터가 다 저장되면 시그널을 줘서, 저장 되었다고 알림. 그와 동시에 2차 크롤링 시작.
        while True:
            if (link_count == self.deque_size) and (first_in == True):
                print("saver - run 1차 링크 데이터 저장완료")
                self.send_links()
                self.signal.link_save_complete_signal.emit(True)
                print("send_link 실행 완")
                first_in = False
                time.sleep(2)
            # 링크용.
            if self.link_deque:
                print("세이버 와일문 안.",link_count,"/",self.deque_size)
                link_count += 1
                save_link = self.link_deque.popleft()
                self.insert_linkdata(self.search_word ,save_link)
                # count += 1
                self.signal.load_data_signal.emit((self.search_word,save_link))    # 일단 popleft해서 DB에 저장하는 데이터를 DB_Viewer에 전달중 // 이걸 불러와서 전달하는게 더 빠를것같은데 그럼 자식의 자식 관계가 필수가 된다.
                    # 링크 다 모았으면 링크 리스트 emit해줘야하는데. 어디서 해야할까.
            elif self.crawling_deque:   # 어차피 1차 끝나면 여기까지ㅏ는 오지도 못함ㄵㄷ그ㅏㅣㅐㅣㅏㅜㄴㅇㄻㄻㄴ애ㅔㅓ
                crawldata = self.crawling_deque.popleft()
                self.insert_crawlingdata(crawldata)
                # count += 1
                # 올 데이터 다 넣는걸로 하나씩 해드리고.
                self.signal.load_data_signal.emit(crawldata)
            # 
            else:
                self.sleep(1)



        # self.signal.link_crawl_end_signal.connect(self.crawl_sign)
        # 데이터 저장 파트.
        
        # 신호 2개를 만들고 링크 신호면 1번 와일, 데이터 신호면 2번 와일 돌아가게 하면 되겟네 ㅅ!ㅂrfasdfsdafㅇㄴ른ㅁㅇ라ㅣㅇㄴ르ㅏㅠㅠㅠㅠㅠㅠㅠㅠ

    """
    def link_while(self, deque_size):
        count = 0
        while count <= deque_size:
            if self.link_deque:
                save_link = self.link_deque.popleft()
                self.insert_linkdata(save_link)
                count += 1
                if self.showtable is not None:
                    self.load_data()
            else:
                self.sleep(1)

    def data_while(self):
        count = 0
        while count <= self.deque_size:
            if self.crawling_deque:   # 어차피 1차 끝나면 여기까지ㅏ는 오지도 못함ㄵㄷ그ㅏㅣㅐㅣㅏㅜㄴㅇㄻㄻㄴ애ㅔㅓ
                self_data = self.crawling_deque.popleft()
                self.insert_crawlingdata(self_data)
                count += 1
                # 올 데이터 다 넣는걸로 하나씩 해드리고.
                if self.showtable is not None:
                    self.load_data()
            else:
                self.sleep(1)
    """


    def crawl_sign(self, amount):
        self.deque_size = amount
        
    def close_con(self, check):
        if check:
            self.con.close()

    def send_links(self):
        # SEARCH_WORD = "example"  # 찾고자 하는 문자열
        # query = "SELECT LINK FROM insta WHERE LINK = ?"
        # self.Cur.execute(query, (SEARCH_WORD,))
        # data = self.Cur.execute("SELECT LINK FROM insta WHERE LINK = ?", (self.search_word,)).fetchall()
        # data = self.Cur
        time.sleep(0.1)
        try:
            sql = "SELECT LINK FROM insta WHERE SEARCH_WORD = ?"
            data = (self.search_word,)
            # 쿼리 실행
            self.Cur.execute(sql, data)
            result = self.Cur.fetchall()
        except Exception as e:
            print("1차 링크 발송 fetchall에서 오류 : ", e)

        # print("1차 링크 데이터(튜플) 전송", result)
        # 튜플 식으로 나오지 않나 ?
        # [(link,), (link,), (link,), (link,), 이런식으로 ...]
        self.signal.crawl_links_send_signal.emit(result)


    def insert_linkdata(self, SEARCH_WORD, LINK):
        try:
            sql = "INSERT OR IGNORE INTO insta (SEARCH_WORD, LINK) VALUES (?,?)"
            data = (SEARCH_WORD, LINK,)
            self.Cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print("링크 insert 에러 발생", e)


        # self.Cur.execute("SELECT * FROM insta")
        # data = self.Cur.fetchall()  # 데이터를 즉시 다시 확인
        # print("insert_linkdata에서 링크 잘 들어갔는지 확인.", data)
            # "INSERT INTO example_table (column1, column2) VALUES (?, ?)", ('value1', 'value2')
            # "INSERT OR REPLACE INTO example_table (id, name) VALUES (?, ?)", (1, 'John')
            # cursor.execute("INSERT OR IGNORE INTO example_table (id, name) VALUES (?, ?)", (1, 'John'))

    def insert_crawlingdata(self, datatup):
        try:
            sql = "INSERT OR REPLACE INTO insta (SEARCH_WORD, LINK, ONER_ID, MAINTEXT, LOVER, HASHTAG) VALUES (?,?,?,?,?,?)"
            data = datatup
            self.Cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print("크롤링 데이터 insert 에러 발생", e)


    # 여기는 데이터가 튜플로 와야하나?
    # 신호 받고 큐에 추가 
    def data_receiver(self, data):
        self.crawling_deque.append(data)

    # 얘는 링크 하나였지.
    def link_receiver(self, SEARCH_WORD, link):
        self.search_word = SEARCH_WORD
        self.link_deque.append(link)

    # 인스타 링크를 instar.com 이후에 / ㄻㅇㄴㄹㅇㅁㄴㄹ / 부분만 짤라서 저장하면 메모리 아낄 수 있음.
    # 테이블 생성 
    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS insta(
            SEARCH_WORD TEXT, 
            LINK TEXT PRIMARY KEY,
            Oner_ID TEXT,
            MAINTEXT TEXT,
            LOVER TEXT,
            HASHTAG TEXT
            );"""
        self.Cur.execute(sql)



    # def run(self):
    #     SQL = DB_Saver()
    #     SQL.create_table
    #     SQL.insert_data("계정주인", "본문내용", "해시태그")

