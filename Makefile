clean:
	find . -type d -name "__pycache__" -delete
	find . -name '*.pyc' -delete
	rm -rf build/
	rm -rf *.egg-info/

install:
	python setup.py install

refresh: clean install
