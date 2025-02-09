import pygame

from .starship import Starship
from .invader import Invader
from .laser import Laser

class Board :
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((w, h))

    def draw(self,invaders : list[Invader],lasers : list[Laser],starship : Starship):
        self.screen = pygame.display.set_mode((self.w, self.h))
        for invader in invaders :
            invader.draw_invader(self.screen, self.w)
        for laser in lasers :
            laser.draw_laser(self.screen,self.w)
        starship.draw_starship(self.screen,self.w)

        