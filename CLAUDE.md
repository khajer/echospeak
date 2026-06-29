# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running

```bash
./run.sh        # first-time setup: installs deps, downloads voice model, then launches
python3 main.py # subsequent runs (once deps and model are in place)
```

Ctrl+C to exit the loop.

## Dependencies

```bash
pip install -r requirements.txt
```

Voice model files (`en_US-amy-medium.onnx` + `.onnx.json`) must be present in the working directory, or `VOICE_MODEL` in `main.py` updated to the full path. `run.sh` downloads them automatically if missing.

## Architecture

Single file (`main.py`) — no modules, no config files.

**Flow (loops until Ctrl+C):**
1. `record_until_enter()` — streams mic via `sounddevice.InputStream` at 16 kHz float32 into a list of chunks; blocks on `input()` until Enter, then concatenates chunks into a flat numpy array.
2. `whisper.load_model("base").transcribe()` — runs OpenAI Whisper on the in-memory audio array (`fp16=False` for CPU/MPS compatibility).
3. `speak()` — synthesizes text via `PiperVoice.synthesize_wav()` into an in-memory WAV buffer, reads back as int16 PCM, plays with `sounddevice`.

Both `whisper` model and `PiperVoice` are loaded once at startup (module level) to avoid reload cost per loop iteration.

## Voice model

Default voice: `en_US-amy-medium` (American female). To swap, download any model from the [piper-voices HuggingFace repo](https://huggingface.co/rhasspy/piper-voices) and update `VOICE_MODEL` in `main.py`. Both `.onnx` and `.onnx.json` files are required. Use `PiperVoice.synthesize_wav()` — `synthesize()` and `synthesize_stream_raw()` do not exist in piper-tts 1.4.2.
