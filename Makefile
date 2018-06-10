clean:
	find . -type d -name "__pycache__" -delete
	find . -name '*.pyc' -delete
	rm -rf build/
	rm -rf *.egg-info/

install:
	python setup.py install

refresh: clean install

autopep:
	time autopep8 --in-place --recursive --max-line-length=79 awork/schema

clear_schema:
	rm -rf awork/schema/current  # could have files that were removed

schema_cmd:
	time awork produce_schema

schema:clear_schema schema_cmd autopep
