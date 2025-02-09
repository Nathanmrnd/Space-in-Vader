from .gameobject import GameObject
from .laser import Laser
import pygame

class Starship(GameObject):
    def __init__(self, column : int, line : int):
        super().__init__(column,line)

    def draw_starship(self, screen, w):
        loc_x = self.column * w/100
        loc_y = self.line * w/100 + w/10
        rect = pygame.Rect(loc_x, loc_y, w/50, w/50)
        pygame.draw.rect(screen, (255,0,0), rect)

    def blast(self):
        return Laser(self.column,self.line,'UP',(255,0,0))  
