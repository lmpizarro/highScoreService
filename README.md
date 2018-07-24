# highScoreService

This modules solves the problem in two differents manners, in the ```class
MemScoreService``` the state of the score is mantained in memory, in the ```class
MongoScoreService``` such state is mantained in a mongoDb database.
Besides ```MemScoreService```, only uses the standard python library.

### 23/07/2018

Added ```observerPlayers.py ```, it simulates 2 players that insert scores in
a list, and an observer watch the list for older elements, if an elements gets
older, the observer, delete it. This version is incomplete, but it would be
possible to have, the most recent scores in memory and the oldest in a DB.
 

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
