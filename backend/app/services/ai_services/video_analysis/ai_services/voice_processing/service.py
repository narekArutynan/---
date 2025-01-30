import speech_recognition as sr
from pydub import AudioSegment

class VoiceProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def process_audio(self, audio_file: str) -> str:
        sound = AudioSegment.from_file(audio_file)
        sound.export("temp.wav", format="wav")
        
        with sr.AudioFile("temp.wav") as source:
            audio = self.recognizer.record(source)
            return self.recognizer.recognize_google(audio, language="ru-RU")
