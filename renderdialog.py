import re, os
import toml
import subprocess as sp

characters = toml.load("characters.toml")["characters"]
print(f"Characters are {characters}")

f = open("output.txt", "r")
s = f.read()
p = r'\[(.*)\].*"(.*)".*'

i = 0
soxcmds = ["sox"]

def render_polly(voice="Brian", text="Test", output="o.wav"):
    proc = sp.Popen(["aws", "polly", "synthesize-speech",
            "--output-format", "mp3",
            "--voice-id", voice,
            "--text", text,
            f"{output}.mp3"],
            stdout=sp.PIPE,
            stderr=sp.PIPE)

    stdout, stderr = proc.communicate()
    print(f"Rendered polly. {stdout} {stderr}")

    proc = sp.Popen(["ffmpeg", "-i", f"{output}.mp3",
        "-acodec", "pcm_u8", "-ar", "22050", output],
        stdout=sp.PIPE,
        stderr=sp.PIPE)

    stdout, stderr = proc.communicate()
    print(f"Converted to wav. {stdout} {stderr}")

def render_tts():
    MODEL_NAME="tts_models/en/vctk/sc-glow-tts"
    speaker_idx="p234"
    cmd=["tts", "--model_name", MODEL_NAME,
                "--text", dialog,
                "--speaker_idx", speaker_idx,
                "--out_path", ofile,
                ]
        
    soxcmds.append(ofile)

    proc = subprocess.Popen(cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        #stdout, stderr = proc.communicate()
        #print(f"stdout=={stdout}")
        #print(f"stderr=={stderr}")
	

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
    print(f"speaker {speaker} in voice of '{voice}' say '{dialog}'")
    ofile=f"out{i}.wav"

    render_polly(voice=voice, text=dialog, output=ofile)

print("Done")
