# -*- coding: utf-8 -*-

''' A base High Score Service Module
.. moduleauthor:: Luis Maria Pizarro <lmpizarro@gmail.com>

'''

from datetime import datetime, timedelta
from operator import attrgetter
from collections import namedtuple


class HighScoreService(object):
    '''
    Base Class for highScoreService
    '''
    def __init__(self):
        '''
        constructor
        '''
        self.table_all = [{'player_id': 0, 'score': 0}]
        self.table_last_hour = [{'player_id': 0, 'score': 0}]
        pass

    def add_score(self, player_id, score):
        '''
        Add score information
        '''
        pass

    def get_table(self):
        '''
        Returns:
            the historic table ordered by ranking.
        '''
        self.table_all = [{'player_id': 0, 'score': 0}]
        return self.table_all

    def get_last_hour_table(self):
        '''
        Returns:
            the last hour table ordered by ranking.
        '''
        self.table_last_hour = [{'player_id': 0, 'score': 0}]
        return self.table_last_hour

    def update(self):
        '''
        Update the state of the object
            Returns:
                historic table
                last hour table
        '''
        self.get_table()
        self.get_last_hour_table()
        return self.table_all, self.table_last_hour


    def __str__(self):
        '''
        Returns:
            string representation of highScoreService
        '''
        str_ = 'High Scores: \n'
        str_ = 'Historic Scores: \n'
        str_ += ''.join([('{}-{}\n').format(e['player_id'], e['score'])
                        for e in self.table_all])
        str_ += '---------\n'
        str_ += 'Last Hour Scores\n'
        str_ += ''.join([('{}-{}\n').format(e['player_id'], e['score'])
                        for e in self.table_last_hour])
        return str_


def main():
    '''
    main() in highScoreService
    '''
    hss = HighScoreService()

    hss.add_score(1, 100)
    hss.add_score(2, 300)
    hss.add_score(1, 250)

    table = hss.get_table()
    table = hss.get_last_hour_table()
    table_all, table_last_hour = hss.update()
    print(hss)

if __name__ == "__main__":
    '''
    To run highScore main() in its own module
    '''
    main()
