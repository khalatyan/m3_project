from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='m3_project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=(
        'Django==2.2',
        'm3-builder==1.2.0',
        'm3-core==2.2.24',
        'm3-django-compat==1.10.1',
        'm3-objectpack==2.2.46',
        'm3-ui==2.2.97',
        'psycopg2==2.7.7',
        'psycopg2-binary==2.9.1',
    ),
)