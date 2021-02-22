from typing import Dict
from futcheap.utils import utils


class Player:
    def __init__(self, content: Dict):
        self.name = content['name'] # str, Critiano Ronaldo
        self.club = content['club']
        self.nation = content['nation']
        self.league = content['league']
        self.rating = content['rating']
        self.position = content['position']
        self.price = utils.convert_price_to_int(content['price'])
        self.card_types = content['card_types']


    def __str__(self):
        return f"name={self.name} rating={self.rating} price={self.price}"



