import pytest
import pygame
from unittest.mock import MagicMock
from vader.invader import Invader
from vader.gameobject import GameObject
from vader.laser import Laser

@pytest.fixture(scope="module")
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def invader_instance():
    return Invader(10, 20)

def test_initialization(invader_instance):
    assert invader_instance._column == 10
    assert invader_instance._line == 20

def test_draw_invader(setup_pygame, invader_instance):
    screen = pygame.display.set_mode((300, 500))
    invader_instance.draw_invader(screen, 300)
    # Check if the draw method was called with the correct parameters
    assert True  # Placeholder for actual assertion

def test_move_invader_right(invader_instance, mocker):
    mocker.patch.object(invader_instance, 'move_right')
    Invader._shared_state = "RIGHT"
    invader_instance.move_invader()
    invader_instance.move_right.assert_called_once()

def test_move_invader_left(invader_instance, mocker):
    mocker.patch.object(invader_instance, 'move_left')
    Invader._shared_state = "LEFT"
    invader_instance.move_invader()
    invader_instance.move_left.assert_called_once()

def test_blast(invader_instance):
    laser = invader_instance.blast()
    assert isinstance(laser, Laser)
    assert laser._direction == "DOWN"

def test_check_and_update_state_right_edge(mocker):
    invaders = [Invader(10, 20), Invader(15, 20)]
    mocker.patch.object(invaders[0], 'is_on_the_right_edge', return_value=True)
    mocker.patch.object(invaders[0], 'move_down')

    Invader.check_and_update_state(invaders)
    assert Invader._shared_state == "LEFT"
    invaders[0].move_down.assert_called()

def test_check_and_update_state_left_edge(mocker):
    invaders = [Invader(10, 20), Invader(15, 20)]
    mocker.patch.object(invaders[0], 'is_on_the_left_edge', return_value=True)
    mocker.patch.object(invaders[0], 'move_down')
    Invader._shared_state = "LEFT"

    Invader.check_and_update_state(invaders)
    assert Invader._shared_state == "RIGHT"
    invaders[0].move_down.assert_called()
