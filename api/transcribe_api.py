import requests
import asyncio

async def transcribe(language):
  loop = asyncio.get_event_loop()
  url = 'http://localhost:5000/api/transcribe'
  audio_path = 'C:\project\speechify\sample.wav'

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
        response = await loop.run_in_executor(None, lambda: requests.post(url, files=files, data=data))
        return response.text
  except IOError as e:
      print(f"Failed to open the audio file: {str(e)}")