from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from logic.audiorecorder import AudioRecorder


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.audiorec = AudioRecorder(self)
    self.initUI()

  
  def initUI(self):
    self.setWindowTitle('Speechify')
    self.setGeometry(100, 100, 300, 150)
    self.start_stop_button = QPushButton('Start Recording', self)
    self.start_stop_button.clicked.connect(self.audiorec.toggle_recording)

    layout = QVBoxLayout()
    layout.addWidget(self.start_stop_button)
    self.setLayout(layout)