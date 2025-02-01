from .board import Board
from .invader import Invader

import pygame
import time


def main():
    pygame.init()
    board = Board(300,500)
    invaders = [Invader(4*i,4*j) for i in range(21) for j in range(6)]
    board.draw(invaders)
    pygame.display.update()
    time.sleep(5)
    pygame.quit
