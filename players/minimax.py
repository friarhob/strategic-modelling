from .player import Player

class MinimaxPlayer(Player):
    def run(self, last_opponent_move, is_first_player):
        # Always play the strategy which does not contain the highest reward for the opponent

        opponent_index = 1 if is_first_player else 0

        best_reward = 0
        best_movement = 0

        for i in range(len(self.board.board)):
            line = self.board.board[i]
            for movement in line:
                if movement[opponent_index] > best_reward:
                    best_reward = movement[opponent_index]
                    best_movement = i

        return 1 - best_movement


