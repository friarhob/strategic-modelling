from .player import Player
from random import randint

class RandomPlayer(Player):
    def run(self, last_opponent_move, is_first_player) -> int:
        # Randomly select a column to play
        return randint(0, 1)