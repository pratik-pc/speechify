class AudioRecorder():
  def __init__(self, main_window):
    self.main_window = main_window
    self.recording = False


  def toggle_recording(self):
    if not self.recording:
      self.start_recording()
      print('start')

    else:
      self.stop_recording()
      print('stop')


  def start_recording(self):
    self.recording = True
    self.main_window.start_stop_button.setText('Stop Recording')

  def stop_recording(self):
    self.recording = False
    self.main_window.start_stop_button.setText('Start Recording')