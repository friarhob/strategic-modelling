from random import randint

from board import Board
from .player import Player


class PavlovPlayer(Player):
    def __init__(self, id: str, board: Board):
        super().__init__(id, board)
        self.last_move: int | None = None
        self.average_payoff: float = self._compute_average_payoff()

    def run(self, last_opponent_move: int, is_first_player: bool) -> int:
        if self.last_move is None or last_opponent_move is None:
            self.last_move = randint(0, 1)
            return self.last_move

        player_index = 0 if is_first_player else 1
        if is_first_player:
            last_payoff = self.board.board[self.last_move][last_opponent_move][player_index]
        else:
            last_payoff = self.board.board[last_opponent_move][self.last_move][player_index]

        if last_payoff >= self.average_payoff:
            return self.last_move

        self.last_move = 1 - self.last_move
        return self.last_move

    def _compute_average_payoff(self) -> float:
        total = 0
        for row in self.board.board:
            for cell in row:
                total += cell[0]  # board is symmetric, so cell[0] and cell[1] average the same
        return total / 4
