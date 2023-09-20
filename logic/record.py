import pyaudio
import wave


class Record:
  def __init__(self, audiorecorder):
    self.audiorecorder = audiorecorder
    self.pyaudio = pyaudio.PyAudio()
    self.stream = None
    self.audio_data = []
    self.frames_per_buffer = 1024


  def start_stream(self):
    self.audio_data = []
    self.stream = self.pyaudio.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=self.frames_per_buffer,
                                  stream_callback=self.audio_callback)
    self.stream.start_stream()


  def audio_callback(self, in_data, frame_count, time_info, status):
    if self.audiorecorder.recording:
      self.audio_data.append(in_data)

    return in_data, pyaudio.paContinue
  
  def save_audio(self):
        wf = wave.open('sample.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.pyaudio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.audio_data))
        wf.close()