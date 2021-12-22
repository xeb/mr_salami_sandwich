import os, sys

cmd = "sox "

files = os.listdir(".")
files.sort()

for f in files:
    if f.endswith(".wav") and f.startswith("out"):
        print(f"Merging {f}")
        cmd = cmd + f + " "

cmd = cmd + " finally.wav"
os.system(cmd)
