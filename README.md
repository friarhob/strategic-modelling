# Python Strategic Modelling

A Python env to simulate the "Prisoners' Dilemma" type of game from [Universal Paperclips game](https://www.decisionproblem.com/paperclips/index2.html)

## Description

This is a platform to put into test some random competitions between bots.

## Table of Contents

[Installation](#installation) | [Usage](#usage) | [Contributing](#contributing)

## Installation

This is intented to run locally, straight away from terminal. Just fork it to include your own bots.

## Usage

Add any new players on `players/` folder, inheriting from `player.Player` and implementing the `run` method. Feel free to store list of moves or any other attributes that help your strategy, as well as implementing any support methods.

After that, add a `(name, PlayerClass)` entry to `PLAYER_CONFIGS` in `simulation.py`. The simulation creates fresh player instances per matchup, so any state stored in your player resets between opponents.

## Players

### From [Universal Paperclips](https://www.decisionproblem.com/paperclips/index2.html)

- **A100** — Always plays 0.
- **B100** — Always plays 1.
- **Random** — Picks 0 or 1 at random each round.
- **Greedy** — Always picks the move containing the highest possible payoff for itself.
- **Generous** — Always picks the move containing the highest possible payoff for the opponent.
- **MiniMax** — Always picks the move containing the lowest possible payoff for the opponent.
- **TitForTat** — Copies the opponent's last move. Plays randomly on the first round.
- **BeatLast** — Picks the best response assuming the opponent will repeat their last move. Plays randomly on the first round.

### Custom

- **Bayesian** — Tracks opponent move frequencies conditioned on its own previous move, then picks the move with the highest expected payoff. Falls back to a greedy strategy until enough history is available.

## License

This project is licensed under the [MIT License](LICENSE).