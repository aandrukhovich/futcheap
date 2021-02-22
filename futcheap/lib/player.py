from typing import Dict


class Player:
    def __init__(self, content: Dict):
        self.name = content['name'] # str, Critiano Ronaldo
        self.club = content['club']
        self.nation = content['nation']
        self.league = content['league']
        self.rating = content['rating']
        self.position = content['position']
        self.price = content['price']
        self.card_types = content['card_types']


    def __str__(self):
        return f"name={self.name} rating={self.rating} price={self.price}"



