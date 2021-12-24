import re, os
import toml
import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="Parse a story to create dialog objects")
parser.add_argument('--input_path', '-i', required=True)
parser.add_argument('--output_path', '-o', required=True)
args = parser.parse_args()

s = ""
with open(args.input_path,"r") as f:
    s = f.read()

characters = toml.load("settings.toml")["characters"]

p = r'\[(.*)\].*"(.*)".*'

i = 0

dialogs = []

for l in s.split('\n'):
    i = i + 1
    print("---")
    print(f"Parsing line {l}")
    s = re.search(p, l)
    if s is None:
        continue

    voice = characters["unknown"]["voice"]
    speaker = s.group(1)
    if speaker in characters.keys():
        voice = characters[speaker]["voice"]

    dialog = s.group(2)
    ofile=f"out{i:03}"

    d = {
        "voice": voice,
        "text": dialog,
        "output": ofile,
    }

    print(d)
    dialogs.append(d)

with open(args.output_path, "w") as f:
    data = toml.dumps({"dialogs": dialogs})
    f.write(data)
    print(f"Wrote to {args.output_path}")

