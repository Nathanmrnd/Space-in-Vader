import pygame
from .gameobject import GameObject
from .laser import Laser

class Invader(GameObject):
    # Shared state for all invaders
    _shared_state = 'RIGHT'

    @classmethod
    def check_and_update_state(cls, invaders: list) -> None:
        # Check if any invader is at the edge and update the shared state
        for invader in invaders:
            if invader.is_on_the_right_edge() and cls._shared_state == 'RIGHT':
                cls._shared_state = 'LEFT'
                for vader in invaders:
                    vader.move_down()
                    vader.move_down()
                break
            elif invader.is_on_the_left_edge() and cls._shared_state == 'LEFT':
                cls._shared_state = 'RIGHT'
                for vader in invaders:
                    vader.move_down()
                    vader.move_down()
                break

    def __init__(self, column: int, line: int) -> None:
        super().__init__(column, line)

    def draw_invader(self, screen: pygame.Surface, w: int) -> None:
        # Calculate the position of the invader
        loc_x = self._column * w / 100
        loc_y = self._line * w / 100 + w / 10
        # Create a rectangle for the invader
        rect = pygame.Rect(loc_x, loc_y, w / 50, w / 50)
        # Draw the invader on the screen
        pygame.draw.rect(screen, (0, 255, 0), rect)

    def move_invader(self) -> None:
        # Move the invader left or right based on the shared state
        if Invader._shared_state == 'RIGHT':
            self.move_right()
        else:
            self.move_left()

    def blast(self) -> Laser:
        # Create and return a new Laser object going down
        return Laser(self._column, self._line, 'DOWN', (0, 255, 0))
