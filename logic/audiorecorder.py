from logic.record import Record
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


  def start_recording(self):
    self.recording = True
    self.main_window.start_stop_button.setText('Stop Recording')
    self.record.start_stream()

  def stop_recording(self):
    self.recording = False
    self.main_window.start_stop_button.setText('Start Recording')
    self.record.stream.stop_stream()
    self.record.stream.close()

    self.record.save_audio()