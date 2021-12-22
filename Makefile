.PHONY:
	echo "Phone"

clean:
	rm -rf *.wav
	rm -rf *.mp3

story:
	python buildstory.py

render:
	python renderdialog.py

merge:
	python merge.py
