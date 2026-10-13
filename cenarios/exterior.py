
import pygame

class Exterior:
    LARGURA = 2560
    ALTURA = 1920

    def __init__(self):
        self.paredes = [
            # Limites do mapa
            pygame.Rect(0, 0, self.LARGURA, 32),
            pygame.Rect(0, self.ALTURA - 32, self.LARGURA, 32),
            pygame.Rect(0, 0, 32, self.ALTURA),
            pygame.Rect(self.LARGURA - 32, 0, 32, self.ALTURA),

            # Obstáculo provisório
            pygame.Rect(350, 150, 100, 100)
        ]

        self.estrada = pygame.Rect(250, 0, 140, self.ALTURA)
        self.posto = pygame.Rect(440, 70, 120, 100)

    def desenhar(self, tela, camera_x=0, camera_y=0):
        # Chão
        tela.fill((55, 62, 55))

        estrada_tela = self.estrada.move(-camera_x, -camera_y)

        # Área de terra ou caminho
        pygame.draw.rect(
            tela,
            (85, 78, 65),
            estrada_tela
        )

        obstaculo = self.paredes[4].move(-camera_x, -camera_y)

        pygame.draw.rect(
            tela,
            (100, 100, 100),
            obstaculo
        )

        posto_tela = self.posto.move(-camera_x, -camera_y)

        pygame.draw.rect(
            tela,
            (90, 75, 65),
            posto_tela
        )
