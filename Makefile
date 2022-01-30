all: publish

.PHONY: all

clean:
	rm -rf *.wav
	rm -rf *.mp3
	rm -rf tmp/*.mp3
	rm -f dialogs.toml
	rm -f wav/final.mp3

story:
	python genstory.py --output_path=output.txt

parse:
	python parsestory.py --input_path=output.txt --output_path=dialogs.toml

render:
	mkdir -p tmp
	python renderdialog.py --input_path=dialogs.toml --output_path=tmp

merge:
	python merge.py --input_path=tmp --output_path=final.mp3

move:
	./move.sh

publish: clean story parse render merge move
audio: clean parse render merge move
