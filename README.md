# highScoreService

This modules solves the problem in two differents manners, in the ```class
MemScoreService``` the state of the score is mantained in memory, in the ```class
MongoScoreService``` such state is mantained in a mongoDb database.
Besides ```MemScoreService```, only uses the standard python library.

Requires [python](https://www.python.org/) 2.7.13

```
$ apt-get install mongodb

$ apt-get install virtualenv

$ virtualenv HSSVENV

$ source HSSVENV/bin/activate

(HSSENV)$ pip install pymongo

(HSSENV)$ git clone https://github.com/lmpizarro/highScoreService.git

(HSSENV)$ cd highScoreService/tests/

(HSSENV)$ python test.py
.
.
.

(HSSENV)$ cd ..

(HSSENV)$ python setup.py install

(HSSENV)$ python -c "from highScoreService import memScoreService"

(HSSENV)$ python -c "from highScoreService import mongoScoreService"

```

To generate the documentation, [Sphinx](http://www.sphinx-doc.org/en/master/) must be  installed:

```
$ cd docs

$ make singlehtml
```
