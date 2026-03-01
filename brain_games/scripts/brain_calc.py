from brain_games.engine import run_game
from brain_games.games.calc import DESCRIPTION, generate_round


def main():
    run_game(generate_round, DESCRIPTION)


if __name__ == '__main__':
    main()