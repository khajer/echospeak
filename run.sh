#!/bin/bash
set -e

pip install -r requirements.txt

if [ ! -f en_US-amy-medium.onnx ]; then
    echo "Downloading voice model..."
    curl -L -o en_US-amy-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx"
    curl -L -o en_US-amy-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx.json"
fi

python main.py
