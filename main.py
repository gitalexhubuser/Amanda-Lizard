import json, pyaudio
from vosk import Model, KaldiRecognizer
import os
import wave
import json

# либы от сюда https://alphacephei.com/vosk/models

model = Model(r"O:\PythonProjects\Amanda-Lizard\vosk-model-small-ru-0.22")
# model = Model(r"O:\PythonProjects\Amanda-Lizard\vosk-model-ru-0.10")

# recognizer = KaldiRecognizer(model, 16000)

# # работает !
# mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,  frames_per_buffer=8192)

# while True:
#     data = stream.read(4096)
#     if recognizer.AcceptWaveform(data):
#         text = recognizer.Result()
#         print(text[14:-3])


# открываем аудиофайл и читаем его содержимое в переменную audio_file
# audio_file = wave.open("videoconvertU4ewLfb.wav")
audio_file = wave.open("reduced.wav")

# создаем объект Recognizer для распознавания речи
recognizer = KaldiRecognizer(model, audio_file.getframerate())

# создаем список для сохранения результатов распознавания
results = []

# читаем данные из аудиофайла по блокам и передаем их на распознавание
while True:
    data = audio_file.readframes(nframes=8000)
    # if len(data) == 0:
    #     break
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result["text"]
        results.append(text)

# получаем результаты распознавания
    result = json.loads(recognizer.FinalResult())
    text = result["text"]
    results.append(text)

    print(results)
