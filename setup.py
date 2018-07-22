# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='highScoreService',
    version='0.1.0',
    description='Memory and MongoDb High Score Service',
    long_description=readme,
    author='Luis Marìa Pizarro',
    author_email='lmpizarro@gmail.com',
    url='https://github.com/lmpizarro/highScoreService',
    license=readme,
    packages=find_packages(exclude=('tests', 'docs'))
)

