
from .invader import Invader


import pygame
import random



class Game:
    def __init__(self,w,h,lasers,invaders,starship,board):
        self.w = w
        self.h = h
        self.board = board
        self.starship = starship
        self.lasers = lasers
        self.invaders = invaders
        self.clock = pygame.time.Clock()
        self.invader_move_counter = 0
    
    def run(self):
        while True :
            self.board.draw(self.invaders,self.lasers,self.starship)
            pygame.display.update()
            self.check_control()
            self.update_invader()
            self.update_laser()

            
            Invader.check_and_update_state(self.invaders)
            self.check_laser_invader_collisions()
            self.check_starship_collision()


            
            self.clock.tick(30)
    pygame.quit


    def check_control(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE :
                    self.lasers.append(self.starship.blast())
        if keys[pygame.K_LEFT] and not self.starship.is_on_the_left_edge():
            self.starship.move_left()
        if keys[pygame.K_RIGHT]and not self.starship.is_on_the_right_edge():
            self.starship.move_right()

  
    def update_laser(self):
        for laser in self.lasers :
            laser.move_laser()
            laser.delete_outranged(self.lasers)


    def check_laser_invader_collisions(self):
        lasers_to_remove = []
        invaders_to_remove = []

        for laser in self.lasers:
            if laser.direction == 'UP':  # On ne vérifie que les lasers montant
                laser_x = laser.column * (self.w / 10)
                laser_y = laser.line * (self.w / 10)
                laser_rect = pygame.Rect(laser_x, laser_y, 2, self.w / 50)  # Taille du laser

                for invader in self.invaders:
                    invader_x = invader.column * (self.w / 10)
                    invader_y = invader.line * (self.w / 10)
                    invader_rect = pygame.Rect(invader_x, invader_y, self.w / 50, self.w / 50)  # Taille de l'invader

                    #Vérification de collision ET laser qui dépasse légèrement l'invader
                    if laser_rect.colliderect(invader_rect) or (
                        laser.line <= invader.line + 1 and laser.column == invader.column
                    ):
                        lasers_to_remove.append(laser)
                        invaders_to_remove.append(invader)
                        break  #Un laser ne touche qu’un invader à la fois

        #Supprimer les objets touchés après la boucle
        for laser in lasers_to_remove:
            if laser in self.lasers:
                self.lasers.remove(laser)

        for invader in invaders_to_remove:
            if invader in self.invaders:
                self.invaders.remove(invader)

    def check_starship_collision(self):
        """Arrête le jeu si un laser ennemi touche le Starship."""
        starship_x = self.starship.column * (self.w / 100)
        starship_y = self.starship.line * (self.w / 100) + self.w / 10
        starship_rect = pygame.Rect(starship_x, starship_y, self.w / 50, self.w / 50)  # Taille du vaisseau

        for laser in self.lasers:
            if laser.direction == 'DOWN':  # Seuls les lasers ennemis comptent
                laser_x = laser.column * (self.w / 100)
                laser_y = laser.line * (self.w / 100) + self.w / 10
                laser_rect = pygame.Rect(laser_x, laser_y, 2, self.w / 50)  # Taille du laser

                if laser_rect.colliderect(starship_rect):  # Vérification de collision
                    print("Starship is touched : Game Over ")
                    pygame.quit()
                    exit()


    def update_invader(self):
        INVADER_MOVE_DELAY = 10
        self.invader_move_counter += 1
        if self.invader_move_counter >= INVADER_MOVE_DELAY:
            Invader.check_and_update_state(self.invaders)  # Vérifie si on change de direction
            for invader in self.invaders:
                invader.move_invader()
            self.invader_move_counter = 0  
        for invader in self.invaders :
            if random.random()<0.002:
                self.lasers.append(invader.blast())


