from random import randint

class Board:
    def __init__(self):
        self.board = [
            [
                (randint(1,10), randint(1,10)),
                (randint(1,10), randint(1,10))
            ],
            [
                (randint(1,10), randint(1,10)),
                (randint(1,10), randint(1,10))
            ],
        ]

    def play(self, a: int, b: int) -> tuple[int, int]:
        if a < 0 or a > 1 or b < 0 or b > 1:
            raise ValueError("a and b must be between 0 and 1.")
        
        return self.board[a][b]
    
    def __repr__(self):
        return f"Board:\n"+"\n".join([f"  {i}" for i in self.board])

