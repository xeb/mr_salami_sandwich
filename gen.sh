#!/bin/bash
source key.sh 2> /dev/null
output_path=$(toml get --toml-path settings.toml output_path)
python buildstory.py
echo "---"
less $output_path
echo "---"
