import pygame
from game import Game

pygame.init()


pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("first_game/assets/bg.jpg")

game = Game()

running = True

while running:

   screen.blit(background, (0, -200))

   screen.blit(game.player.image, game.player.rect)

   pygame.display.flip()

   for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

            pygame.quit()
            
            print("fermeture du jeu")
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key ==pygame.K_LEFT:
               game.player.move_left()