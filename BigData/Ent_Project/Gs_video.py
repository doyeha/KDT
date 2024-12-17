import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer


class VideoDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 메인 윈도우 설정
        self.setWindowTitle("Resized and Restored Video")
        self.setGeometry(100, 100, 1920, 1080)

        # QLabel 설정 (영상 표시)
        self.video_label = QLabel(self)
        self.video_label.setFixedSize(1920, 1080)  # 표시할 영상의 크기 설정
        self.video_label.setStyleSheet("background-color: black;")  # 배경색을 검정으로 설정

        # 버튼 설정
        self.select_button = QPushButton("Select Video", self)
        self.select_button.clicked.connect(self.select_video)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.select_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        # 비디오 캡처 객체
        self.cap = None

    def select_video(self):
        # 비디오 파일 선택
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mkv)", options=options)

        if file_name:
            self.cap = cv2.VideoCapture(file_name)
            self.timer.start(30)  # 30ms마다 프레임 업데이트

    def update_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                self.timer.stop()
                self.cap.release()
                return

            # 해상도 변환: 1920x1080 -> 1280x720 -> 1920x1080
            # resized_frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_LINEAR)
            resized_frame = cv2.resize(frame, (640, 360), interpolation=cv2.INTER_LINEAR)
            restored_frame = cv2.resize(resized_frame, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_LINEAR)

            # BGR -> RGB 변환 (OpenCV -> PyQt용 이미지)
            restored_frame_rgb = cv2.cvtColor(restored_frame, cv2.COLOR_BGR2RGB)
            self.display_frame(self.video_label, restored_frame_rgb)

    def display_frame(self, label, frame):
        # OpenCV 이미지를 PyQt QPixmap으로 변환해 QLabel에 표시
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(q_image).scaled(1920, 1080))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoDisplayApp()
    window.show()
    sys.exit(app.exec_())
