all: publish

.PHONY: all

clean:
	rm -rf *.wav
	rm -rf *.mp3
	rm -f dialogs.toml

story:
	python genstory.py --input_path=prompt.txt --output_path=output.txt

parse:
	python parsestory.py --input_path=output.txt --output_path=dialogs.toml

render:
	python renderdialog.py --input_path=dialogs.toml --output_path=tmp

merge:
	python merge.py --input_path=tmp --output_path=final.mp3

copy:
	mv final.mp3 wav/

publish: clean story parse render merge copy
