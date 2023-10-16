from PyQt5.QtWidgets import QPushButton
from logic.audiorecorder import AudioRecorder


class Button(QPushButton):
  def __init__(self, audiorec, parent=None):
    super().__init__('Start Recording', parent)
    self.audiorec = audiorec
    self.clicked.connect(self.audiorec.toggle_recording)