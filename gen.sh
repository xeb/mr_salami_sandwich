#!/bin/bash
source key.sh 2> /dev/null
MAX_TOKENS=1700
python buildstory.py --max_tokens=$MAX_TOKENS --input_path=prompt.txt --output_path=output.txt
echo "---"
cat output.txt
echo "---"
