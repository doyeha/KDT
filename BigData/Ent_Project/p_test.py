import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import *
# 원본 이미지 불러오기
# original_image = cv2.imread('example.jpg')  # 1920x1080 이미지

# # 이미지 축소 (1280x720)
# resized_image = cv2.resize(original_image, (1280, 720), interpolation=cv2.INTER_LINEAR)

# # 이미지 확대 (1920x1080)
# restored_image = cv2.resize(resized_image, (1920, 1080), interpolation=cv2.INTER_LINEAR)

# 결과 이미지 비교
cv2.imshow('Original Image', original_image)
cv2.imshow('Resized Image (1280x720)', resized_image)
cv2.imshow('Restored Image (1920x1080)', restored_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

test_video = r"C:\Users\kjy19\OneDrive\Desktop\Detect_test_Cam5 - Trim.MP4"


class test_video(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Quality Comparison")
        self.setGeometry(100, 100, 1300, 600)



    cap = cv2.VideoCapture(test_video)  # 저장된 영상 가져오기 프레임별로 계속 가져오는 듯
    while ret:
        ret, frame = cap.read()  # 알아서 0번부터 끝까지 착실히 넘어가면서 수행
        if ret:
                rgbImage = cv2.cvtColor(predicted_frame, cv2.COLOR_BGR2RGB)  # 프레임에 색 입히기
                convertToQtFormat = QImage(rgbImage.data,rgbImage.shape[1],rgbImage.shape[0],QImage.Format_RGB888,)
                pixmap = QPixmap(convertToQtFormat)  # 이 부분이 메인스레드에서 처리되어야하는 QPixmap이 있어서 2개 다 잡아먹고 있는거다?
                p = pixmap.scaled(2050, 1150, QtCore.Qt.IgnoreAspectRatio)  # 프레임 크기 조정 1920, 1080 후보 1
                current_time = cap.get(cv2.CAP_PROP_POS_MSEC) * 0.001  # 밀리초 단위 현재 위치
                frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
                if type(int(frame_number) % int(fps)) is int:   # 이게 int값 되는 순간인디
                    print(f"fps : {fps}, frame_number : {frame_number}")
                    signal.video_playing_signal.emit(current_time)  # video_playing_signal을 통해 메인쓰레드로 변수 전송               
                    signal.silder_signal.emit(length, fps, current_time)
                pixmap_signal.emit(p)
                video_frame.update()  # 프레임 띄우기
                predicted_frame = None
                delay = int(1000/fps)
                cv2.waitKey(delay)  # fps에 맞게 프레임 지연이라는데 이게 sleep이랑 같은 역할을 하나?
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    running = False