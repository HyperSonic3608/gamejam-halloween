import pygame

class Puzzle:
    def __init__(self):
        self.porta = pygame.Rect(290, 448, 60, 32)

        self.paredes = [
            pygame.Rect(0, 0, 640, 32),
            pygame.Rect(0, 448, 290, 32),
            pygame.Rect(350, 448, 290, 32),
            pygame.Rect(0, 0, 32, 480),
            pygame.Rect(608, 0, 32, 480)
        ]

    def desenhar(self, tela):
        tela.fill((55, 50, 45))

        for parede in self.paredes:
            pygame.draw.rect(tela, (100, 100, 100), parede)

    def personagem_perto_da_porta(self, personagem):
        area_interacao = self.porta.inflate(100, 100)
        return personagem.hitbox.colliderect(area_interacao)
