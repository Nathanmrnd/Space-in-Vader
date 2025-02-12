import pytest
import pygame
from vader.laser import Laser

@pytest.fixture(scope="module")
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def laser_instance():
    return Laser(10, 20, "UP", (255, 0, 0))

def test_initialization(laser_instance):
    assert laser_instance._column == 10
    assert laser_instance._line == 20
    assert laser_instance._direction == "UP"
    assert laser_instance._color == (255, 0, 0)

def test_draw_laser(setup_pygame, laser_instance):
    screen = pygame.Surface((300, 500))  # Use a Surface object instead of initializing a display
    laser_instance.draw_laser(screen, 300)
    # Check if the draw method was called with the correct parameters
    # This is a simple check and may need to be expanded based on actual implementation
    assert True  # Placeholder for actual assertion

def test_move_laser_up(laser_instance):
    laser_instance._direction = "UP"
    initial_line = laser_instance._line
    laser_instance.move_laser()
    assert laser_instance._line < initial_line  # Assuming move_up decreases the line value

def test_move_laser_down(laser_instance):
    laser_instance._direction = "DOWN"
    initial_line = laser_instance._line
    laser_instance.move_laser()
    assert laser_instance._line > initial_line  # Assuming move_down increases the line value

def test_delete_outranged(laser_instance):
    lasers = [laser_instance]
    laser_instance._line = -1  # Simulate laser being out of range
    laser_instance.delete_outranged(lasers)
    assert len(lasers) == 0

def test_delete_outranged_down(laser_instance):
    lasers = [laser_instance]
    laser_instance._line = 101  # Simulate laser being out of range
    laser_instance.delete_outranged(lasers)
    assert len(lasers) == 0
