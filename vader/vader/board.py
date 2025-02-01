import pygame


from .invader import Invader


class Board :
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((w, h))

    def draw(self,invaders : list[Invader]):
        for invader in invaders :
            invader.draw_invader(self.screen, self.w, self.h)
        