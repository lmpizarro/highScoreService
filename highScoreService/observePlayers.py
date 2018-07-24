from multiprocessing import Process, Manager
from datetime import timedelta, datetime
from time import sleep
import random
import os

random.seed(123)
manager = Manager()
l_score = manager.list()

 
def player(player_id):
    """ Append to a list scores with time_tags
         
    """
    proc = os.getpid()
    while True:
      s = random.randint(1,10)
      sleep(s)
      d = {'score': 3, 'player_id': player_id, 'time_tag': datetime.now()}
      l_score.append(d)
      print('New Score -> len: {0} player_id {1}  sleep: {2}'.format(len(l_score),
          player_id, s))
      
def observer(antiq, sampling_time):
    """Observe if the score list have old scores
    
    """   
    while True:
       sleep(sampling_time)

       len_l = len(l_score)
       now_ = datetime.now()
       delta = timedelta(seconds=antiq)
       if len_l > 0:
         first_time = l_score[0]['time_tag']
         if first_time < now_ -delta:
            time_older = l_score[0]['time_tag']
            # before deleting the older score from the list,
            # it must be written to a database
            l_score.pop(0)
            print ('pop older score time: {0}'.format(time_older))
       print('Observer  -> len: {0} {1}'.format(len_l, now_))

if __name__ == '__main__':
    player_ids = [1,2]
    procs = []
 
    # creates player simulators
    for number in player_ids:
        proc = Process(target=player, args=(number,))
        procs.append(proc)
        proc.start()

    antiq = 10 # time to write in the DB - define the oldest score
    sampling_time = 2 # period time to observe the older element in the list
    proc = Process(target=observer, args=(antiq, sampling_time))
    procs.append(proc)
    proc.start()
 
    for proc in procs:
        proc.join()
