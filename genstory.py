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

print(f"Using prompt {prompt}")

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=settings["temperature"],
  max_tokens=settings["max_tokens"],
  frequency_penalty=settings["frequency_penalty"],
  presence_penalty=settings["presence_penalty"],
)

text = response["choices"][0]["text"]
print(text)

with open(args.output_path,"w") as f:
    f.write(prompt)
    f.write(text)

print(f"----\nSaved to {args.output_path}")
