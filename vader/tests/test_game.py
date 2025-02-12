import pytest
from unittest.mock import MagicMock
from vader.game import Game
from vader.laser import Laser
from vader.invader import Invader
from vader.starship import Starship
from vader.board import Board

@pytest.fixture
def setup_game():
    """Fixture pour initialiser un jeu avec les objets nécessaires."""
    # Mocks pour les objets nécessaires
    laser = MagicMock(spec=Laser)
    invader = MagicMock(spec=Invader)
    starship = MagicMock(spec=Starship)
    board = MagicMock(spec=Board)

    # Initialisation de l'objet Game
    game = Game(w=800, h=600, lasers=[laser], invaders=[invader], starship=starship, board=board)
    return game, laser, invader, starship, board


def test_game_initialization(setup_game):
    game, laser, invader, starship, board = setup_game

    assert game._game_state == "START"
    assert game._starship == starship
    assert game._board == board
    assert len(game._lasers) == 1  # Une seule laser est initialisée
    assert len(game._invaders) == 1  # Un seul envahisseur est initialisé


def test_run_method(setup_game):
    game, laser, invader, starship, board = setup_game

    # Tester que la méthode run entre dans la boucle et passe à l'état "PLAYING" lorsqu'on appuie sur ENTER
    with pytest.raises(SystemExit):  # On capture un exit car pygame.quit() va être appelé
        game.run()


def test_show_start_screen(setup_game):
    game, laser, invader, starship, board = setup_game

    # Appeler la méthode qui affiche l'écran de départ
    game.show_start_screen()

    # Vérifier que les bonnes méthodes sont appelées
    board.draw_text.assert_any_call("Space Invaders", (400, 200), 50, (0, 0, 255))
    board.draw_text.assert_any_call("Press ENTER to start", (400, 400), 25, (255, 255, 255))


def test_play_game(setup_game):
    game, laser, invader, starship, board = setup_game

    # Simuler l'appel de la méthode play_game
    game.play_game()

    # Vérifier si certaines méthodes sont appelées pendant le jeu
    board.draw.assert_called()
    game.check_control.assert_called()
    game.update_invader.assert_called()
    game.update_laser.assert_called()


def test_check_laser_invader_collisions(setup_game):
    game, laser, invader, starship, board = setup_game

    # Simuler une collision laser-invader
    laser._direction = "UP"
    laser._line = 5
    laser._column = 3
    invader._line = 5
    invader._column = 3

    game.check_laser_invader_collisions()

    # Vérifier si les lasers et les invaders ont été retirés après la collision
    assert laser not in game._lasers
    assert invader not in game._invaders


def test_reset_game(setup_game):
    game, laser, invader, starship, board = setup_game

    # Appeler la méthode reset_game
    game.reset_game()

    # Vérifier que les lasers sont réinitialisés et les envahisseurs également
    assert len(game._lasers) == 0
    assert len(game._invaders) == 120  # Comme il y a 6 rangées et 20 envahisseurs
    assert game._starship is not None
