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