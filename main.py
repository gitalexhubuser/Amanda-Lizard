import os
from gtts import gTTS #pip install gtts
import speech_recognition as sr # pip install SpeechRecognition #pip install pyaudio



# from gtts import gTTS #pip install gtts
# import speech_recognition as sr #pip install SpeechRecognition #pip install pyaudio

def JarvisRecord(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        voice_result = r.recognize_google(audio, show_all=True, language="ru-RU")
        ts = voice_result['alternative'][0]['transcript'].lower() # transcript_value
        print("Gotham: распознал следующие слова:", ts)
        # print("Gotham: распознал следующие слова:", voice_result)
    except sr.UnknownValueError:
        print('Gotham: Не удалось распознать аудио')

if __name__ == '__main__':
    # JarvisRecord("videoconvertU4ewLfb.wav")
    # JarvisRecord("ExquisiteSmoothPorcupineCurseLit-va5UBQYvWaE4sw8F.wav")
    JarvisRecord("reduced.wav")
