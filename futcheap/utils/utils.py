import math
from typing import List

from futcheap.lib.schema import Schema
from futcheap.lib.player import Player



POSITIONS_LIST = [
    "GK",  # 0
    "RB",  # 1
    "CB",  # 2
    "LB",  # 3
    "RWB", # 4
    "LWB", # 5
    "CDM", # 6
    "CM",  # 7
    "CAM", # 8
    "RM",  # 9
    "LM",  # 10
    "RW",  # 11
    "LW",  # 12
    "CF",  # 13
    "RF",  # 14
    "LF",  # 15
    "ST"   # 16
]

position2num = {POSITIONS_LIST[i]: i for i in range(len(POSITIONS_LIST))}
num2position = {v: k for k, v in position2num.items()}


Pos2MaxChemTable = [
    [10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 10, 5, 5, 9, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2],
    [2, 5, 10, 5, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 5, 5, 10, 2, 9, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2],
    [2, 9, 2, 2, 10, 5, 2, 2, 2, 5, 2, 5, 2, 2, 2, 2, 2],
    [2, 2, 2, 9, 5, 10, 2, 2, 2, 2, 5, 2, 5, 2, 2, 2, 2],
    [2, 2, 5, 2, 2, 2, 10, 9, 5, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 9, 10, 9, 5, 5, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 5, 9, 10, 2, 2, 2, 2, 9, 2, 2, 2],
    [2, 5, 2, 2, 5, 2, 2, 5, 2, 10, 5, 9, 2, 2, 5, 2, 2],
    [2, 2, 2, 5, 2, 5, 2, 5, 2, 5, 10, 2, 9, 2, 2, 5, 2],
    [2, 2, 2, 2, 5, 2, 2, 2, 2, 9, 2, 10, 5, 2, 9, 2, 2],
    [2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 9, 5, 10, 2, 2, 9, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 9, 2, 2, 2, 2, 10, 5, 5, 9],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 9, 2, 5, 10, 5, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 9, 5, 5, 10, 5],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 5, 5, 10]
]


def get_chemistry(schema: Schema, players: List[Player]) -> int:
    return 15


def get_rating(players: List[Player]) -> int:
    """ sources: https://fifauteam.com/fifa-19-squad-rating-guide/
    https://www.reddit.com/r/FIFA/comments/5osq7k/new_overall_rating_figured_out/"""
    summary_rating = sum(player.rating for player in players)
    overall_rating = summary_rating / len(players)
    correction_factor = sum(
        player.rating - overall_rating
        for player in players
        if player.rating > overall_rating
    )
    return math.floor((summary_rating + correction_factor) / len(players))
