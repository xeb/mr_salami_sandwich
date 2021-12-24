import os, sys
import argparse

parser = argparse.ArgumentParser(description="Parse a story to create dialog objects")
parser.add_argument('--input_path', '-i', required=True)
parser.add_argument('--output_path', '-o', required=True)
args = parser.parse_args()

cmd = 'ffmpeg -i "concat:'

files = os.listdir(args.input_path)
files.sort()

for f in files:
    if f.endswith(".mp3") and f.startswith("out"):
        print(f"Merging {f}")
        cmd = cmd + f"{args.input_path}/{f}|"

cmd = cmd[:-1]
cmd = cmd + f'" -acodec copy {args.output_path}'

os.system(cmd)
print(cmd)
