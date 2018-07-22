from datetime import datetime, timedelta
from operator import attrgetter
from collections import namedtuple
from  highScoreService import HighScoreService


class MemScoreService(HighScoreService):

    def __init__(self):
        # create DB
        self.db={}
        self.Score= namedtuple('Score','score time')

    def add_score(self, player_id, score):
        # Add score information
        d = self.Score(score=score, time=datetime.now())
        if str(player_id) not in self.db:
            self.db[str(player_id)] = []
        self.db[str(player_id)].append(d)

    def __group_reduce(self, db):
        ScoreCard = namedtuple('ScoreCard', 'player_id score') 
        Ranking=[]
        for p_id in db:
          if len(db[p_id])>0:
            s = reduce(lambda x,y: x+y, [e.score for e in db[p_id]])
            Ranking.append(ScoreCard(player_id=int(p_id), score=s)) 
        return sorted(Ranking, key=attrgetter('score'), reverse=True)

    def __list_tupple_to_list_dict(self, lt):
        l_dict_r = [{'player_id':r.player_id, 'score':r.score} for r in lt]
        return l_dict_r

    def get_table(self):
        # Returns the table ordered by ranking.
        reduc = self.__group_reduce(self.db)
        return self.__list_tupple_to_list_dict(reduc) 


    def get_last_hour_table(self):
        # Returns the table ordered by ranking.
        h = self.get_table()
        t = datetime.now()
        d = timedelta(hours=1)
        tm = t - d

        db_time_filtered  = {}
        for k in self.db:
            db_time_filtered[k] = [s for s in self.db[k] if s.time > tm]

        reduc = self.__group_reduce(db_time_filtered)

        return self.__list_tupple_to_list_dict(reduc) 

def genOlder():
    Score= namedtuple('Score','score time')
    
    hss = MemScoreService()
    hss.db['1'] = [] 
    hss.db['2'] = []

    
    t = datetime.now()
    d = timedelta(hours=3)
    tm = t - d


    d = Score(score=100, time=tm)
    hss.db['1'].append(d) 
    d = Score(score=300, time=tm)
    hss.db['2'].append(d) 
    hss.db['2'].append(d) 

    d = timedelta(hours=.5)
    tm = t - d
    d = Score(score=300, time=tm)
    hss.db['2'].append(d) 
    hss.db['1'].append(d) 
    d = Score(score=100, time=tm)
    hss.db['1'].append(d) 

    return hss 

def main():
    hss = genOlder() # MemScoreService()
   
    #hss.add_score(1,100)
    #hss.add_score(2,300)
    #hss.add_score(1,250)

    table = hss.get_table()
    print hss.tableToStr(table)
    table = hss.get_last_hour_table()
    print hss.tableToStr(table)

if __name__=="__main__":
    main()