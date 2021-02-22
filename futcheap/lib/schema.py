from typing import List
class Schema:
    def __init__(self, title: str, positions: List[int], links: List[List[int]]):
        self.title = title
        self.positions = positions
        assert len(positions) == 11
        self.links = links
        assert len(links) == 11

    # title = str # 4-4-2
    # """ NUMERATION
    #         10  9
    #     8   7   6   5
    #     4   3   2   1
    #           0
    # """
    # positions = [
    #     0, # GK
    #     1, # RB
    #     2, # CB
    #     2, # CB
    #     3, # LB
    #     9, # RM
    #     7, # CM
    #     7, # CM
    #     10, # LM
    #     16, # ST
    #     16  # ST
    # ]
    # assert len(positions) == 11

    # links = [
    #     [2, 3], # GK -- to CB and CB
    #     [2, 5],
    #     [0, 1, 3, 6],
    #     [0, 2, 4, 7],
    #     [3, 8],
    #     [1, 6, 9],
    #     [2, 5, 7, 9],
    #     [3, 6, 8, 10],
    #     [4, 7, 10],
    #     [5, 6, 10],
    #     [7, 8, 9]
    # ]
    # assert len(links) == 11
