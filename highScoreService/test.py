''' A test module for High Score Service Modules
.. moduleauthor:: Luis Maria Pizarro <lmpizarro@gmail.com>

'''

import unittest
import mongoHighScore as mh
import memScoreService as hs

p_id_get_table = [2, 1]
sco_get_table = [900, 500]

p_id_get_last_hour_table = [1, 2]
sco_get_last_hour_table = [400, 300]


class Test_Score(unittest.TestCase):
    '''
    '''
    def test_get_table(self):
        '''
        '''
        hss = mh.genOlder()
        table = hss.get_table()
        for i, t in enumerate(table):
            self.assertEqual(p_id_get_table[i], t['player_id'])
            self.assertEqual(sco_get_table[i], t['score'])

    def test_get_last_hour_table(self):
        '''
        '''
        hss = mh.genOlder()
        table = hss.get_last_hour_table()
        for i, t in enumerate(table):
            self.assertEqual(p_id_get_last_hour_table[i], t['player_id'])
            self.assertEqual(sco_get_last_hour_table[i], t['score'])

    def test_get_table_(self):
        '''
        '''
        hss = hs.genOlder()
        table = hss.get_table()
        for i, t in enumerate(table):
            self.assertEqual(p_id_get_table[i], t['player_id'])
            self.assertEqual(sco_get_table[i], t['score'])

    def test_get_last_hour_table_(self):
        '''
        '''
        hss = hs.genOlder()
        table = hss.get_last_hour_table()
        for i, t in enumerate(table):
            self.assertEqual(p_id_get_last_hour_table[i], t['player_id'])
            self.assertEqual(sco_get_last_hour_table[i], t['score'])


if __name__ == "__main__":
    '''
    '''
    unittest.main()
