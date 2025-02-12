import logging
import pygame

from .gameobject import GameObject
from .laser import Laser

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Starship(GameObject):
    def __init__(self, column: int, line: int) -> None:
        logging.debug("Initializing Starship object.")
        super().__init__(column, line)

    def draw_starship(self, screen: pygame.Surface, w: int) -> None:
        logging.debug("Drawing starship on the screen.")
        loc_x = self._column * w / 100
        loc_y = self._line * w / 100 + w / 10

        rect = pygame.Rect(loc_x, loc_y, w / 50, w / 50)

        pygame.draw.rect(screen, (255, 0, 0), rect)

    def blast(self) -> Laser:
        logging.info("Starship is firing a laser.")
        return Laser(self._column, self._line, "UP", (255, 0, 0))
