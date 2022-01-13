import os
import toml
import openai
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")

settings = toml.load("settings.toml")["settings"]
print(f"Using settings {settings}")

parser = argparse.ArgumentParser(description="Generate a Mr. Salami Sandwich Story")
parser.add_argument('--input_path', '-i', required=True)
parser.add_argument('--output_path', '-o', required=True)
args = parser.parse_args()

prompt = ""
with open(args.input_path,"r") as f:
    prompt = f.read()

if settings["input"] is not None:
  prompt = prompt.replace("{INPUT}", settings["input"])

print(f"Using prompt {prompt}")

def complete(prompt):
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      temperature=settings["temperature"],
      max_tokens=(2048 - len(prompt)),
      frequency_penalty=settings["frequency_penalty"],
      presence_penalty=settings["presence_penalty"],
    )

    text = response["choices"][0]["text"]
    return text

text = complete(prompt)
print(text)

story = prompt.strip() + "\n" + text.strip()

if settings["reruns"] > 0:
    for rr in range(0, settings["reruns"]):
        nprompt = '\n'.join(story.split('\n')[-settings["rerun_lines"]:])
        print(f"Using new prompt of \n{nprompt}")
        noutput = complete(nprompt)

        print(f"Received \n{noutput}")
        story = story + noutput

with open(args.output_path, "w") as f:
    f.write(story)

print(f"----\nSaved to {args.output_path}")
