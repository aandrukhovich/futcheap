import futcheap.utils.utils as utils
from futcheap.lib.schema import Schema


def create_4_4_2():
    """
         ST - ST
       /  |   |  \
    LM - CM - CM - RM
    |     |   |     |
    LB - CB - CB - RB
          \   /
            GK
    """
    positions = [
        "GK", # 0
        "RB", # 1
        "CB", # 2
        "CB", # 3
        "LB", # 4
        "RM", # 5
        "CM", # 6
        "CM", # 7
        "LM", # 8
        "ST", # 9
        "ST", # 10
    ]

    return Schema(
        title="4-4-2",
        positions = [utils.position2num[pos] for pos in positions],
        links = [
            [2, 3], # GK -- to CB and CB
            [2, 5],
            [0, 1, 3, 6],
            [0, 2, 4, 7],
            [3, 8],
            [1, 6, 9],
            [2, 5, 7, 9],
            [3, 6, 8, 10],
            [4, 7, 10],
            [5, 6, 10],
            [7, 8, 9]
        ]
    )


TITLE2SCHEMA = {
    "4_4_2": create_4_4_2()
}
