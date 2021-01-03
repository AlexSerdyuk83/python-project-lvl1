#!/usr/bin/env python
from brain_games.scripts.brain_games import greet
from brain_games.games.prime_games import get_prime_games


def main():
    greet()
    get_prime_games()


if __name__ == "__main__":
    main()
