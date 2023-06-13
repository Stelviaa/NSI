import pygame



class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('pictures/characters/Golem/PNG/Golem.png')
        self.image = pygame.transform.scale(self.image,(180,120))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 615
        self.velocity = 1.5


    def avancer(self):
        if not self.game.collision(self,self.game.all_players):
            self.rect.x -= self.velocity








