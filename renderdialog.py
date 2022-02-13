import re, os
import toml
from tqdm import tqdm
import subprocess as sp
import argparse

parser = argparse.ArgumentParser(description="Parse a story to create dialog objects")
parser.add_argument("--input_path", "-i", required=True)
parser.add_argument("--output_path", "-o", required=True)
args = parser.parse_args()

dialogs = toml.load(args.input_path)["dialogs"]


def render_polly(voice="Brian", text="Test", output="o.wav"):
    proc = sp.Popen(
        [
            "aws",
            "polly",
            "synthesize-speech",
            "--output-format",
            "mp3",
            "--voice-id",
            voice,
            "--text",
            text,
            f"{args.output_path}/{output}.mp3",
        ],
        stdout=sp.PIPE,
        stderr=sp.PIPE,
    )

    stdout, stderr = proc.communicate()
    print(f"Rendered polly. {stdout} {stderr}")


for dialog in tqdm(dialogs):
    #print(f"Rendering {dialog}")
    render_polly(voice=dialog["voice"], text=dialog["text"], output=dialog["output"])

print("Done")
