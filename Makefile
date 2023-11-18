install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py
lint:
	pylint --disable=R,C namecheck.py
test:
	python -m pytest -vv --cov=namecheck test_*.py

all: install format lint test
