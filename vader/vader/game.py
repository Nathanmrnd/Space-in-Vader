from .invader import Invader
import pygame
import random
from .board import Board
from .starship import Starship
from .laser import Laser

class Game:
    def __init__(self, w: int, h: int, lasers: list[Laser], invaders: list[Invader], starship: Starship, board: Board) -> None:
        self._w = w
        self._h = h
        self._board = board
        self._starship = starship
        self._lasers = lasers
        self._invaders = invaders
        self._clock = pygame.time.Clock()
        self._invader_move_counter = 0
        self._game_state = "START"  # Initial game state

    def run(self) -> None:
        # Main game loop
        while True:
            if self._game_state == "START":
                self.show_start_screen()
            elif self._game_state == "PLAYING":
                self.play_game()
            elif self._game_state == "GAME_OVER":
                self.show_game_over_screen()
            elif self._game_state == "WIN":
                self.show_win_screen()

    def show_start_screen(self) -> None:
        # Draw the start screen
        self._board.draw_text("Space Invaders", (self._w // 2, self._h // 3), 50, (0, 0, 255))
        self._board.draw_text("Press SPACE to shoot, ARROW keys to move", (self._w // 2, self._h // 2), 20, (255, 255, 255))
        self._board.draw_text("Press ENTER to start", (self._w // 2, self._h * 2 // 3), 25, (255, 255, 255))
        pygame.display.update()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self._game_state = "PLAYING"

    def play_game(self) -> None:
        self._board.draw(self._invaders, self._lasers, self._starship)
        pygame.display.update()
        # Check for user input and update game state
        self.check_control()
        self.update_invader()
        self.update_laser()
        Invader.check_and_update_state(self._invaders)
        self.check_laser_invader_collisions()
        self.check_starship_collision()

        # Check for win condition
        if not self._invaders:
            self._game_state = "WIN"
        self._clock.tick(30) # Control the frame rate

    def show_game_over_screen(self) -> None:
        # Draw the game over screen
        self._board.draw_text("Game Over", (self._w // 2, self._h // 3), 50, (255, 0, 0))
        self._board.draw_text("Press ENTER to play again", (self._w // 2, self._h // 2), 30, (255, 255, 255))
        pygame.display.update()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.reset_game()
                    self._game_state = "PLAYING"

    def show_win_screen(self) -> None:
        # Draw the win screen
        self._board.draw_text("You Win!", (self._w // 2, self._h // 3), 50, (0, 255, 0))
        self._board.draw_text("Press ENTER to play again", (self._w // 2, self._h // 2), 30, (255, 255, 255))
        pygame.display.update()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.reset_game()
                    self._game_state = "PLAYING"

    def reset_game(self) -> None:
        # Reset the game objects
        self._lasers = []
        self._invaders = [Invader(4 * i + 4, 4 * j) for i in range(20) for j in range(6)]
        self._starship = Starship(50, 140)

    def check_control(self) -> None:
        # Check for user input
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    self._lasers.append(self._starship.blast())
        if keys[pygame.K_LEFT] and not self._starship.is_on_the_left_edge():
            self._starship.move_left()
        if keys[pygame.K_RIGHT] and not self._starship.is_on_the_right_edge():
            self._starship.move_right()

    def update_laser(self) -> None:
        for laser in self._lasers:
            laser.move_laser()
            laser.delete_outranged(self._lasers)

    def check_laser_invader_collisions(self) -> None:
        lasers_to_remove = []
        invaders_to_remove = []
        for laser in self._lasers:
            if laser._direction == 'UP':
                laser_x = laser._column * (self._w / 100)
                laser_y = laser._line * (self._w / 100)
                laser_rect = pygame.Rect(laser_x, laser_y, 2, self._w / 50)
                for invader in self._invaders:
                    invader_x = invader._column * (self._w / 100)
                    invader_y = invader._line * (self._w / 100)
                    invader_rect = pygame.Rect(invader_x, invader_y, self._w / 50, self._w / 50)
                    if laser_rect.colliderect(invader_rect) or (
                        laser._line <= invader._line + 1 and laser._column == invader._column
                    ):
                        lasers_to_remove.append(laser)
                        invaders_to_remove.append(invader)
                        break
        for laser in lasers_to_remove:
            if laser in self._lasers:
                self._lasers.remove(laser)
        for invader in invaders_to_remove:
            if invader in self._invaders:
                self._invaders.remove(invader)

    def check_starship_collision(self) -> None:
        # Check for collisions between lasers and the starship
        starship_x = self._starship._column * (self._w / 100)
        starship_y = self._starship._line * (self._w / 100) + self._w / 10
        starship_rect = pygame.Rect(starship_x, starship_y, self._w / 50, self._w / 50)
        for laser in self._lasers:
            if laser._direction == 'DOWN':
                laser_x = laser._column * (self._w / 100)
                laser_y = laser._line * (self._w / 100) + self._w / 10
                laser_rect = pygame.Rect(laser_x, laser_y, 2, self._w / 50)
                if laser_rect.colliderect(starship_rect):
                    self._game_state = "GAME_OVER"

    def update_invader(self) -> None:
        # Update the position of each invader
        INVADER_MOVE_DELAY = 3
        self._invader_move_counter += 1
        if self._invader_move_counter >= INVADER_MOVE_DELAY:
            Invader.check_and_update_state(self._invaders)
            for invader in self._invaders:
                invader.move_invader()
            self._invader_move_counter = 0
        for invader in self._invaders:
            if random.random() < 0.002:
                self._lasers.append(invader.blast())
