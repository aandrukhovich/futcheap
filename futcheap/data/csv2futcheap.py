import csv
from futcheap.lib.player import Player


# fill list of clubs, nations, leagues and card types
def load_csv(csv_filepath: str):
    """ return list of Player"""
    clubs = set()
    nations = set()
    leagues = set()
    card_types = set()
    players = []
    with open(csv_filepath, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            players.append(Player(row))
            clubs.add(row['club'])
            nations.add(row['nation'])
            leagues.add(row['league'])
            for card_type in row['card_types'].split(' '):
                card_types.add(card_type)
    return players, clubs, nations, leagues, card_types


if __name__ == '__main__':
    players = load_csv('csvs/data_660.csv')
