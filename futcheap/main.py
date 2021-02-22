from typing import List
import random

from lib.schemes import TITLE2SCHEMA
from lib.squad import Squad
from data.csv2futcheap import load_csv


def main():
    schema = TITLE2SCHEMA["4_4_2"]
    content = load_csv("data/csvs/data_100.csv")
    players = random.choices(content[0], k=11)
    squad = Squad(schema, players)
    print(squad.get_rating())
    for p in squad.players:
        print(p)

if __name__ == '__main__':
    main()
