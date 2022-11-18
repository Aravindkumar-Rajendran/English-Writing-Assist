import pyaudio
import wave
import whisper
import numpy as np

# ! pip install -q git+https://github.com/openai/whisper.git
# ! pip install -q jiwer

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS  = 1
RATE = 44100
seconds = 5


p = pyaudio.PyAudio()

while input("continue..."):
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("start recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Stop recording")

    stream.stop_stream()
    stream.close()
    # p.terminate()

    wave_file = wave.open("speech.wav", "wb")
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(p.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()


    model = whisper.load_model("tiny.en")
    result = model.transcribe("speech.wav")
    print("Transcription: \n", result["text"])

