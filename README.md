# echospeak

Speak into your mic — echospeak transcribes it with OpenAI Whisper and reads it back using a local text-to-speech voice (piper-tts). Runs in a continuous loop until you press Ctrl+C.

## Quick start

```bash
./run.sh
```

This installs dependencies, downloads the voice model, and launches the app.

## Manual setup

```bash
pip install -r requirements.txt

# Download voice model (~60 MB)
curl -L -o en_US-amy-medium.onnx \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx"
curl -L -o en_US-amy-medium.onnx.json \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx.json"

python3 main.py
```

## Usage

1. Press **Enter** to stop recording
2. Wait for transcription and playback
3. Repeat — press **Ctrl+C** to quit

## Changing the voice

Download any voice from [piper-voices on HuggingFace](https://huggingface.co/rhasspy/piper-voices) (both `.onnx` and `.onnx.json` files), then update `VOICE_MODEL` in `main.py`.

## Docker

```bash
docker build -t echospeak .
docker run -it --device /dev/snd echospeak
```

> Audio device passthrough (`--device /dev/snd`) works on Linux only.

## Dependencies

| Package | Role |
|---|---|
| `openai-whisper` | Speech-to-text transcription |
| `piper-tts` | Local text-to-speech |
| `sounddevice` | Mic input and audio playback |
| `numpy` | Audio buffer handling |
