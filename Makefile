install:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt

run:
	python3 -m venv .venv
	. .venv/bin/activate
	python3 src/app.py

test:
	python3 -m unittest discover -s tests

build:
	docker build -t python-devops .
