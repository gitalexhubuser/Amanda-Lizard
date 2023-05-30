import json, pyaudio
from vosk import Model, KaldiRecognizer
import os
import wave
import json

# либы от сюда https://alphacephei.com/vosk/models
model = Model(r"O:\PythonProjects\Amanda-Lizard\vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,  frames_per_buffer=8192)

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)
        print(text[14:-3])