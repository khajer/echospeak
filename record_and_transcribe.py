import threading
import numpy as np
import sounddevice as sd
import whisper

SAMPLE_RATE = 16000  # whisper expects 16kHz

def record_until_enter():
    chunks = []
    stop = threading.Event()

    def callback(indata, frames, time, status):
        chunks.append(indata.copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32", callback=callback):
        input("Recording... press Enter to stop.\n")
        stop.set()

    return np.concatenate(chunks, axis=0).flatten()

model = whisper.load_model("base")

audio = record_until_enter()
print("Transcribing...")
result = model.transcribe(audio, fp16=False)
print("\nTranscript:", result["text"])
