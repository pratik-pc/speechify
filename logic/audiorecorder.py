from logic.record import Record
from api.transcribe_api import transcribe
from logic.speech import speech
import subprocess

class AudioRecorder():
  def __init__(self, main_window):
    self.main_window = main_window
    self.recording = False
    self.record = Record(self)


  def toggle_recording(self):
    if not self.recording:
      print('start')
      self.start_recording()
      

    else:
      self.stop_recording()
      print('stop')
      text = self.call_api()
      subprocess.run(['venv\Scripts\python', 'logic\websocket_message_service.py'])


  def start_recording(self):
    self.recording = True
    self.main_window.button.setText('Stop Recording')
    self.record.start_stream()

  def stop_recording(self):
    self.recording = False
    self.main_window.button.setText('Start Recording')
    self.record.stream.stop_stream()
    self.record.stream.close()

    self.record.save_audio()

  def call_api(self):
    return transcribe()