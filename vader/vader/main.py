from .board import Board
from .invader import Invader
from .laser import Laser
from .starship import Starship

import pygame

import random

W_SCREEN = 300
H_SCREEN = 500

def check_laser_invader_collisions(lasers, invaders, w):
    lasers_to_remove = []
    invaders_to_remove = []

    for laser in lasers:
        if laser.direction == 'UP':  # On ne vérifie que les lasers montant
            laser_x = laser.column * (w / 10)
            laser_y = laser.line * (w / 10)
            laser_rect = pygame.Rect(laser_x, laser_y, 2, w / 50)  # Taille du laser

            for invader in invaders:
                invader_x = invader.column * (w / 10)
                invader_y = invader.line * (w / 10)
                invader_rect = pygame.Rect(invader_x, invader_y, w / 50, w / 50)  # Taille de l'invader

                # ✅ Vérification de collision ET laser qui dépasse légèrement l'invader
                if laser_rect.colliderect(invader_rect) or (
                    laser.line <= invader.line + 1 and laser.column == invader.column
                ):
                    lasers_to_remove.append(laser)
                    invaders_to_remove.append(invader)
                    break  # Un laser ne touche qu’un invader à la fois

    # ✅ Supprimer les objets touchés après la boucle
    for laser in lasers_to_remove:
        if laser in lasers:
            lasers.remove(laser)

    for invader in invaders_to_remove:
        if invader in invaders:
            invaders.remove(invader)

def check_starship_collision(starship, lasers, w):
    """Arrête le jeu si un laser ennemi touche le Starship."""
    starship_x = starship.column * (w / 100)
    starship_y = starship.line * (w / 100) + w / 10
    starship_rect = pygame.Rect(starship_x, starship_y, w / 50, w / 50)  # Taille du vaisseau

    for laser in lasers:
        if laser.direction == 'DOWN':  # Seuls les lasers ennemis comptent
            laser_x = laser.column * (w / 100)
            laser_y = laser.line * (w / 100) + w / 10
            laser_rect = pygame.Rect(laser_x, laser_y, 2, w / 50)  # Taille du laser

            if laser_rect.colliderect(starship_rect):  # Vérification de collision
                print("Starship touché ! Game Over ")
                pygame.quit()
                exit()





def main():
    pygame.init()
    clock = pygame.time.Clock()
    invader_move_counter = 0  # Compteur pour ralentir le déplacement des invaders
    INVADER_MOVE_DELAY = 10   # Modifier cette valeur pour ajuster la vitesse (plus grand = plus lent)


    starship=Starship(50,140)
    lasers=[]
    board = Board(W_SCREEN,H_SCREEN)
    invaders = [Invader(4*i+4,4*j) for i in range(20) for j in range(6)]
    while True :
        board.draw(invaders,lasers,starship)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                return True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    return True
                if event.key == pygame.K_SPACE :
                    lasers.append(starship.blast())
        if keys[pygame.K_LEFT]:
            starship.move_left()
        if keys[pygame.K_RIGHT]:
            starship.move_right()

        
        Invader.check_and_update_state(invaders)
        check_laser_invader_collisions(lasers, invaders, W_SCREEN)
        check_starship_collision(starship, lasers, W_SCREEN)
        invader_move_counter += 1
        if invader_move_counter >= INVADER_MOVE_DELAY:
            Invader.check_and_update_state(invaders)  # Vérifie si on change de direction
            for invader in invaders:
                invader.move_invader()
            invader_move_counter = 0  
        for invader in invaders :
            if random.random()<0.002:
                lasers.append(invader.blast())
        for laser in lasers :
            laser.move_laser()
            laser.delete_outranged(lasers)
        
        clock.tick(30)
    pygame.quit
