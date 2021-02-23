import unittest
from collections import defaultdict

import futcheap.utils.utils as utils
from futcheap.lib.player import Player

class PlayerPlaceholder(Player):
    def __init__(self, rating):
        row = defaultdict(str)
        row['rating'] = rating
        row['price'] = "1000"
        super().__init__(row)


class TestRating(unittest.TestCase):
    def test_81(self):
        """https://www.futbin.com/sbc-rating-combinations"""
        combinations = [
            [79, 80, 80, 80, 81, 81, 81, 81, 81, 81, 82],
            [80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81],
            [76, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81],
            [78, 79, 79, 79, 79, 80, 81, 82, 82, 82, 82],
            [77, 77, 77, 77, 78, 80, 82, 82, 82, 82, 84]
        ]
        for combination in combinations:
            players = [PlayerPlaceholder(rating) for rating in combination]
            self.assertEqual(utils.get_rating(players), 81)


    def test_from_source_example(self):
        """https://www.reddit.com/r/FIFA/comments/5osq7k/new_overall_rating_figured_out/"""
        combinations = [
            [83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 84],
            [83, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84],
            [82, 82, 82, 82, 82, 84, 84, 84, 84, 84, 87]
        ]
        players = [PlayerPlaceholder(rating) for rating in combinations[0]]
        self.assertEqual(utils.get_rating(players), 83)
        players = [PlayerPlaceholder(rating) for rating in combinations[1]]
        self.assertEqual(utils.get_rating(players), 84)
        players = [PlayerPlaceholder(rating) for rating in combinations[2]]
        self.assertEqual(utils.get_rating(players), 84)



if __name__ == '__main__':
    unittest.main()
