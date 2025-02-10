from .board import Board
from .invader import Invader
from .game import Game

from .starship import Starship

import pygame



W_SCREEN = 300
H_SCREEN = 500








def main():
    pygame.init()
    starship=Starship(50,140)
    lasers=[]
    board = Board(W_SCREEN,H_SCREEN)
    invaders = [Invader(4*i+4,4*j) for i in range(20) for j in range(6)]
    game = Game(W_SCREEN,H_SCREEN,lasers,invaders,starship,board)
    game.run()
    pygame.quit
