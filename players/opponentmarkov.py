from board import Board
from .player import Player


class OpponentMarkovPlayer(Player):
    def __init__(self, id: str, board: Board):
        super().__init__(id, board)
        # counts[opp_prev_move][opp_next_move] tracks opponent move transitions
        self.counts: list[list[int]] = [[0, 0], [0, 0]]
        self.prev_opponent_move: int | None = None

    def run(self, last_opponent_move: int, is_first_player: bool) -> int:
        # Record: opponent transitioned from prev_opponent_move to last_opponent_move
        if last_opponent_move is not None and self.prev_opponent_move is not None:
            self.counts[self.prev_opponent_move][last_opponent_move] += 1

        probabilities = self._get_opponent_probabilities(last_opponent_move)
        self.prev_opponent_move = last_opponent_move

        if probabilities is None:
            return self._initial_move(is_first_player)

        return self._best_expected_move(is_first_player, probabilities)

    def _get_opponent_probabilities(self, last_opponent_move: int) -> tuple[float, float] | None:
        """Estimate P(opponent plays X next | opponent played last_opponent_move)."""
        if last_opponent_move is None:
            return None

        total = sum(self.counts[last_opponent_move])
        if total == 0:
            return None

        return (
            self.counts[last_opponent_move][0] / total,
            self.counts[last_opponent_move][1] / total,
        )

    def _best_expected_move(self, is_first_player: bool, probabilities: tuple[float, float]) -> int:
        """Pick the move that maximises expected payoff given opponent probabilities."""
        player_index = 0 if is_first_player else 1
        probability_opponent_0, probability_opponent_1 = probabilities

        best_move = 0
        best_expected_payoff = -1.0

        for move in range(2):
            if is_first_player:
                expected_payoff = (
                    probability_opponent_0 * self.board.board[move][0][player_index]
                    + probability_opponent_1 * self.board.board[move][1][player_index]
                )
            else:
                expected_payoff = (
                    probability_opponent_0 * self.board.board[0][move][player_index]
                    + probability_opponent_1 * self.board.board[1][move][player_index]
                )

            if expected_payoff > best_expected_payoff:
                best_expected_payoff = expected_payoff
                best_move = move

        return best_move

    def _initial_move(self, is_first_player: bool) -> int:
        """Fallback: pick the move containing the highest possible payoff."""
        player_index = 0 if is_first_player else 1

        best_move = 0
        best_reward = 0

        for i in range(len(self.board.board)):
            for cell in self.board.board[i]:
                if cell[player_index] > best_reward:
                    best_reward = cell[player_index]
                    best_move = i

        return best_move
