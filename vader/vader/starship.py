from .gameobject import GameObject
from .laser import Laser
import pygame

class Starship(GameObject):
    def __init__(self, column: int, line: int) -> None:
        # Initialize the Starship object using the parent class constructor
        super().__init__(column, line)

    def draw_starship(self, screen: pygame.Surface, w: int) -> None:
        # Calculate the position of the starship
        loc_x = self._column * w / 100
        loc_y = self._line * w / 100 + w / 10

        # Create a rectangle for the starship
        rect = pygame.Rect(loc_x, loc_y, w / 50, w / 50)

        # Draw the starship on the screen
        pygame.draw.rect(screen, (255, 0, 0), rect)

    def blast(self) -> Laser:
        # Create and return a new Laser object
        return Laser(self._column, self._line, 'UP', (255, 0, 0))
