#!/bin/bash
output=$(python -c 'import toml; print(toml.load("settings.toml")["settings"]["output"])')
mv final.mp3 wav/$output
