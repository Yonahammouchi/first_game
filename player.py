import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__
        self.health = 100
        self.max_health = 100
        self.ttack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("first_game/assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        projectile = Projectile()

        self.all_projectiles.add(Projectile())

    
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity