from .player import Player

class A100Player(Player):
    def run(self, last_opponent_move, is_first_player):
        # Always play the first column
        return 0