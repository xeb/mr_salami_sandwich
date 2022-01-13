#!/bin/bash
virtualenv --python=python3.8 venv
. venv/bin/activate
pip install -r requirements.txt
mkdir -p wav
