from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from logic.audiorecorder import AudioRecorder
from .record_button import Button, PushButton
from .dropdown import Dropdown
from logic.hotkey import Hotkey


class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.audiorec = AudioRecorder(self)
    self.hotkey_listener = Hotkey(self.audiorec)
    self.hotkey_listener.start()
    self.initUI()

  
  def initUI(self):
    self.setWindowTitle('Speechify')
    self.setGeometry(100, 100, 300, 150)
    self.setFixedSize(300, 150)
    self.button = Button(self.audiorec, self)
    self.push_button = PushButton(self.hotkey_listener)
    self.dropdown = Dropdown(self.audiorec, self)
    self.label1 = QLabel("change hotkey", self)
    hbox_layout = QHBoxLayout()
    hbox_layout.addWidget(self.label1)
    hbox_layout.addWidget(self.push_button)
    layout = QVBoxLayout()
    self.label = QLabel('Select Language:', self)
    layout.addWidget(self.label)
    layout.addWidget(self.dropdown)
    layout.addWidget(self.button)
    layout.addLayout(hbox_layout)
    self.setLayout(layout)


  def closeEvent(self, event):
    self.hotkey_listener.stop()
    event.accept()