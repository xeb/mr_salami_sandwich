import re, os
import toml
import argparse
import random
import subprocess as sp

parser = argparse.ArgumentParser(description="Parse a story to create dialog objects")
parser.add_argument('--input_path', '-i', required=True)
parser.add_argument('--output_path', '-o', required=True)
args = parser.parse_args()

s = ""
with open(args.input_path,"r") as f:
    s = f.read()

s = s.replace("[", "\n[")
s = s.replace(":", "")
s = s.replace("xa0", "")
s = s.replace("\xa0", "")

characters = toml.load("settings.toml")["characters"]

def get_voice(speaker):
    if speaker in characters.keys():
        voice = characters[speaker]["voice"]

        
p = r'\[(.*)\]:?(.*)' # expected dialog
p2 = r'\[(.*)\](.*)' # backup

i = 0

dialogs = []
sm = {}

for l in s.split('\n'):
    l = l.strip()
    l = l.replace("\"","")
    i = i + 1
    print("---")
    print(f"Parsing line {l}")
    
    voice = characters["unknown"]["voice"] # use unknown for standard looking dialogs
    voice = None
    dialog = None

    s = re.search(p, l)
    if s is None:
        
        print("BACKUP DIALOG")
        s = re.search(p2, l)
        voice = characters["narrator"]["voice"] # use narrator as backup for weird lines

        # Magic strings
        if l.strip() == "<|endoftext|>":
            print(f"Skipping because")
            continue

        if len(l) > 10:
            dialog = l # just make the whole line a narration

    # Parse standard
    if s is not None:
        speaker = s.group(1).replace(" ", "").strip()
        if speaker in characters.keys():
            voice = characters[speaker]["voice"]
            sm[speaker] = voice
        elif speaker in sm.keys():
            voice = sm[speaker]
            print(f"Reusing voice {voice} for {speaker}")
        else:
            print(f"No voice, picking random")

            acs = list(characters.keys())
            random.shuffle(acs)

            for c in acs:
                print(f"Looking for rando, checking out {c}")
                if c not in sm.keys():
                    voice = characters[c]["voice"]
                    sm[speaker] = voice
                    print(f"Picking rando character of {voice} for {speaker}!")
                    break
                else:
                    print(f"Skipping {c} because they are in {sm.keys()}")

        dialog = s.group(2)

    if dialog is None or len(dialog.strip()) == 0:
        continue

    ofile=f"out{i:03}"

    if voice is None:
        print(f"OMFG, what?")
        sys.exit(1)

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

