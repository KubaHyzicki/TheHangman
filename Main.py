import argparse
from Hangman import Hangman


parser = argparse.ArgumentParser(
    description='TheHangman:\n1-tryb standardowy\n2-tryb artystyczny'
)
parser.add_argument('mode',
                    nargs='?',
                    const=1,
                    type=int,
                    help='default: 1',
                    default=1)

hangman=Hangman(parser.parse_args().mode)