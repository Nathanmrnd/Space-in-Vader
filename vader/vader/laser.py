from .gameobject import GameObject
import pygame

class Laser(GameObject):
    def __init__(self,column,line,direction,color):
        super().__init__(column,line)
        self.direction = direction
        self.color = color

    def draw_laser(self,screen,w):
        loc_x = self.column * w/100
        loc_y = self.line * w/100 + w/10
        rect = pygame.Rect(loc_x, loc_y, 2, w/50)
        pygame.draw.rect(screen, self.color, rect)

    def move_laser(self):
        if self.direction == 'UP':
            self.move_up()
        if self.direction == 'DOWN':
            self.move_down()

    def delete_outranged(self,lasers):
        if self.is_on_the_up_edge() or self.is_on_the_down_edge():
            lasers.remove(self)


