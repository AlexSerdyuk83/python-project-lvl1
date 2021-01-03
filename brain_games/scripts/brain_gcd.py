#!/usr/bin/env python
from brain_games.scripts.brain_games import greet
from brain_games.games.gcd_games import get_gcd_games


def main():
    greet()
    get_gcd_games()


if __name__ == "__main__":
    main()
