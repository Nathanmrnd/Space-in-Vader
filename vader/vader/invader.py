import logging
import pygame

from .gameobject import GameObject
from .laser import Laser

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Invader(GameObject):
    _shared_state = "RIGHT"

    @classmethod
    def check_and_update_state(cls, invaders: list) -> None:
        logging.debug("Checking and updating invader state.")
        for invader in invaders:
            if invader.is_on_the_right_edge() and cls._shared_state == "RIGHT":
                logging.info("Invader hit the right edge, changing direction to LEFT.")
                cls._shared_state = "LEFT"
                for vader in invaders:
                    vader.move_down()
                    vader.move_down()
                    vader.move_down()
                    vader.move_down()
                break
            if invader.is_on_the_left_edge() and cls._shared_state == "LEFT":
                logging.info("Invader hit the left edge, changing direction to RIGHT.")
                cls._shared_state = "RIGHT"
                for vader in invaders:
                    vader.move_down()
                    vader.move_down()
                    vader.move_down()
                    vader.move_down()
                break

    def __init__(self, column: int, line: int) -> None:
        logging.debug("Initializing Invader object.")
        super().__init__(column, line)

    def draw_invader(self, screen: pygame.Surface, w: int) -> None:
        logging.info("Drawing invader on the screen.")
        loc_x = self._column * w / 100
        loc_y = self._line * w / 100 + w / 10
        rect = pygame.Rect(loc_x, loc_y, w / 50, w / 50)
        pygame.draw.rect(screen, (0, 255, 0), rect)

    def move_invader(self) -> None:
        logging.info("Moving invader.")
        if Invader._shared_state == "RIGHT":
            self.move_right()
        else:
            self.move_left()

    def blast(self) -> Laser:
        logging.info("Invader is firing a laser.")
        return Laser(self._column, self._line, "DOWN", (0, 255, 0))
