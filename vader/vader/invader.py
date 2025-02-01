import pygame

class Invader:
    def __init__(self, column : int, line : int):
        self.column = column
        self.line = line

    def draw_invader(self, screen, w, h):
        loc_x = self.column * w/100 + w/10
        loc_y = self.line * w/100 + w/10
        rect = pygame.Rect(loc_x, loc_y, w/50, w/50)
        pygame.draw.rect(screen, (0,255,0), rect)