# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running

```bash
python record_and_transcribe.py
```

Ctrl+C to exit the loop.

## Dependencies

```bash
pip install openai-whisper sounddevice numpy piper-tts
```

Voice model files (`en_US-lessac-medium.onnx` + `.onnx.json`) must be present in the working directory, or `VOICE_MODEL` updated to the full path.

## Architecture

Single file (`record_and_transcribe.py`) — no modules, no config files.

**Flow (loops until Ctrl+C):**
1. `record_until_enter()` — streams mic via `sounddevice.InputStream` at 16 kHz float32 into a list of chunks; blocks on `input()` until Enter, then concatenates chunks into a flat numpy array.
2. `whisper.load_model("base").transcribe()` — runs OpenAI Whisper on the in-memory audio array (`fp16=False` for CPU/MPS compatibility).
3. `speak()` — synthesizes text via `PiperVoice.synthesize_wav()` into an in-memory WAV buffer, reads back as int16 PCM, plays with `sounddevice`.

Both `whisper` model and `PiperVoice` are loaded once at startup (module level) to avoid reload cost per loop iteration.

## Voice model

To swap voices, download any model from the piper-voices HuggingFace repo and update `VOICE_MODEL`. Both `.onnx` and `.onnx.json` files are required.
