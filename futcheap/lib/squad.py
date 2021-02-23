from typing import List

from futcheap.lib.schema import Schema
from futcheap.lib.player import Player
import futcheap.utils.utils as utils

POS2POS_POINTS = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 3, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 3, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 3, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 3, 1, 2, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 3, 0, 2, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 3, 1, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 3, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 1, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 3, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 3, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 3]
]

def get_link_int(player_a, player_b):
    return sum((
        int(player_a.nation == player_b.nation),
        int(player_a.league == player_b.league),
        int(player_a.club == player_b.club)
    ))


class Squad:
    def __init__(self, schema: Schema, players: List[Player]):
        self.schema = schema
        self.players = players

    def get_rating(self):
        return utils.get_rating(self.players)

    def get_chemistry(self, detailed=False):
        """
        https://www.reddit.com/r/FIFA/comments/k05te9/need_the_exact_formula_for_individual_player/
        https://www.gfinityesports.com/article/6727/fifa-21-ultimate-team-chemistry-guide-team-player-loyalty-chemistry-explained
        """
        individual_chemistries = []
        for i in range(11):
            player = self.players[i]
            position_by_schema = utils.num2position[self.schema.positions[i]]

            position_points = POS2POS_POINTS[utils.position2num[player.position]][self.schema.positions[i]]
            position_multiplier = min(3, position_points + 1)

            link_values = []
            for link in self.schema.links[i]:
                linked_player = self.players[link]
                link_values.append(get_link_int(player, linked_player))
            sum_links = sum(link_values)
            len_links = len(link_values)
            link_points = int(sum_links >= len_links * 1 / 3) + int(sum_links >= len_links * 3 / 3)
            overlinked_bonus = int(sum_links >= len_links * 5 / 3) * int(position_multiplier == 3)

            final = min(10, position_points + (position_multiplier * link_points) + overlinked_bonus)
            individual_chemistries.append(final)
            print(player.name, final)
        team_chemistry = min(100, sum(individual_chemistries))
        if detailed:
            return team_chemistry, individual_chemistries
        else:
            return team_chemistry

