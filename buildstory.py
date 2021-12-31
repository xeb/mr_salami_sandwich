import os
import openai
from settings import settings

openai.api_key = os.getenv("OPENAI_API_KEY")

input_path = settings["input_path"]

prompt = ""
with open(input_path,"r") as f:
    prompt = f.read()

print(f"Using prompt {prompt}")

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=settings["temperature"],
  max_tokens=settings["max_tokens"],
  top_p=settings["top_p"],
  frequency_penalty=settings["frequency_penalty"],
  presence_penalty=settings["presence_penalty"],
  #stop=["\n"]
)

print(response)

text = response["choices"][0]["text"]

with open(settings["output_path"],"w") as f:
    f.write(prompt)
    #f.write("---\n")
    f.write(text)

print(f"Saved to {settings['output_path']}")
