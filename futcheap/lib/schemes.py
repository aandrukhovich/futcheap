from futcheap.lib.schema import Schema



def create_4_4_2():
    return Schema(
        title="4-4-2",
        positions = [
            0, # GK
            1, # RB
            2, # CB
            2, # CB
            3, # LB
            9, # RM
            7, # CM
            7, # CM
            10, # LM
            16, # ST
            16  # ST
        ],
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
