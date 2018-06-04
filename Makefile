clean:
	find . -type d -name "__pycache__" -delete
	find . -name '*.pyc' -delete

install:
	python setup.py install

refresh: clean install
