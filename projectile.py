import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('pictures/ball.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 70
        self.rect.y = player.rect.y + 70

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        if self.player.game.collision(self, self.player.game.all_monster):
            self.remove()

        if self.rect.x > 1080:
            self.remove()
