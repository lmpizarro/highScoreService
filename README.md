# highScoreService

Requires python 2.7.13

```
$ apt-get install mongodb

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
