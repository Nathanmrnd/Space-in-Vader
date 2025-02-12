import pytest
import pygame
from vader.board import Board
from vader.invader import Invader
from vader.laser import Laser
from vader.starship import Starship

@pytest.fixture(scope="module")
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_draw(setup_pygame):
    board = Board(300, 500)
    invaders = [Invader(10, 20)]
    lasers = [Laser(50, 140, "UP", (255, 0, 0))]
    starship = Starship(50, 140)
    board.draw(invaders, lasers, starship)
    # Check if the draw method was called with the correct parameters
    assert True  # Placeholder for actual assertion

def test_draw_text(setup_pygame):
    board = Board(300, 500)
    board.draw_text("Test", (150, 250), 20, (255, 255, 255))
    # Check if the draw_text method was called with the correct parameters
    assert True  # Placeholder for actual assertion
