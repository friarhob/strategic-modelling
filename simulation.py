from board import Board
from players.a100 import A100Player
from players.b100 import B100Player
from players.beatlast import BeatLastPlayer
from players.generous import GenerousPlayer
from players.greedy import GreedyPlayer
from players.minimax import MinimaxPlayer
from players.random import RandomPlayer
from players.player import Player
from players.titfortat import TitForTatPlayer

N_GAMES = 1000
N_MOVES_PER_GAME = 100

PRINT_GAMES = False
PRINT_BOARD = False

def simulate_game(board: Board, player1: Player, player2: Player, rounds: int) -> dict:
    results = {
        player1.id: 0,
        player2.id: 0
    }

    last_moveA = None
    last_moveB = None
    
    for _ in range(rounds):
        moveA = player1.run(last_moveB, True)
        moveB = player2.run(last_moveA, False)
        result = board.play(moveA, moveB)

        last_moveA = moveA
        last_moveB = moveB
        
        results[player1.id] += result[0]
        results[player2.id] += result[1]
    
    return results

PLAYER_CONFIGS = [
    ("A100", A100Player),
    ("B100", B100Player),
    ("Random", RandomPlayer),
    ("Greedy", GreedyPlayer),
    ("Generous", GenerousPlayer),
    ("MiniMax", MinimaxPlayer),
    ("TitForTat", TitForTatPlayer),
    ("BeatLast", BeatLastPlayer),
]

if __name__ == "__main__":
    final_results = {}

    for _ in range(N_GAMES):
        board = Board()

        if PRINT_BOARD:
            print(board)

        for index1, (player_id1, player_class1) in enumerate(PLAYER_CONFIGS):
            for index2, (player_id2, player_class2) in enumerate(PLAYER_CONFIGS):
                if index1 != index2:
                    player1 = player_class1(player_id1, board)
                    player2 = player_class2(player_id2, board)
                    results = simulate_game(board, player1, player2, N_MOVES_PER_GAME)

                    if PRINT_GAMES:
                        print(f"{player_id1} ({results[player_id1]}) vs ({results[player_id2]}) {player_id2}")

                    for player in results:
                        if player not in final_results:
                            final_results[player] = 0
                        final_results[player] += results[player]

        if PRINT_GAMES or PRINT_BOARD:
            print("")

    final_output = sorted([(result, player) for player, result in final_results.items()], reverse=True)
    for (result, player) in final_output:
        print(f"{player} scored {result} points.")