


default: all
all: install run

install:
	python -m venv ./.venv/
	./.venv/bin/python -m pip install -r requirements.txt

run: test
	.venv/bin/python src/main.py

test:
	.venv/bin/python -m pytest

lint:
	.venv/bin/python -m mypy ./src/main.py

clean:
	rm -rf ./venv
	rm -rf ./.venv
