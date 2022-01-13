#!/bin/bash
OPTH=/var/www/html/wav/sample.wav

tts --model_name tts_models/en/vctk/sc-glow-tts --speaker_idx p256 --text "Just creatingg a wonderful story" --out_path $OPTH
