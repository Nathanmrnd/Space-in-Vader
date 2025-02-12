import pytest
import pygame
from vader.starship import Starship

@pytest.fixture(scope="module")
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_draw_starship(setup_pygame):
    screen = pygame.display.set_mode((300, 500))
    starship = Starship(50, 140)
    starship.draw_starship(screen, 300)
    # Check if the draw method was called with the correct parameters
    assert True  # Placeholder for actual assertion

def test_blast():
    starship = Starship(50, 140)
    laser = starship.blast()
    assert laser is not None
    assert laser._direction == "UP"
