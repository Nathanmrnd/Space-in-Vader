import pygame
from .starship import Starship
from .invader import Invader
from .laser import Laser

class Board:
    def __init__(self, w: int, h: int) -> None:
        # Initialize the Board with screen dimensions
        self._w = w
        self._h = h
        self._screen = pygame.display.set_mode((w, h))
        pygame.font.init()  # Initialize the font module fot pygame

    def draw(self, invaders: list[Invader], lasers: list[Laser], starship: Starship) -> None:
        # Clear the screen
        self._screen.fill((0, 0, 0))

        # Draw invaders, lasers, and starship
        for invader in invaders:
            invader.draw_invader(self._screen, self._w)
        for laser in lasers:
            laser.draw_laser(self._screen, self._w)
        starship.draw_starship(self._screen, self._w)

    def draw_text(self, text: str, position: tuple, size: int, color: tuple) -> None:
        # Create a font object needed to write on the creen
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)

        # Get the rectangle of the text and set its center to the specified position
        text_rect = text_surface.get_rect(center=position)
        
        # Draw the text on the screen
        self._screen.blit(text_surface, text_rect)
