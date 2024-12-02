from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
import cv2
import time

class VideoThread(QThread):
    frame_signal = pyqtSignal(QPixmap)  # QLabel 업데이트용 신호
    def __init__(self, video_file):
        super().__init__()
        self.video_file = video_file
        self.running = True  # 루프 상태 제어
        self.pause = False   # 일시정지 상태

    def run(self):
        cap = cv2.VideoCapture(self.video_file)
        while self.running:
            if self.pause:
                time.sleep(0.1)  # 일시 정지 상태면 루프를 멈춤
                continue

            ret, frame = cap.read()
            if not ret:
                break

            # 프레임 처리 (OpenCV -> QPixmap 변환)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)

            # QLabel로 프레임 전달
            self.frame_signal.emit(pixmap)
            time.sleep(0.01)  # 프레임 속도 조절

        cap.release()

    def stop(self):
        self.running = False

    def toggle_pause(self):
        self.pause = not self.pause


from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class VideoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player with Button Control")

        # UI 구성
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)
        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        # 스레드 설정
        self.video_thread = None

        # 버튼 이벤트 연결
        self.start_button.clicked.connect(self.start_video)
        self.pause_button.clicked.connect(self.pause_video)
        self.stop_button.clicked.connect(self.stop_video)

    def start_video(self):
        if self.video_thread is None or not self.video_thread.isRunning():
            self.video_thread = VideoThread(r"C:\Users\kjy19\Videos\y2mate.com - 황정민  APT_720pFH.mp4")
            self.video_thread.frame_signal.connect(self.update_frame)
            self.video_thread.start()

    def pause_video(self):
        if self.video_thread:
            self.video_thread.toggle_pause()

    def stop_video(self):
        if self.video_thread:
            self.video_thread.stop()
            self.video_thread.wait()
            self.video_thread = None

    def update_frame(self, pixmap):
        self.video_label.setPixmap(pixmap)

    def closeEvent(self, event):
        if self.video_thread:
            self.video_thread.stop()
            self.video_thread.wait()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VideoApp()
    window.show()
    sys.exit(app.exec_())
