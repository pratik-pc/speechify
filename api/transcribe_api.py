import requests

def transcribe(language):
  url = 'http://localhost:5000/api/transcribe'
  audio_path = 'C:\project\speechify\sample.wav'
  # language = 'hi-IN'

  data = {
      'language': language,
  }
  files = {
     'audio': None
  }
  try:
    with open(audio_path, 'rb') as audio_file:
        files['audio'] = (audio_file.name, audio_file, 'audio/wav')
        print("Audio file opened successfully.")
        response = requests.post(url, files=files, data=data)
        return response.text
  except IOError as e:
      print(f"Failed to open the audio file: {str(e)}")