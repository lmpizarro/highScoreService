from datetime import datetime, timedelta
from operator import attrgetter
from collections import namedtuple


class HighScoreService(object):

    def __init__(self):
        # constructor 
        pass

    def add_score(self, player_id, score):
        # Add score information
        pass

    def get_table(self):
        # Returns the table ordered by ranking.
        pass

    def get_last_hour_table(self):
        # Returns the table ordered by ranking.
        pass

    def tableToStr(self, table):
      str_=''
      for e in table:
         str_ += ('{}-{}\n').format(e['player_id'], e['score'])
      return str_


def main():
    hss = HighScoreService()
   
    hss.add_score(1,100)
    hss.add_score(2,300)
    hss.add_score(1,250)

    table = hss.get_table()
    #print hss.tableToStr(table)
    table = hss.get_last_hour_table()
    #print hss.tableToStr(table)

if __name__=="__main__":
    main()
