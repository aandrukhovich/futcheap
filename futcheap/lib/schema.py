from typing import List

class Schema:
    def __init__(self, title: str, positions: List[int], links: List[List[int]]):
        self.title = title
        self.positions = positions
        assert len(self.positions) == 11
        self.links = links
        assert len(self.links) == 11
