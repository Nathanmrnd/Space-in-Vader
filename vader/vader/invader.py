import pygame


from .gameobject import GameObject
from .laser import Laser

class Invader(GameObject):
    shared_state = 'RIGHT'

    @classmethod
    def check_and_update_state(cls, invaders):

        for invader in invaders:
            if invader.is_on_the_right_edge() and cls.shared_state == 'RIGHT':
                cls.shared_state = 'LEFT'
                for vader in invaders:
                    vader.move_down()
                break
            elif invader.is_on_the_left_edge() and cls.shared_state == 'LEFT':
                cls.shared_state = 'RIGHT'
                for vader in invaders:
                    vader.move_down()
                break

    def __init__(self, column : int, line : int):
        super().__init__(column,line)


    def draw_invader(self, screen, w):
        loc_x = self.column * w/100
        loc_y = self.line * w/100 + w/10
        rect = pygame.Rect(loc_x, loc_y, w/50, w/50)
        pygame.draw.rect(screen, (0,255,0), rect)

    def move_invader(self):
        if Invader.shared_state == 'RIGHT':
            self.move_right()
        else:
            self.move_left()

    def blast(self):
        return Laser(self.column,self.line,'DOWN',(0,255,0))
    
    
