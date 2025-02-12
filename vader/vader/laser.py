from .gameobject import GameObject
import pygame

class Laser(GameObject):
    def __init__(self, column: int, line: int, direction: str, color: tuple) -> None:
        # Initialize the Laser object using the parent class constructor
        super().__init__(column, line)

        # Set the direction and color of the laser
        self._direction = direction
        self._color = color

    def draw_laser(self, screen: pygame.Surface, w: int) -> None:
        # Calculate the position of the laser
        loc_x = self._column * w / 100
        loc_y = self._line * w / 100 + w / 10
        # Create a rectangle for the laser
        rect = pygame.Rect(loc_x, loc_y, 2, w / 50)
        # Draw the laser on the screen
        pygame.draw.rect(screen, self._color, rect)

    def move_laser(self) -> None:
        # Move the laser up or down based on its direction
        if self._direction == 'UP':
            self.move_up()
        elif self._direction == 'DOWN':
            self.move_down()

    def delete_outranged(self, lasers: list) -> None:
        # Remove the laser from the list if it is out of range
        if self.is_on_the_up_edge() or self.is_on_the_down_edge():
            lasers.remove(self)
