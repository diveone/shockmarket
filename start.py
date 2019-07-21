from argparse import ArgumentParser, ArgumentError, ArgumentTypeError


def find_account():
    path = '~/Documents/Shockmarket/game_data/main.xml'
    # Parse XML looking for a tag named Player
    # if Player found, skip configuration and load them
    # else, create a new Player


class GameConfiguration:
    def __init__(self, **options):
        parser = ArgumentParser()
        parser.add_argument('bar', nargs='+', help='bar help')
        parser.add_argument('bar', nargs='+', help='bar help')
        find_account()

    def initial_setup(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    config = GameConfiguration()
    config.run()
