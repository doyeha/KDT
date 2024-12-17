241209 압축본 
로그 발생 시 알림 쓰레드 나눔.




App 6 
현 기능
 영상 재생
 위험 구역 지정 - 그리기
 영상 재생 시 위험 구역 필름 생성

frame - 모델 쓰레드화 일부 성공
Log 발생 시 영상 재생 속도 느려지는 이슈 확인
Log 발생 또한 쓰레드화 필요

현재 필요 쓰레드
1-1. Log txt작성
1-2. Log 검색 

2-1. 위험 구역 그리기 쓰레드

3-1. 영상 저장

4-1. 알림 생성
4-2. 알림 띄우기


[MainView.py]
class MainView(QMainWindow, form_class):
class ThreadOfDrawing(QThread, form_class):

[drawing.py]
class Drawing(QMainWindow, form_class):
class PaintView(QLabel):
class ThreadOfDrawing(QThread, form_class):

[setting.py]


[signal_collection.py]
class collectionOfSignals(QObject):


1206_ 10:58
영상 백그라운드 저장하면서 
기초는 -10~+10 으로 하고 
cv2.writer는 파일 형식으로 저장하는건데 최신 10초만 계속 저장되도록 유지할 수 있는가?
사고 3개 동시 발생 시 -10 ~ +10 * 사고 갯수



[방법 1] 백그라운드 저장
메모리 많이 쓰는 방식으로 진행
 * 1080p (1920x1080) 기준 1프레임에 6MB (우리는 화질 구진데???)
30fps/20s -> 3.6GB     ||        20fps/15s -> 1.8GB
ㅁㅊ 우리 2050, 1150 쓰고 있어
30프레임 x 20초 -> 10~20프레임 x 15~20초로 영상 질 낮추기
프레임별 체감 차이 참고 영상 : https://www.youtube.com/shorts/vAFs8AlcKGk
FHD는 해상도 1920x1080가 한계임.
현재 노트북들은 2560x1600  인데 . 이 기준이 아니라 FHD로 해야하나?
그렇게 바꾸면 1280x1024
2,073,600 = 6
1,310,720 = 3.7 메가


if 1280x1024 & 20fps & 20s ==> 1.48GB


방법2] 신호 시 시간 기준 -10초 ~ +10초 다시 read
방법1과는 달리 영상 저장에 10초가 아닌 20초 소모,
메모리 대신 앱이 무거워져 앱 속도 보장 불가능일지도.