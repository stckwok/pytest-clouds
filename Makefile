install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black namecheck.py test_namecheck.py
lint:
	pylint --disable=R,C namecheck.py
test:
	python -m pytest -vv --cov=namecheck test_namecheck.py

all: install format lint test
