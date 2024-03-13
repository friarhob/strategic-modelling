from .player import Player

class B100Player(Player):
    def run(self, last_opponent_move, is_first_player):
        # Always play the second column
        return 1