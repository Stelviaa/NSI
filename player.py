# coding=utf-8
import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game        #caractéristiques par défaut
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('pictures/characters/Primer character/PNG/Knight/knight.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 623

    def avancer(self):
        if not self.game.collision(self,self.game.all_monster):
            self.rect.x += self.velocity
        

    def reculer(self):
        if not self.game.collision(self,self.game.all_monster):
            self.rect.x -= self.velocity

    def projectile(self):
        self.all_projectiles.add(Projectile(self))


