from abc import ABC, abstractmethod
from board import Board


class Player(ABC):
    def __init__(self, id: str, board: Board):
        self.id = id
        self.board = board
    
    @abstractmethod 
    def run(self, last_opponent_move: int, is_first_player: bool) -> int:
        raise NotImplementedError