
인스타 아이디 비밀번호 입력 필요

셀레니움으로 진입 시 로그인 기록 저장 / 나중에 하기 선택 탭 뜸 (랜덤이므로 이 경우에는 뜰 경우에 나중에 하기로 넘어가도록 설정 필요)
DB 연결해서 저장

1. DB 저장 쓰레드
2. 크롤링 하는 쓰레드

크롤링 시 어떤 정보를 수집할 것 인가 선택
1. 태그
2. 아이디

크롤링 가능한 목록
1. 계정주 아이디
2. 본문 글
3. 해시태그

# LoginView -> MainView 조건 충족 시 전환
방법 1. 컨트롤 클래스를 만들어 LoginView에서 조건을 충족하면 닫히고, 이후에 MainView가 뜨도록 컨트롤함.
방법 2. 부모-자식 관계 활용 // Main에서 Login을 직접 제어 - 큰 프로젝트에는 비효율적이라고 함.
방법 3. QStackedWidget 활용
방법 4. 시그널 - 슬롯 방식.

DB 저장은 일단 sqlite3 쓰고, 
https://devyurim.github.io/python/crawler/2018/08/11/crawler-2.html


CONDA 3.8.19
가상환경 slpj
[package] selenium, sqlite3, pyQT5

처음에 로그인 View에서 로그인


로그인 진입 시 
https://www.instagram.com/sem/campaign/emailsignup/?campaign_id=13530338586&extra_1=s%7Cc%7C547419126422%7Ce%7Cinsta%20gram%7C&placement=&creative=547419126422&keyword=insta%20gram&partner_id=googlesem&extra_2=campaignid%3D13530338586%26adgroupid%3D126262418054%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1321618850291%26loc_physical_ms%3D9217072%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gad_source=1&gclid=CjwKCAiA9bq6BhAKEiwAH6bqoAMjrL5H_47xcosqTNLO_5ApyVfLHltyOLmka64hKvikaE8B1jUhhhoCudsQAvD_BwE
가입 권유 화면이 먼저 뜸.
이 화면일 시, 로그인 화면인 여기로 이동.
https://www.instagram.com/accounts/login/?source=auth_switcher
그 담에 로그인 하더라도 로그인 정보 저장 물음.
https://www.instagram.com/accounts/onetap/?next=%2F


로그인 정보 저장하겠냐고 묻는 창.
https://www.instagram.com/accounts/onetap/?next=%2F
selector = #mount_0_0_K8 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div > div > div > div
XPATH = //*[@id="mount_0_0_K8"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div
fullXPATH = /html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div


좋아요
element = <span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">8만</span>

selector = body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x12nagc.x182iqb8.x1pi30zi.x1swvt13 > div > div > span > a > span > span

XPATH = /html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/span/a/span/span

fullXPATH = /html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/span/a/span/span




수정 필요 사항
1205. 0919 = 아이디 비밀번호 에러 메세지가 너무 늦게 나온다 . 


크롤링 시 조건들.
    # 검색어 (태그 or 게시자 아이디)
    # 게시글 내용
    # 좋아요 수
    # 게시자 이름
    # 해시태그
    # 크롤링 게시글 횟수

현재는 링크를 받아서 이후에 그 링크에 쫘라락인데.
접근 방식을 바꾸어야할까?
오히려 시간면에서는 애매할 수 도 있음. 일단은 그렇게 진행하자.


1205 \ 16:06
+ 데이터 입력 안했을 때 메세지 박스가 안뜨는 것 같다.
자, 1차 링크 크롤링은 완료함.
다만, 링크 크롤링이 완료된 이후에도 계속 데이터 밀어넣으려는 시도갸 ㅏ있음.
이거 확실하게 끝내주고.
그다음에 저 링크 타고 다시 None값으로 처리된 친구 밀어넣으러 가자고.



두 쓰레드에서 db에 동시 접근하면 안되니까 
fetchall 해서 저장한 link를 링크 쓰레드에 보내줘야해.
근데 언제?
링크 저장 다 끝나고 . 
그럼 링크 저장 끝난 후에 while True 긑내줘야겟네



자, 지금은 어떻게 하고 있어.
링크 크롤링을 한 다음에 그걸 신호를 주면 그 다음으로 다시다시다시 run에서 2차 데이터 크롤링을 해야하는데
그걸 멍청하게 같이 묶어두고 신호를 줘서 1차만 하면 끝내게 만들어버렸단 말이지?
그럼 어떻게 해ㅔ야0휴ㅐㅑㄴㅇㅀ매ㅡㅜㅑㅏㅓㄴㅁㅎ\
ㅐㅡ3ㄿ 4

while 문 2개 만들어서 실행시키면 while의 시작 지점이 저거니까
크롤링 시작할때 알려주고 while문 시작하면서 끝도 같이 알려줘야하는데. 그럼 너무 시그널 낭비가 아닌가.
이게 맞나 
쓰레드 안 쓰레드로 하는게 나을려ㅏㄴ.
어차피 순서상으로는 
링크만 긁어온 다음 그 다음에 시작하는거니까
원래는 쓰레드 연결 끊으면 되는건데 왜 ... 아름ㄴ아르아아 ㅏ


자, 지금 하나씩 추가가 되고 있는 상황에서 계속 저장이 되어야해.
그럼 이 while문은 언제끝날지 모르는거란 말이지.
근데 이게 또 끝나면 새로운 while을 돌려야하는데.

데이터 긁어오면서 실시간으로 받아야하니까
처음에 while문 시작하면서 항상 돌아가야함.
2차가 문제인거지.

처음 시도했던 처음에는 9999 해주고 그 다음에 self.amount 바꾸면서 break 설정해주고
그럼 처음 link_while은 계속 True로 돌린다음에
링크 모으는게 끝나면 amount 바꾸는 식응로 해서 break

이후에 break가 걸리면 

그럼 처음부터 끝까지 게속 어차피? 쓰레드가 실행되고 있으니까
while 링크용 | 데이터용 if 걸어서



start_crawling_signal 시작해서 search_condition_receiver이 실행이 되고 
search_condition_receiver 여기서는  타입, 검색어, 긁어올거 T/F 수집 양 정보 받아와.
이거 하면 tag_link_crawler 바로 실행 함께 됨.
tag_link_crawler 이거는 그냥 바로 링크 크롤링 실행


그럼 2차 크롤링은 언제 해야하냐 ?

저 태그 링크 크롤러가 다 실행된 후에. 해야겠지?



1205 \ 22:05
현재 일단? 2차 크롤링까지 해서 저장은 되고 있지만, 태그가 새로이 저장되는 순간 None값으로 처리되어 들어가고 있고.
갑자기 이전 링크로 들어가서 5번 돌았음에도 제대로 정보가 저장되지 않고 반복되는 현상이 있음.

load_data -> 데이터 뷰어 부분에서 역시 느린것같아 뷰어 부분 되살리기 목적으로 백업



1205_23:16 메모
처리속도가 맞지 않아 빈값이 나오는건가?
2차 크롤링을 하는데 자꾸 link가 제대로 전달되지 않는 문제가 있다.


start_crawling이 먼저 실행이 되고, 시그널을 주는 사이에 print() 먼저 실행이 된다.


link_save_complete_signal으로 start_crawling이 실행이 되고,
그 담에 send_links가 실행이되고,

saver-send_links에서 그 다음에 1차 링크 데이터 전송이 되고,
TupToLinks가 링크를 줘야 for문에서 link가 도는데 그 속도도 느리고 빈값이야. 돌아갈리가 없지.



1206 | 00:18 압축
일단 조건부로 해서 현재 검색 태그만 db에서 찾아서 가져오도록 설정함.
다만, Viewer 띄우는 방식으로 인해 중복 제거된 것임에도 안뜬다.
load_data할때 ITEm을 비우는 방식이 아니었나?

그리고 SQLite 기준 1번째 행에는 데이터가 들어가지 않는 오류가 계속 발생중이다.


1206 | 00:46 압축
라벨러 쓰레드 추가 전 압축.
위 문제 해결중 (1번째 행 이슈는 해결 완)



1206 | 2:37 압축
여전히 QTableWidget은 clear() 안되고 있음.
시스템 메시지 setText 안되고 있음

+ 2:56
/이 포함되어있는 텍스트면 그냥 다 re.sub 과정에서 사라진다


+ 1041
lover 미 선택 시 오류