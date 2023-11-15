install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C namecheck.py

test:
	python -m pytest -vv --cov=namecheck test_namecheck.py
