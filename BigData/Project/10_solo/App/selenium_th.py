
from PyQt5.QtCore import pyqtSignal,QThread
from PyQt5.QtWidgets import *

# 본인 모듈 import 
from signal_col import signal_collection

# 셀레니움 크롤링 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
import random as rd
import pandas as pd
import re

class crawling_sele(QThread):
    def __init__(self, signal):
        super().__init__()
        self.ID = None
        self.PW = None
        self.signal = signal
        # self.signal.idpw_signal.connect(self.login_info_receiver)   # idpw 받아옴.
        self.open_check = True
        self.signal.open_driver_Mainview_signal.connect(self.open_driver)
        self.login_try = False
        self.link_point = False
        self.Link_list = []

        # 세부조건
        self.hash_amt, self.text_amt = 1, None

        # 검색 조건
        self.search_type_condition, self.searh_word_condition, self.MainText_condition, self.Oner_ID_condition, self.lover_condition, self.Hash_condition, self.want_amount_condition = None,None, None, None, None, None, None

        print("쓰레드 시작")
        

    def open_driver(self, ch):
        if ch:
            print("셀레니움 실행")
            options = Options()
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            options.add_argument(f"user-agent={user_agent}")
            chrome_driver_path = "chromedriver.exe"  # 크롬 드라이버 설치 경로 입력
            service = Service(chrome_driver_path)
            # 웹 드라이버 실행
            self.driver = webdriver.Chrome(options=options)
            self.url ="https://www.instagram.com"
            self.driver.get(self.url)
            # self.driver.set_window_position(100, 100)
            # self.driver.set_window_size(1024, 768)
            # self.open_check = False
            ch = False
            

    
    idinput_path = [ # 로그인 ID 입력 창 
        # (By.CLASS_NAME, '_aa4b _add6 _ac4d _ap35'),
        # (By.CLASS_NAME, '_aa4b._add6._ac4d._ap35'),
        (By.CSS_SELECTOR,'#loginForm > div > div:nth-child(1) > div > label > input'),
        (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'),
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[1]/div/label/input")
        ]
    pwinput_path = [ # 로그인 PW 입력 창 
        # (By.CLASS_NAME, '_aa4b _add6 _ac4d _ap35'),
        # (By.CLASS_NAME, '_aa4b._add6._ac4d._ap35'),
        (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input'),
        (By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'),
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div/div[2]/div/label/input')
        ]
    log_submit_path = [ # 로그인 입력 버튼 클릭.
        # (By.CLASS_NAME, 'x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1'),
        # (By.CLASS_NAME, 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'),
        (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div'),
        (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'),
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button/div')
        ]
    fail_login_path = [ # 로그인 실패 문구 찾는 path
        (By.CLASS_NAME, 'x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj'),
        (By.CLASS_NAME, 'x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj'.replace(" ",".")),
        (By.CSS_SELECTOR, '#loginForm > span'),
        (By.XPATH, '//*[@id="loginForm"]/span'),
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/span')
        ]
    login_info_question_path = [    # 로그인 성공 후 나중에 하기 path
        (By.CLASS_NAME, 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37'.replace(" ",".")),
        (By.CSS_SELECTOR, '#mount_0_0_js > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div > div > div > div'),
        (By.XPATH, '//*[@id="mount_0_0_js"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div'),
        (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
        ]
    MainText_path = [   # 본문 찾기
        (By.CLASS_NAME, "_ap3a._aaco._aacu._aacx._aad7._aade"),
        (By.CLASS_NAME, "x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"),
        (By.CSS_SELECTOR, "#mount_0_0_Nn > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6 > div > div:nth-child(1) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > span > div > span"),
        (By.XPATH, "//*[@id='mount_0_0_Nn']/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span"),
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span')
        ]
    scroll_selectors = [# 스크롤 가능한 요소 찾기
        (By.CLASS_NAME, "_a9z6._a9za"),
        (By.CLASS_NAME, "x5yr21d.xw2csxc.x1odjw0f.x1n2onr6"),
        (By.XPATH, '//*[@id="mount_0_0_IQ"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[2]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul'),
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]'),
        (By.CSS_SELECTOR, '#mount_0_0_Nn > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6')
        ]
    comments_path = [# 댓글창 전체를 리스트로 뽑아내는 경로
        (By.CLASS_NAME, 'x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1'),
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div"),
        (By.CSS_SELECTOR, '#mount_0_0_Nn > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6 > div > div.x78zum5.xdt5ytf.x1iyjqo2 > div:nth-child(1) > div:nth-child(1) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(1) > div'),
        (By.CSS_SELECTOR, '#mount_0_0_mD > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xvkph5b.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x10o80wk.x14k21rp.xh8yej3.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6 > div > div:nth-child(3) > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div:nth-child(1) > div'),
        (By.XPATH, '//*[@id="mount_0_0_mD"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div')
        ]
    comment_box_PATH = [    # 본문 + 일반 댓글의 전체 댓글 박스
    (By.CLASS_NAME, 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'.replace(" ",".")),
    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]'),
    (By.XPATH,'//*[@id="mount_0_0_D7"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]'),
    (By.CSS_SELECTOR,'#mount_0_0_D7 > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6 > div > div.x78zum5.xdt5ytf.x1iyjqo2 > div:nth-child(1)')
    ]
    button_path = [ # 대댓글 열기 버튼 path
        (By.CLASS_NAME, 'x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x87ps6o.x1d5wrs8'),
        (By.CSS_SELECTOR, '#mount_0_0_AB > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6 > div > div.x78zum5.xdt5ytf.x1iyjqo2 > div:nth-child(6) > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x540dpk > div'),
        (By.XPATH, '//*[@id="mount_0_0_AB"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[6]/div[2]/div'),
        (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[6]/div[2]/div')
    ]
    lover_path = [
        (By.CLASS_NAME, 'x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj'),
        (By.CLASS_NAME, 'x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj'.replace(" ",".")),
        (By.CSS_SELECTOR, '#mount_0_0_nl > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x1xp8e9x.x13fuv20.x178xt8z.x9f619.x1yrsyyn.x1pi30zi.x10b6aqq.x1swvt13.xh8yej3 > section.x12nagc > div > div > span > a > span'),
        (By.XPATH, '//*[@id="mount_0_0_nl"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[3]/section[2]/div/div/span/a/span'),
        (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[3]/section[2]/div/div/span/a/span')
        ]

    # path 리스트 입력 시 크롤링 되는 text 리턴
    def text_finder(self, path_list):
        # 조건 충족하는 버튼 클릭시키는 함수.
        for by, path in path_list:
            try:
                target_text = self.driver.find_element(by, path).text
                break # 되면 더 찾지마
            except:           
                continue
        self.timesleep_under_1s()
        return target_text
        # 이걸 해서 찾는 결과물.
        # 1. 조건에 맞는 버튼 클릭
        # 2. 조건 충족 시 text 출력
        # 3. 조건 미충족 시 다음 이벤트로 안넘어가게 하기.

    # 찾는 리스트로 해서 텍스트 입력하는 함수
    # 아이디, 비밀번호 
    def text_sendkey(self, path_list, input_text):
        for by, path in path_list:  # 아이디 입력
            try:
                # self.driver.find_element(by, path).clear()
                self.driver.find_element(by, path).send_keys(Keys.LEFT_SHIFT, Keys.HOME, Keys.BACKSPACE)
                self.driver.find_element(by, path).send_keys(input_text)
                break # 되면 더 찾지마
            except:           
                continue
        self.timesleep_under_1s()


    def click_target(self, path_list, button_text):
        # 조건을 추가해야하나?
        for by, path in path_list:
            try:
                self.login_btn = self.driver.find_element(by, path)
                if self.login_btn.text == button_text:
                    self.driver.find_element(by, path).click()
                break # 되면 더 찾지마
            except:           
                continue
        self.timesleep_under_1s()


    def run(self):
        # 만약 로그인창이라면?
        self.signal.idpw_signal.connect(self.login_info_receiver)     # ID/PW 비밀번호 받아오면 작동되도록 시그널화
        # 조건 여기서 추가해서 조건을 받아서 그에 따라 실행되도록 해야한다.
        self.signal.start_crawling_signal.connect(self.search_condition_receiver)    # 이때 받아야만 본격적인 크롤링 시작되도록 함.
        # if self.link_point:
        #     self.tag_link_crawler(self.search_type_condition, self.searh_word_condition,self.want_amount_condition)
        self.signal.mini_condition_signal.connect(self.minicon_receiver)
        self.signal.link_save_complete_signal.connect(self.start_crawling)
        self.signal.crawl_links_send_signal.connect(self.TupToLinks)
        
        

    def minicon_receiver(self, text_amt,hash_amt):
        self.text_amt = text_amt
        self.hash_amt = hash_amt

        
    def search_condition_receiver(self, type, searh_word, id, text,  love, hash, amount):
        self.search_type_condition = type   # str
        self.searh_word_condition = searh_word
        # 긁어올 내용   checkBox
        self.Oner_ID_condition = id
        self.MainText_condition = text   # bool
        self.lover_condition =  love
        self.Hash_condition = hash
        # 수집할 양 - EditLabel
        self.want_amount_condition = amount # int
        print("조건 : ", type, searh_word,  id, text, love, hash, amount)
        # self.link_point = True
        self.tag_link_crawler(self.search_type_condition, self.searh_word_condition,self.want_amount_condition)

    
    # 일단 링크 긁어서 DB에 넣기.
    def tag_link_crawler(self, type, searh_word, amount):
        # for tag in ['먹스타그램']:    # 검색할 태그 입력
        links = 0
        if type =="태그":
            base_url = "https://www.instagram.com/explore/search/keyword/?q=%23"
        elif type =="사용자 ID":
            base_url = "https://www.instagram.com/"
        else:
            print("오류 발생!")
        
        # 일단 태그 하나만 검색할 수 있도록 함.
        url = base_url+searh_word
        self.driver.get(url) 
        time.sleep(rd.choice([4.7,5,5.3]))
            # 태그서치 url
        while links <= amount:
            # 링크가 원하는 양만큼 차면 멈출건데. 그걸 DB에서 확인을 해야함. 
            # 링크가 나오면 바로 DB 저장 쓰레드에 넣자.
            # 스크롤은 계속 내려야하니까. 이후에 저 조건이 충족이 안되면 내려가는 걸로.
            first_result = self.driver.find_elements(By.CSS_SELECTOR, "a.x1i10hfl.xjbqb8w.x1ejq31n")
            # 처음에 온갖게 리스트 뭉탱이로 나오고
            for f in first_result:  # 여기서 하나씩 뽑아서? href가 포함되어있는 것만 한다.
                link = f.get_attribute("href")
                if "/p/" in link:
                    # 링크는 텍스트야.
                    self.signal.system_message_signal.emit(f"[1/2] 링크 진행중 ___{links+1}/{amount}")
                    # print(f"--- 진행중 {links+1}/{amount}----")

                    # print("링크된 크롤링 : ",link)
                    links += 1

                    self.signal.link_saver_signal.emit(searh_word, link)
                    if links == amount:
                        self.signal.link_crawl_end_signal.emit(amount)
                        break
                    self.timesleep_under_1s()
            if links == amount:
                self.signal.link_crawl_end_signal.emit(amount)
                break
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.timesleep_2s_4s()
        # self.search_type_condition, self.searh_word_condition,self.want_amount_condition = None, None, None
        # 링크 끝났으면 찐 크롤링 시작해야함. 여기서 시그널을 줄까?
        # 아 근데 링크가 다 저장된 다음에 해야함.
        

    def TupToLinks(self, tupdata):
        self.Link_list = [data[0] for data in tupdata]
        # print("TupToLinks 실행, tupdata : ",tupdata)
        
        
    def start_crawling(self):
        search_word = self.searh_word_condition
        b_id = self.Oner_ID_condition
        b_text = self.MainText_condition   # bool
        b_love =self.lover_condition
        b_hash = self.Hash_condition
        amount = self.want_amount_condition
        # [(link,), (link,), (link,), (link,), 이런식으로 ...] 이런식으로 데이터가 들어올 예정
        # 이걸로 link 받아서 리스트화 한 다음에 그걸로 for 문 돌리자.
        
        print("2차 (선택 요소) 크롤링 시작")
        print(f"self.Link_list : {len(self.Link_list)}개", self.Link_list)
        for main_idx, link in enumerate(self.Link_list):
            # print(f"---------------------{main_idx+1}/{len(self.Link_list)}---------------------")
            self.signal.system_message_signal.emit(f"[2/2] 링크 진행중 ___{main_idx+1}/{len(self.Link_list)}")
            # print("링크 :", link)
            hash_list = []
            self.driver.get(link)
            time.sleep(rd.choice([3,3.3,3.5,3.7,4.0,4.1,4.3,4.5,4.7,5.0,5.1,5.2,5.3]))   # 계정 정지 방지용

            # id크롤링 부분
            if b_id:
                try:
                    Oner_ID = self.driver.find_element(By.CLASS_NAME,'x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.xqnirrm.xj34u2y.x568u83')
                    
                    Oner_ID = Oner_ID.text  # 아래 댓글 조건용으로 담기는 해야해.
                    send_noid = Oner_ID     # 보내는 용으로 따로 저장
                except:
                    Oner_ID = "삭제된 페이지"  #
                    self.signal.data_saver_signal.emit((search_word, link ,Oner_ID, None, None, None))
                    continue    # 아이디도 안 긁혀오는 경우에는 페이지 삭제 확률이 높다.
            else:
                send_noid = None
                time.sleep(rd.choice([0.3,0.5,0.7,1.0]))

            # 본문 부분
            
            for by, path in self.MainText_path:
                try:
                    MainText = self.driver.find_element(by, path)
                    break # 되면 더 찾지마
                except:               
                    MainText = None
                    continue

            if MainText is not None:
                MainText = MainText.text
            else:   # 본문 글이 없다면 다 None값 처리 
                continue

            for t in MainText.split():
                if "#" in t:                # 본문에 해시태그가 있는 경우, 삭제 및 hash리스트에 빼서 넣어두기.
                    MainText = MainText.replace(t,"")
                    hash_list.append(t)
            time.sleep(rd.choice([0.3,0.5,0.7,1.0])) 
            MainText = re.sub('[^가-힣]+',' ', MainText) # 영어 및 이모티콘 같은 글 삭제

            if not b_text:
                MainText = None

            if self.text_amt != None:
                if len(MainText) < self.text_amt:
                    MainText = "텍스트 조건 미달"
            else:
                pass

            # lover 부분
            # 신규 구현 필요 ...
            # lover = None
            if b_love:
                for by, path in self.lover_path:
                    try:
                        lover = self.driver.find_element(by, path)
                        lover = lover.text
                        lover = lover.replace("좋아요","").replace(" ","").replace("개","")
                        if ("만" in lover) and ("." in lover):
                            lover = lover.replace("만","000").replace(".","")
                        elif "만" in t:
                            lover = lover.replace("만","0000")
                        lover = int(lover)
                        break # 되면 더 찾지마
                    except:           
                        lover = "좋아요 미표기 게시글"
            else:
                pass



            # 해시태그 부분 
            scrollable_div = None
            for by, selector in self.scroll_selectors:
                try:
                    scrollable_div = self.driver.find_element(by, selector)
                    break
                except:
                    pass  

            bad_try = 0
            if b_hash:
                for by, path in self.comments_path:
                        try:
                            comment = self.driver.find_elements(by, path)
                            break
                        except:
                            pass
                Oner_text = ""
                for c in comment:   # 댓글에 있는 태그도 일단 검색해.
                    if Oner_ID in c.text:
                        Oner_text += c.text
                for text in Oner_text.split():  # 계정주 글 중에 # 포함되어있는 것들 추가.
                    if "#" in text:
                        for t in text.split("#")[1:]:
                            t = "#"+t
                            hash_list.append(t)
                time.sleep(rd.choice([0.5,0.7,1.0, 1.1,1.2,1.3]))
                    # 만약 본문과 일반 댓글에 없다면? 내려가야겠지?         
                while (len(hash_list) < self.hash_amt) and (bad_try<10):
                    # 무언가 문제 발생 시 무한 스크롤하고 작동 정지하는 문제 있음. -> bad_try 로 스크롤 10번만 하는 것으로 제한. 
                    for by, path in self.comment_box_PATH:
                        try:
                            comment_box = self.driver.find_elements(by, path)
                            break
                        except:
                            pass
                    cocom = False
                    # 댓글창
                    for idx, box in enumerate(comment_box):
                        # print(f"-----------------------------{idx}-----------------------------")
                        if ("모두 보기" in box.text) and (len(box.text)>11) and (box.text.split()[0] == Oner_ID):    # 댓글 전체 + 그냥 답글 1개 모두 보기 이런식으로 또 2개 뜸  # 진짜 왜 .........?
                            for by, path in self.button_path:
                                try:
                                    box.find_element(by, path).click()
                                    time.sleep(rd.choice([0.5,0.7,0.9])) 
                                    self.driver.execute_script("arguments[0].scrollTop += arguments[1];", scrollable_div, 100)   # 스크롤 했으니 다시 크롤링 해야지.
                                    time.sleep(rd.choice([1.2,1.5,1.7])) 
                                    cocom = True
                                except:
                                    pass
                    # 대댓글 발견 시 작동.
                    if cocom:
                        for by, path in self.comment_box_PATH:
                            try:
                                comment = self.driver.find_elements(by, path)
                                break
                            except:
                                pass
                        for idx, box in enumerate(comment):
                            if box.text.split() != []:
                                # print(box.text.split())
                                if (box.text.split()[0] == Oner_ID):
                                    hash_list = [text for text in box.text.split() if "#" in text]  # 일단 스크롤해서 더 밑에 깊게 묻혀있는게 아니면 갖고옴.
                    if len(hash_list) < self.hash_amt:  # 아니 뭐하느라 남들 댓글달때 지 태그를 안걸어놔 밑으로 계속 가
                        self.driver.execute_script("arguments[0].scrollTop += arguments[1];", scrollable_div, 300)
                        bad_try += 1
                        time.sleep(rd.choice([1.0, 1.5,1.6,1.9]))
                # SEARCH_WORD, LINK, ONER_ID, MAINTEXT, LOVER, HASHTAG
                hash_list = list(set(hash_list))
                hash_list = ' '.join(hash_list)
            else:
                hash_list = None

            if bad_try == 10:
                hash_list = "해시태그 탐지 불가"

            print(f" 저장 데이터 | 검색어 : {search_word}, <링크생략> , 사용자이름 : {send_noid}, 본문 : {MainText}, 좋아요 : {lover}, 해시태그 : {hash_list}")
            self.signal.data_saver_signal.emit((search_word, link ,send_noid, MainText, lover, hash_list))    # 크롤링 된 데이터 튜플 형식으로 발송.
        # 여기서 끝나니까 만약 추가하면 saver 종료하는 시그널 줘서 while True문 깰 수 있을 것 같음.
        # mainview 쓸때 스타트 했음. 얘는 for문 다하면  /// 아냐아냐아냐 이거 꺼지면 셀레니움도 꺼지는데?
        # 그럼 메인뷰가 아니라 아냐 로그인하려면 있긴 해야해.
        # self.join()


    def timesleep_under_1s(self):
        time.sleep(rd.choice([0.1,0.2,0.4,0.5,0.7,0.8,1.0]))

    def timesleep_1s_2s(self):
        time.sleep(rd.choice([1.0,1.2,1.4,1.5,1.7,1.8,2.0]))
    def timesleep_2s_4s(self):
        time.sleep(rd.choice([2.0,2.2,2.4,2.5,2.7,2.8,3.0,3.1,3.2,3.4,3.6,3.8,4.0]))



    def login_info_receiver(self, id, pw, login_try):
        self.ID = id
        self.PW = pw
        self.login_try = login_try
        # print("self.login_try : ", self.login_try)
        self.Try_login()
        
        
    def Try_login(self):
        if self.login_try:
            self.text_sendkey(self.idinput_path, self.ID)
            self.text_sendkey(self.pwinput_path, self.PW)
            self.click_target(self.log_submit_path, "로그인")
            # 일단 여기서 로그인이 되면 문제가 없는데, 만약 문제가 생기면 ?
            self.login_try = False
            time.sleep(4)   # 로그인에 소요되는 시간 
            self.check_login()
      
      # 기능이 많이 느리다. 쓰레드 따로 만드는것이 좋을 듯함.
    def check_login(self):
        # 로그인에 성공했다면? 아래 링크임.
        if self.driver.current_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':
            self.click_target(self.login_info_question_path, "나중에 하기")
            time.sleep(1.5)
            self.signal.login_success_signal.emit(True)
        else:
            print("로그인 실패")
            # 일로 왔으면 로그인 실패 가능성 98%
            # 실패 문구 찾기
            fail_text = self.text_finder(self.fail_login_path)
            if (fail_text == "잘못된 비밀번호입니다. 다시 확인하세요.") or (fail_text =="입력한 사용자 이름을 사용하는 계정을 찾을 수 없습니다. 사용자 이름을 확인하고 다시 시도하세요."):
                # self.mini_message = threading.Thread(self.showMessageBox("로그인 오류","잘못된 ID/PW 입니다."))
                # self.mini_message.start()
                self.showMessageBox("로그인 오류","잘못된 ID/PW 입니다.")



    # def Warning_event(self,case, text) :
    #     QMessageBox.about(self,case,text)
    def showMessageBox(self,case,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(case)
        msg.setInformativeText(text)
        msg.setWindowTitle("오류")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        # if self.mini_message.is_alive():
        #     self.mini_message.join()



        # 로그인 신호 로그인에서 받고 크롬 실행 + 아이디, 비밀번호 입력
    def selenium_test(self):
           # 기본 크롤링은 인스타. 이외의 링크는 취급 x
        # url ="https://httpbin.org/headers"
        # 여기서 로그인 하고 아래 본격적인 크롤링 시작하기
        pass

