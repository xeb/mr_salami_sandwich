# Mr. Salami Sandwich
Once upon a time, there once was a sandwich named Mr. Salami Sandwich. He was made from two pieces of sourdough bread and had salami in the middle of his body. 

This is a story generation codebase that takes an input prompt and creates audio dialogs as MP3 files of the characters from the story.

## Notes
This is all a big hack right now... nothing to see yet. To get started, do something like this:

```
./setup.sh
echo "export OPENAI_API_KEY=\"{YOUR_OPENAI_API_KEY}\"" > key.sh
source key.sh
make
```

Be sure to look at `settings.toml` for various options, including a "rerun" feature that creates longer stories from the final lines of a previously generated prompt.
