
import pygame


class Puzzle:
    def __init__(self):
        # Porta azul decorativa no centro do quarto
        self.porta = pygame.Rect(296, 210, 48, 48)

        self.sprite_passagem = pygame.image.load(
            "sprites/sprite_passagem/sprite_0.png"
        ).convert_alpha()

        self.sprite_passagem = pygame.transform.scale(
            self.sprite_passagem,
            (48, 48)
        )

        # Área de saída na abertura da parede inferior
        self.saida = pygame.Rect(290, 400, 60, 48)
        self.area_interacao_saida = self.saida.inflate(100, 60)

        # Paredes do cenário
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
            pygame.draw.rect(
                tela,
                (100, 100, 100),
                parede
            )

        # Porta azul decorativa: não é a saída
        tela.blit(
            self.sprite_passagem,
            self.porta.topleft
        )

    def personagem_perto_da_porta(self, personagem):
        # Mantém o nome do método para compatibilidade com main.py.
        # Agora verifica a saída na parede inferior.
        return personagem.hitbox.colliderect(
            self.area_interacao_saida
        )
