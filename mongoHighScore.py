''' A mongo High Score Service Module
.. moduleauthor:: Luis Maria Pizarro <lmpizarro@gmail.com>

'''

import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta
from highScoreService import HighScoreService


class MongoHighScore(HighScoreService):
    '''
    Implements in mongo HighScoreService
    '''
    def __init__(self, clear=False):
        '''
        constructor
        '''
        self.client = MongoClient('localhost', 27017)

        self.db = self.client['Score_DB']
        self.table = self.db['score']
        self.reduce = self.db['reduce']

        if clear:
            self.table.drop()

    def add_score(self, player_id, score):
        '''
        # Add score information for mongoScoreService
        '''
        t_t = datetime.now()
        self.table.insert_one(
            {'player_id': player_id, 'score': score, 'time_tag': t_t})

    def __group_reduce(self, q):
        '''
        Group by player_id and reduce scores in mongoScoreService
        '''
        # clean auxiliary collection
        self.reduce.drop()

        # find distinct player_id
        p_id = self.table.find().distinct('player_id')
        # for each player find all scores that satisfy q
        for pi in p_id:
            score_pi = self.table.find({'player_id': pi, 'time_tag': q})

            sum_ = 0
            # for each scores of each player SUM score
            sum_ = 0
            if score_pi.count() > 0:
                sum_ = reduce(
                    lambda x, y: x + y, [e['score'] for e in score_pi])

            # append to score reduce card
            self.reduce.insert_one({'player_id': pi, 'score': sum_})
        # return ordered list
        res = self.reduce.find().sort('score', pymongo.DESCENDING)
        return res

    def get_table(self):
        '''
        Returns the historic table ordered by ranking.
        '''
        q = {'$lt': datetime.now()}
        self.table_all = self.__group_reduce(q)
        return self.table_all

    def get_last_hour_table(self):
        '''
        Returns the last hour table ordered by ranking.
        '''
        t = datetime.now()
        d = timedelta(hours=1)
        tm = (t - d)
        q = {'$gt': tm}
        self.table_last_hour = self.__group_reduce(q)
        return self.table_last_hour


def genOlder():
    '''
     Generates the precondition for the tests
    '''
    tinit = datetime.now()
    d = timedelta(hours=3)
    tm = (tinit - d)

    hss = MongoHighScore(clear=True)

    hss.table.insert_one({'player_id': 2, 'score': 300, 'time_tag': tm})
    hss.table.insert_one({'player_id': 2, 'score': 300, 'time_tag': tm})
    hss.table.insert_one({'player_id': 1, 'score': 100, 'time_tag': tm})

    d = timedelta(hours=.5)
    tm = (tinit - d)

    hss.table.insert_one({'player_id': 2, 'score': 300, 'time_tag': tm})
    hss.table.insert_one({'player_id': 1, 'score': 300, 'time_tag': tm})
    hss.table.insert_one({'player_id': 1, 'score': 100, 'time_tag': tm})

    tend = datetime.now()

    print ('Mongo Elapsed Time: {}').format(tend - tinit)

    return hss


def main():
    '''
    main() in mongoScoreService
    '''
    hss = genOlder()  # MongoHighScore()

    # hss.add_score(1,100)
    # hss.add_score(2,300)
    # hss.add_score(1,250)

    table_all = hss.get_table()
    table_last_hour = hss.get_last_hour_table()
    table_all, table_last_hour = hss.update()
    print(hss)


if __name__ == "__main__":
    '''
    To run mongoScore main() in its own module
    '''
    main()
