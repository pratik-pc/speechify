from PyQt5.QtWidgets import QPushButton
from logic.audiorecorder import AudioRecorder
from pynput import keyboard


class Button(QPushButton):
  def __init__(self, audiorec, parent=None):
    super().__init__('Start Recording', parent)
    self.audiorec = audiorec
    self.clicked.connect(self.audiorec.toggle_recording)


class PushButton(QPushButton):
  def __init__(self, hotkey_instance, parent=None):
    super().__init__('Record Keybind', parent)
    self.hotkey_instance = hotkey_instance        # Assign Global Hotkey instance 
    self.clicked.connect(self.change_hotkey)

  def on_key_press(self, key):
    if isinstance(key, keyboard.KeyCode):
      self.hotkey_instance.set_hotkey(key.char)
      self.hotkey_listener.stop()         # Stop the local listener after changing the hotkey

  def change_hotkey(self):
    self.hotkey_listener = keyboard.Listener(on_press=self.on_key_press)      # Create local keyboard listener to catch key for changing hotkey
    self.hotkey_listener.start()