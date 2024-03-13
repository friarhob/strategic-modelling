from .player import Player
from random import randint

class TitForTatPlayer(Player):
    def run(self, last_opponent_move, is_first_player):
        # Always play the strategy which the opponent played last time
        if last_opponent_move is None:
            return randint(0, 1)
        return last_opponent_move