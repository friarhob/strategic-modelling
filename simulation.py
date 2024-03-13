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

N_GAMES = 100
N_MOVES_PER_GAME = 100

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

if __name__ == "__main__":
    final_results = {}

    for _ in range(N_GAMES):
        board = Board()

        print(board)

        list_players = [
            A100Player("A100", board),
            B100Player("B100", board),
            RandomPlayer("Random", board),
            GreedyPlayer("Greedy", board),
            GenerousPlayer("Generous", board),
            MinimaxPlayer("MiniMax", board),
            TitForTatPlayer("TitForTat", board),
            BeatLastPlayer("BeatLast", board),
        ]

        for player1 in list_players:
            for player2 in list_players:
                if(player1 != player2):
                    results = simulate_game(board, player1, player2, N_MOVES_PER_GAME)

                    print(f"{player1.id} ({results[player1.id]}) vs ({results[player2.id]}) {player2.id}")

                    for player in results:
                        if player not in final_results:
                            final_results[player] = 0
                        final_results[player] += results[player]
        
        print("")

    final_output = sorted([(result, player) for player, result in final_results.items()], reverse=True)
    for (result, player) in final_output:
        print(f"{player} scored {result} points.")