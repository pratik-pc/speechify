from PyQt5.QtWidgets import QWidget, QVBoxLayout
from logic.audiorecorder import AudioRecorder
from .record_button import Button


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.audiorec = AudioRecorder(self)
    self.initUI()

  
  def initUI(self):
    self.setWindowTitle('Speechify')
    self.setGeometry(100, 100, 300, 150)
    self.button = Button(self.audiorec, self)
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    self.setLayout(layout)