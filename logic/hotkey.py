from pynput import keyboard
import threading


class Hotkey(threading.Thread):
  def __init__(self, audiorec):
    super().__init__()
    self.audiorec = audiorec
    self.key = keyboard.KeyCode.from_char('t')
    self.key_listener = keyboard.Listener(on_press=self.on_hotkey_press, on_release=self.on_hotkey_release)


  def on_hotkey_press(self, key):
    if key == self.key:
      self.audiorec.start_recording()

  def on_hotkey_release(self, key):
    if key == self.key:
      self.audiorec.stop_recording()

  def run(self):
    self.key_listener.start()

  def stop(self):
    self.key_listener.stop()

  def set_hotkey(self, key):
    self.key = keyboard.KeyCode.from_char(key)