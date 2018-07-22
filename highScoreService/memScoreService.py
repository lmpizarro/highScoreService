# -*- coding: utf-8 -*-

''' A memory High Score Service Module
.. moduleauthor:: Luis Maria Pizarro <lmpizarro@gmail.com>

'''

from datetime import datetime, timedelta
from operator import attrgetter
from collections import namedtuple
from highScoreService import HighScoreService


class MemScoreService(HighScoreService):
    '''
    Implements in memory HighScoreService
    '''
    def __init__(self):
        '''
        constructor
        '''
        # creates an empty DB as a dictionary
        # the player_id will be the key
        self.db = {}
        # defines a Score named tuple 
        self.Score = namedtuple('Score', 'score time')

    def add_score(self, player_id, score):
        '''Add score information for MemScoreService
        to db in a list for each player_id.
        If the player_id isn't in db, creates a list
        for a new player_id key

            Args:
              player_id (int):  the id for the player
              score: (int): the score for the player
        '''
        d = self.Score(score=score, time=datetime.now())
        if str(player_id) not in self.db:
            self.db[str(player_id)] = []
        self.db[str(player_id)].append(d)

    def __group_reduce(self, db):
        '''
        Group by player_id and reduce scores in MemScoreService
        Args:
            db: a score db to group by player_id and reduce by player_id
        Returns:
            An ordered list of ScoreCard
        '''
        ScoreCard = namedtuple('ScoreCard', 'player_id score')
        Ranking = []
        for p_id in db:
            if len(db[p_id]) > 0:
                s = reduce(lambda x, y: x + y, [e.score for e in db[p_id]])
                Ranking.append(ScoreCard(player_id=int(p_id), score=s))
        return sorted(Ranking, key=attrgetter('score'), reverse=True)

    def __list_tupple_to_list_dict(self, lt):
        '''
        Convert a list of named tupples to dictionaries
        Args:
            An ordered list of ScoreCard
        Returns:
            An ordered list of dictionaries
        '''
        l_dict_r = [{'player_id': r.player_id, 'score': r.score} for r in lt]
        return l_dict_r


    def get_table(self):
        '''
        Returns:
            the historic table ordered by ranking.
        '''
        reduc = self.__group_reduce(self.db)
        self.table_all = self.__list_tupple_to_list_dict(reduc)
        return self.table_all

    def get_last_hour_table(self):
        '''
        A time filter for records older than an hour is
        applied

        Returns:
             the last hour table ordered by ranking.
        '''
        h = self.get_table()
        t = datetime.now()
        d = timedelta(hours=1)
        tm = t - d

        db_time_filtered = {}
        for k in self.db:
            db_time_filtered[k] = [s for s in self.db[k] if s.time > tm]

        reduc = self.__group_reduce(db_time_filtered)

        self.table_last_hour = self.__list_tupple_to_list_dict(reduc)
        return self.table_last_hour


def genOlder():
    '''Generates the precondition for the tests

       Returns:
           An initializade memScoreService for the tests
    '''
    tinit = datetime.now()

    Score = namedtuple('Score', 'score time')

    hss = MemScoreService()
    hss.db['1'] = []
    hss.db['2'] = []

    d = timedelta(hours=3)
    tm = tinit - d

    d = Score(score=100, time=tm)
    hss.db['1'].append(d)
    d = Score(score=300, time=tm)
    hss.db['2'].append(d)
    hss.db['2'].append(d)

    d = timedelta(hours=.5)
    tm = tinit - d
    d = Score(score=300, time=tm)
    hss.db['2'].append(d)
    hss.db['1'].append(d)
    d = Score(score=100, time=tm)
    hss.db['1'].append(d)

    tend = datetime.now()

    print ('Memory Elapsed Time: {}').format(tend - tinit)

    return hss


def main():
    '''
    main() in memScoreService
    '''
    hss = genOlder()  # MemScoreService()

    # hss.add_score(1,100)
    # hss.add_score(2,300)
    # hss.add_score(1,250)

    table_all = hss.get_table()
    table_last_hour = hss.get_last_hour_table()
    table_all, table_last_hour = hss.update()
    print(hss)

if __name__ == "__main__":
    '''
    To run memScore main() in its own module
    '''
    main()
