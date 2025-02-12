from .board import Board
from .invader import Invader
from .game import Game
from .starship import Starship
from .laser import Laser  # Import Laser class for type hinting

import pygame
import argparse

# Default screen dimensions
W_DEFAULT = 300
H_DEFAULT = 500
MIN_SIZE = 100

def argue() -> argparse.Namespace:
    # Let the user choose the size of the game screen
    parser = argparse.ArgumentParser(description='Choose the width and height of the game window.')
    parser.add_argument('-L', type=int, help="Width", default=W_DEFAULT)
    parser.add_argument('-l', type=int, help="Height", default=H_DEFAULT)
    args = parser.parse_args()

    # Check argument
    if min(args.L, args.l) < MIN_SIZE:
        raise ValueError(f"The size must be greater or equal to {MIN_SIZE}.")

    return args

def main() -> None:
    # Parse command-line arguments
    args = argue()
    W_SCREEN = args.L
    H_SCREEN = args.l

    # Initialize Pygame
    pygame.init()
    starship = Starship(50, 140)
    lasers = []
    board = Board(W_SCREEN, H_SCREEN)
    invaders = [Invader(4 * i + 4, 4 * j) for i in range(20) for j in range(6)]
    game = Game(W_SCREEN, H_SCREEN, lasers, invaders, starship, board)
    game.run()
    pygame.quit()

