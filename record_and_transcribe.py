import io
import wave
import numpy as np
import sounddevice as sd
import whisper
from piper.voice import PiperVoice

SAMPLE_RATE = 16000
VOICE_MODEL = "en_US-lessac-medium.onnx"  # ponytail: set path to your downloaded .onnx file

model = whisper.load_model("base")
voice = PiperVoice.load(VOICE_MODEL)

def record_until_enter():
    chunks = []
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32",
                        callback=lambda indata, *_: chunks.append(indata.copy())):
        input("Recording... press Enter to stop.\n")
    return np.concatenate(chunks).flatten()

def speak(text):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        voice.synthesize_wav(text, w)
    buf.seek(0)
    with wave.open(buf) as w:
        pcm = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
        sd.play(pcm, samplerate=w.getframerate(), blocking=True)

try:
    while True:
        audio = record_until_enter()
        print("Transcribing...")
        text = model.transcribe(audio, fp16=False)["text"]
        print("Transcript:", text)
        speak(text)
except KeyboardInterrupt:
    print("\nDone.")
