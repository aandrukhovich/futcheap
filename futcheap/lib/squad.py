from typing import List

from futcheap.lib.schema import Schema
from futcheap.lib.player import Player
import futcheap.utils.utils as utils


class Squad:
    def __init__(self, schema: Schema, players: List[Player]):
        self.schema = schema
        self.players = players

    def get_rating(self):
        return utils.get_rating(self.players)
