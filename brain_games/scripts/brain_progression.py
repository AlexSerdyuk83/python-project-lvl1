#!/usr/bin/env python
from brain_games.scripts.brain_games import greet
from brain_games.games.progression_games import get_progression_games


def main():
    greet()
    get_progression_games()


if __name__ == "__main__":
    main()
