# deals with creating the virtualenv, running pip install, and
# generally setting up the box
default: install

install: requirements.txt sources/ 
	virtualenv -p python3 --no-site-packages ./
	pip install --upgrade -r requirements.txt

test: tests/
	coverage run py.test tests/
	coverate report

report: 
	coverage report

