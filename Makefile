runflask:
	export PYTHONPATH="/home/johnny/code_repo/proScholy/proscholy-data-to-file-export/src:/home/johnny/code_repo/proScholy/proscholy-data-to-file-export"
	flask --app server run -p 3000

cleanpdf:
	rm -f *.pdf

zip:
	zip proscholy_song_export.zip server.py exportpdf.py props.py readme.pdf readme.md
