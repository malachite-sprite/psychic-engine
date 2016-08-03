# deals with creating the virtualenv, running pip install, and
# generally setting up the box
default: install

install: requirements.txt
	virtualenv -p python3 --no-site-packages ./; \
	source bin/activate; \
	python setup.py install; \
	pip install --upgrade -r requirements.txt; \
	echo 'remember to source bin/activate!'; \

store:
	pip freeze > requirements.txt
	coverage report > coverage.txt

test: tests/
	py.test --cov=tests/ tests/

