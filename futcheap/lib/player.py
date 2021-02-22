from typing import Dict

def convert_price_to_int(price: str) -> int:
    multiplier = 1
    if price.endswith('M'):
        multiplier = 1_000_000
        price = price[:-1]
    elif price.endswith('K'):
        multiplier = 1_000
        price = price[:-1]
    return int(float(price) * multiplier)

class Player:
    def __init__(self, content: Dict):
        self.name = content['name'] # str, Critiano Ronaldo
        self.club = content['club']
        self.nation = content['nation']
        self.league = content['league']
        self.rating = int(content['rating'])
        self.position = content['position']
        self.price = convert_price_to_int(content['price'])
        self.card_types = content['card_types']


    def __str__(self):
        return f"name={self.name} rating={self.rating} price={self.price}"
