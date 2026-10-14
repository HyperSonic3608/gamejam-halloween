
import pygame


class Exterior:
    LARGURA = 2560
    ALTURA = 1920

    ESPESSURA_MURALHA = 32

    def __init__(self):
        self.paredes = [
            # Limites do mapa
            pygame.Rect(
                0, 0,
                self.LARGURA,
                self.ESPESSURA_MURALHA
            ),
            pygame.Rect(
                0,
                self.ALTURA - self.ESPESSURA_MURALHA,
                self.LARGURA,
                self.ESPESSURA_MURALHA
            ),
            pygame.Rect(
                0, 0,
                self.ESPESSURA_MURALHA,
                self.ALTURA
            ),
            pygame.Rect(
                self.LARGURA - self.ESPESSURA_MURALHA,
                0,
                self.ESPESSURA_MURALHA,
                self.ALTURA
            ),

            
        ]

        self.estrada = pygame.Rect(250, 0, 140, self.ALTURA)
        self.posto = pygame.Rect(440, 70, 120, 100)

        #muralhas
        self.muralha_frente = pygame.image.load(
            "sprites/sprites_muralha/sprite_0.png"
        ).convert_alpha()

        self.muralha_lateral = pygame.image.load(
                    "sprites/sprites_muralha/sprite_1.png"
                ).convert_alpha()

    def desenhar(self, tela, camera_x=0, camera_y=0):
        # Chão
        tela.fill((55, 62, 55))

        # Estrada
        estrada_tela = self.estrada.move(-camera_x, -camera_y)

        pygame.draw.rect(
            tela,
            (85, 78, 65),
            estrada_tela
        )

        # Paredes laterais
        cor_muralha = (82, 84, 78)

        for parede in self.paredes[2:4]:
            parede_tela = parede.move(-camera_x, -camera_y)

            pygame.draw.rect(
                tela,
                cor_muralha,
                parede_tela
            )

        # Muralhas superior e inferior
        largura_sprite = self.muralha_frente.get_width()
        altura_sprite = self.muralha_frente.get_height()

        for x in range(0, self.LARGURA, largura_sprite):

        #desenhando muralhas cima e baixo
            tela.blit(
                self.muralha_frente,
                (x - camera_x, -altura_sprite - camera_y)
            )

            tela.blit(
                self.muralha_frente,
                (
                    x - camera_x,
                    self.ALTURA - altura_sprite - camera_y
                )
            )

        #desenhando muralhas laterais

        altura_sprite = self.muralha_lateral.get_height()
        largura_sprite = self.muralha_lateral.get_width()

        for y in range(0, self.ALTURA, altura_sprite):
            # Esquerda
            tela.blit(
                self.muralha_lateral,
                (0 - camera_x, y - camera_y)
            )

            # Direita
            tela.blit(
                self.muralha_lateral,
                (self.LARGURA - largura_sprite - camera_x, y - camera_y)
            )

            self.construcoes = {
                "administracao": pygame.Rect(650, 300, 220, 160),
                "galpao": pygame.Rect(1500, 250, 300, 200),
                "oficina": pygame.Rect(1850, 580, 220, 170),
                "alojamento": pygame.Rect(560, 1000, 240, 180),
                "deposito": pygame.Rect(1450, 1040, 260, 190),
                "tunel": pygame.Rect(2050, 1510, 150, 100),
                "comunicacoes": pygame.Rect(850, 1570, 180, 140),
            }