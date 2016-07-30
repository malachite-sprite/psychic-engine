from setuptools import setup
from os import path

# deploy steps:
# $ virtualenv -p python3 --no-site-packages ./
# $ pip install -r requirements.txt
# $ python setup.py install

# test steps:
# $ coverage run setup.py test
# $ coverage report

package_name = path.basename(
        path.dirname(path.realpath(__file__))
)

setup(name=package_name,
    packages=['sources'],
    license='MIT',
    setup_requires=['pytest_runner'],
    tests_require=['pytest'],
)    
