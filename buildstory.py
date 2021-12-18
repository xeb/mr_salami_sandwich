import os
import openai
import argparse

temperature=0.7
top_p=1

openai.api_key = os.getenv("OPENAI_API_KEY")

parser = argparse.ArgumentParser(description="Generate a Mr. Salami Sandwich Story")
parser.add_argument('--input_path', '-i', required=True)
parser.add_argument('--output_path', '-o', required=True)
parser.add_argument('--max_tokens', '-mt', required=True, type=int)
args = parser.parse_args()

prompt = ""
with open(args.input_path,"r") as f:
    prompt = f.read()

print(f"Using prompt {prompt}")

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=temperature,
  max_tokens=args.max_tokens,
  top_p=top_p,
  #frequency_penalty=1.1,
  #presence_penalty=1.1,
  #stop=["\n"]
)

print(response)

text = response["choices"][0]["text"]

with open(args.output_path,"w") as f:
    f.write(prompt)
    f.write("---\n")
    f.write(text)

print(f"Saved to {args.output_path}")
