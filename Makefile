# deals with creating the virtualenv, running pip install, and
# generally setting up the box
default: install

install: requirements.txt
	virtualenv -p python3 --no-site-packages ./
	python setup.py install
	pip install --upgrade -r requirements.txt

store:
	pip freeze > requirements.txt

test: tests/
	py.test --cov=tests/ tests/

