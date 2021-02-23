import csv
import os
import unittest
from collections import defaultdict

from futcheap.lib.schemes import TITLE2SCHEMA
from futcheap.lib.squad import Squad
import futcheap.utils.utils as utils
from futcheap.data.csv2futcheap import load_csv

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class TestChemistry(unittest.TestCase):
    def test_1(self):
        """https://www.futbin.com/21/squad/100172665/sbc"""
        content = load_csv(os.path.join(THIS_DIR, "test_data/chemistry_1.csv"))
        canon_chemistries = [3, 5, 6, 1, 9, 6, 9, 10, 9, 10, 2]
        schema = TITLE2SCHEMA["4_4_2_2"]
        players = content[0]
        squad = Squad(schema, players)
        team_chemistry, individual_chemistries = squad.get_chemistry(detailed=True)
        self.assertEqual(team_chemistry, 70)
        self.assertEqual(canon_chemistries, individual_chemistries)

    def test_2(self):
        """https://www.futbin.com/21/squad/100173014/sbc"""
        canon_chemistries = [9, 9, 9, 9, 9, 3, 2, 6, 8, 6, 3]
        content = load_csv(os.path.join(THIS_DIR, "test_data/chemistry_2.csv"))
        schema = TITLE2SCHEMA["4_4_2_2"]
        players = content[0]
        squad = Squad(schema, players)
        team_chemistry, individual_chemistries = squad.get_chemistry(detailed=True)
        self.assertEqual(team_chemistry, 73)
        self.assertEqual(canon_chemistries, individual_chemistries)


if __name__ == '__main__':
    unittest.main()
