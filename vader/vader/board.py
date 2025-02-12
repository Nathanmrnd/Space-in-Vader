import logging
import pygame

from .invader import Invader
from .laser import Laser
from .starship import Starship

logging.basicConfig(level=logging.info, format='%(asctime)s - %(levelname)s - %(message)s')

class Board:
    def __init__(self, w: int, h: int) -> None:
        logging.info("Initializing Board object.")
        self._w = w
        self._h = h
        self._screen = pygame.display.set_mode((w, h))
        pygame.font.init()

    def draw(self, invaders: list[Invader], lasers: list[Laser], starship: Starship) -> None:
        logging.info("Drawing game objects on the screen.")
        self._screen.fill((0, 0, 0))

        for invader in invaders:
            invader.draw_invader(self._screen, self._w)
        for laser in lasers:
            laser.draw_laser(self._screen, self._w)
        starship.draw_starship(self._screen, self._w)

    def draw_text(self, text: str, position: tuple, size: int, color: tuple) -> None:
        logging.info("Drawing text on the screen.")
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self._screen.blit(text_surface, text_rect)
