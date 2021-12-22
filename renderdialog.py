import re, os
import subprocess as sp

MODEL_NAME="tts_models/en/vctk/sc-glow-tts"
speaker_idx="p234"
OUTPUT_FILE="final.wav"

s = '[a]: "hi there"\n[bahhh+test]:"cool"\n[ong]: "hey"'

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

for l in s.split('\n'):
        i = i + 1
        print("---")
        print(f"Parsing line {l}")
        s = re.search(p, l)
        if s is None:
            continue

        speaker = s.group(1)
        dialog = s.group(2)
        print(f"in voice of '{speaker}' say '{dialog}'")
        ofile=f"out{i}.wav"

        render_polly(voice="Brian", text=dialog, output=ofile)
        continue

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
	
print("~~~~ MIXING audio ~~~~~")
soxcmds.append("finally.wav")
print(f"Mixing with {soxcmds}")

proc = sp.Popen(soxcmds,
        stdout=sp.PIPE,
        stderr=sp.PIPE)

stdout, stderr = proc.communicate()
print(f"stdout=={stdout}")
print(f"stderr=={stderr}")


os.system("mv finally.wav ./wav/")
#os.system("rm -f *.wav")

