from .player import Player

class GreedyPlayer(Player):
    def run(self, last_opponent_move, is_first_player):
        # Always play the strategy containing the highest reward

        player_index = 0 if is_first_player else 1

        best_reward = 0
        best_movement = 0

        for i in range(len(self.board.board)):
            line = self.board.board[i]
            for movement in line:
                if movement[player_index] > best_reward:
                    best_reward = movement[player_index]
                    best_movement = i

        return best_movement


