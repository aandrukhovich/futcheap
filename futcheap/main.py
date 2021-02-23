from typing import List
import random

from futcheap.lib.schemes import TITLE2SCHEMA
from futcheap.lib.squad import Squad
import futcheap.utils.utils as utils
from futcheap.data.csv2futcheap import load_csv



def find_players(names, players_db):
    output = []
    for player in players_db:
        if player.name in names:
            output.append(player)
    return output

def main():
    schema = TITLE2SCHEMA["4_4_2"]
    content = load_csv("data/csvs/test.csv")
    # players = random.choices(content[0], k=11)
    players = content[0]


    squad = Squad(schema, players)
    print("rating:", squad.get_rating())
    print("chemistry:", squad.get_chemistry())
    for p in squad.players:
        print(p)
    for i in range(11):
        print(squad.players[i].position, utils.num2position[schema.positions[i]])

if __name__ == '__main__':
    main()
