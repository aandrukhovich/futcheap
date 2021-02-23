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


def get_fitness(squad):
    return 10 * max(0, 84 - squad.get_rating()) + 10 * max(0, 50 - squad.get_chemistry()) + squad.get_price() * 0.0000001


def genetic_algorithm():
    content = load_csv("data/csvs/data_100_wo_icons.csv")
    all_players = content[0]
    schema = TITLE2SCHEMA["4_4_2(2)"]


    squads = []
    for i in range(300):
        s = Squad(schema, random.choices(all_players, k=11))
        fitness = get_fitness(s)
        squads.append((s, fitness))
    iterations = -1

    try:
        while iterations < 1000:
            for i in range(100):
                for j in range(int((100 - i) / 10 + 1)):
                    squad = squads[i]
                    a = random.randint(0, 10)
                    b = random.randint(0, 10)
                    while a == b:
                        a = random.randint(0, 10)
                        b = random.randint(0, 10)
                    players = squad[0].players.copy()
                    players[a], players[b] = players[b], players[a]
                    new_squad = Squad(schema, players)
                    new_fitness = get_fitness(new_squad)
                    if new_fitness <= squads[i][1] + 30:
                        squads.append((new_squad, get_fitness(new_squad)))

            for i in range(100):
                for j in range(int((100 - i) / 10 + 1)):
                    squad = squads[i]
                    a = random.choice(all_players)
                    index = random.randint(0, 10)
                    players = squad[0].players.copy()
                    new_squad = Squad(schema, players)
                    new_fitness = get_fitness(new_squad)
                    if new_fitness <= squads[i][1] + 30:
                        squads.append((new_squad, get_fitness(new_squad)))

            squads.sort(key=lambda x: x[1])
            new_squads = []
            new_squads_fitnesses = set()
            for squad, fitness in squads:
                if fitness not in new_squads_fitnesses:
                    new_squads.append((squad, fitness))
                    new_squads_fitnesses.add(fitness)
            squads = new_squads
            squads = squads[:100]
            iterations += 1
            # print("########################")
            # for i in range(len(squads)):
            #     print(i, squads[i][0].get_rating(), squads[i][0].get_chemistry(), squads[i][0].get_price(), squads[i][1])
            if iterations % 100 == 0:
                print("########################")
                print(iterations)
                for i in range(10):
                    print(i, squads[i][0].get_rating(), squads[i][0].get_chemistry(), squads[i][0].get_price(), squads[i][1])
                # print(iterations, squads[0][0].get_rating(), squads[0][0].get_chemistry(), squads[0][0].get_price(), squads[0][1])
            #     print(iterations, squads[1][0].get_rating(), squads[1][0].get_chemistry(), squads[1][0].get_price(), squads[1][1])
            #     print(iterations, squads[49][0].get_rating(), squads[49][0].get_chemistry(), squads[49][0].get_price(), squads[49][1])
    except KeyboardInterrupt:
        best_squad = squads[0][0]
        for p in best_squad.players:
            print(p)



def main():
    genetic_algorithm()
    # schema = TITLE2SCHEMA["4_4_2"]
    # content = load_csv("data/csvs/test.csv")
    # players = random.choices(content[0], k=11)
    # players = content[0]


    # squad = Squad(schema, players)
    # print("rating:", squad.get_rating())
    # print("chemistry:", squad.get_chemistry())
    # for p in squad.players:
    #     print(p)
    # for i in range(11):
    #     print(squad.players[i].position, utils.num2position[schema.positions[i]])

if __name__ == '__main__':
    main()
