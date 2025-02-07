from .board import Board
from .invader import Invader
from .laser import Laser

import pygame
import time
import random

W_SCREEN = 300
H_SCREEN = 500


def main():
    pygame.init()
    lasers=[]
    board = Board(W_SCREEN,H_SCREEN)
    invaders = [Invader(4*i+4,4*j) for i in range(20) for j in range(6)]
    while True :
        board.draw(invaders,lasers)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                return True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    return True
        time.sleep(0.5)
        Invader.check_and_update_state(invaders)
        for invader in invaders:
            invader.move_invader()
            if random.random()<0.002:
                lasers.append(invader.blast())
        for laser in lasers :
            laser.move_laser()
    pygame.quit
