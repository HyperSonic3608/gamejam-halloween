import pygame

class Quarto:
    def __init__(self):
        self.porta = pygame.Rect(580, 180, 60, 100)
        self.paredes = [
            pygame.Rect(0, 0, 640, 32),
            pygame.Rect(0, 448, 640, 32),
            pygame.Rect(0, 0, 32, 480),

            #parede da direita parte de cima e de baixo
            pygame.Rect(608, 0, 32, 180),
            pygame.Rect(608, 280, 32, 200)
        ]

    def desenhar(self, tela):
        tela.fill((55,50,45))
        for parede in self.paredes:
            pygame.draw.rect(tela, (100, 100, 100), parede)

    def personagem_perto_da_porta(self, personagem):
        return personagem.hitbox.colliderect(self.porta)