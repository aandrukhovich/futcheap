from typing import Dict


class Player:
    def __init__(self, content: Dict):
        self.name = content['name'] # str, Critiano Ronaldo
        self.club = content['club']
        self.nation = content['nation']
        self.league = content['league']
        self.rating = content['rating']
        self.position = content['position']
        self.rating = content['rating']
        self.card_types = content['card_types']



