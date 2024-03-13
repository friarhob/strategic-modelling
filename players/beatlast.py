from random import randint
from .player import Player

class BeatLastPlayer(Player):
    def run(self, last_opponent_move, is_first_player) -> int:
        # Always play the strategy which beats the opponent's last move
        if last_opponent_move is None:
            return randint(0, 1)

        best_move = 0
        best_result = -1

        for my_move in range(2):
            i = my_move if is_first_player else last_opponent_move
            j = last_opponent_move if is_first_player else my_move

            if(self.board.board[i][j][0 if is_first_player else 1] > best_result):
                best_result = self.board.board[i][j][0 if is_first_player else 1]
                best_move = my_move
        
        return best_move