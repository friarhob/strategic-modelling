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

After that, add a instance creating in `list_players` on `simulation.py`.

## Contributing

I just implemented the bots that exist in [Universal Paperclips game](https://www.decisionproblem.com/paperclips/index2.html). It would be nice to have some standardised strategies as bots by default. Feel free to pull request anything regarding that. I don't plan to put in the codebase customised bots, though.

Also, this was a 4-hour project, feel free to propose any refactors or improvements towards that.

## License

This project is licensed under the [MIT License](LICENSE).