#!/usr/bin/env python

from brain_games.games import logics_brain_even
from brain_games.common_logic import get_engine_of_games


def main():
    get_engine_of_games(logics_brain_even)


if __name__ == "__main__":
    main()
