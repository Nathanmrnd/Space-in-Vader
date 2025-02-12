import pytest
import pygame
from unittest.mock import patch, MagicMock
from vader.main import argue, main 


def test_argue_valid():
    """Teste si la fonction argue retourne les bonnes valeurs avec des arguments valides."""
    test_args = ["program", "-L", "400", "-l", "600"]
    with patch("sys.argv", test_args):
        args = argue()
        assert args.L == 400
        assert args.l == 600


def test_argue_invalid():
    """Teste si argue lève une erreur lorsque les dimensions sont trop petites."""
    test_args = ["program", "-L", "50", "-l", "50"]
    with patch("sys.argv", test_args), pytest.raises(ValueError, match="The size must be greater or equal to 100"):
        argue()


def test_main():
    """Teste si la fonction main s'exécute sans erreur."""
    with patch("your_module.main.Game.run", MagicMock()), patch("pygame.quit", MagicMock()):
        with patch("your_module.main.argue") as mock_argue:
            mock_argue.return_value.L = 300
            mock_argue.return_value.l = 500
            main()  # Vérifie que la fonction ne plante pas