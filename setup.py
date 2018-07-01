from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='td-cli',
    version='0.0.1',
    description='A todo command line tool',
    url='https://github.com/darrikonn/td-cli',
    author='Darri Steinn Konn Konradsson',
    author_email='darrikonn@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='todo commandline',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, <4',
    install_requires=[],
    entry_points={
        'console_scripts': [
            # TODO
            'todo=todo:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/darrikonn/td-cli',
    },
)