
from setuptools import setup, find_packages

setup(
    name='excellib',
    version='0.1.0',
    author='Kevin Dick',
    author_email='kevinedick@gmail.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='http://github.cyanoptics.com/kevinedick/spreadsheet',
    description="A package to help parse .csv files into tablib for quick formatting",
    long_description=open('README.md').read(),
    install_requires=[
        "tablib >= 0.10.0",
    ],
)
