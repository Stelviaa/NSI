# coding=utf-8
import pygame
from pygame.locals import *
from game import Game
from monster import Monster


pygame.init()




#Génération de la fenêtre


pygame.display.set_caption("Projet NSI")
screen = pygame.display.set_mode((928,793))

background = pygame.image.load('pictures/background/Background.png')

game = Game()

running = True

#Boucle infinie

while running:

    screen.blit(background,(0,0)) #injecter l'image "background" dans la fenêtre "screen"

    screen.blit(game.player.image,game.player.rect) #injecter l'image du perso dans la fenetre screen



    for projectile in game.player.all_projectiles:
        projectile.move()
    for monster in game.all_monster:
        monster.avancer()


    game.player.all_projectiles.draw(screen)

    game.all_monster.draw(screen)

    if game.pressed.get(K_d) and game.player.rect.x + game.player.rect.width < screen.get_width() :
        game.player.avancer()
    elif game.pressed.get(K_q) and game.player.rect.x > 0:
        game.player.reculer()



    pygame.display.flip()       #Maj de la fenetre


    for event in pygame.event.get():

        if event.type == QUIT:

            running = False
            pygame.quit()

        elif event.type == KEYDOWN:
            game.pressed[event.key] = True

            if event.key == K_SPACE:
                game.player.projectile()

        elif event.type == KEYUP:
            game.pressed[event.key] = False



