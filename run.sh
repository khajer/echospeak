#!/bin/bash
set -e

pip install -r requirements.txt

if [ ! -f en_US-lessac-medium.onnx ]; then
    echo "Downloading voice model..."
    curl -L -o en_US-lessac-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx"
    curl -L -o en_US-lessac-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"
fi

python main.py
