
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

        
        self.estradas_secundarias = [
            # Estrada horizontal superior
            # Abertura entre os lotes 4 e 9
            pygame.Rect(0, 400, 1590, 100),
            pygame.Rect(1990, 400, 570, 100),

            # Estrada horizontal central
            # Abertura entre os lotes 7 e 12
            pygame.Rect(0, 900, 590, 100),
            pygame.Rect(990, 900, 1570, 100),

            # Estrada horizontal inferior
            pygame.Rect(0, 1400, 2560, 100),

            # Estradas verticais
            pygame.Rect(490, 0, 100, 1920),

            # Abertura entre os lotes 2 e 3
            pygame.Rect(990, 500, 100, 1420),

            # Estrada vertical com abertura entre os lotes 13 e 14
            pygame.Rect(1490, 0, 100, 1000),
            pygame.Rect(1490, 1400, 100, 520),
            
            pygame.Rect(1990, 0, 100, 1920),
        ]


        self.posto = pygame.Rect(440, 70, 120, 100)

        #muralhas
        self.muralha_frente = pygame.image.load(
            "sprites/sprites_muralha/sprite_0.png"
        ).convert_alpha()

        self.muralha_lateral = pygame.image.load(
                    "sprites/sprites_muralha/sprite_1.png"
                ).convert_alpha()

        #quarto inicial - lote 1
        self.quarto_inicial = pygame.Rect(
            10, -60,
            460, 490
        )

        #prédio - lotes 2 e 3
        self.predio = pygame.Rect(
            650, 40,
            780, 320
        )

        #casinha_laika - lote 17
        self.casinha_laika = pygame.Rect(
            600, 1500,  # posição x, y
            160, 160    # largura e altura
        )

        #prédio_militar - lote 13 e 14
        self.predio_militar = pygame.Rect(
            1160, 1030,
            780, 320
        )

        #prédio_propaganda - lote 11
        self.predio_propaganda = pygame.Rect(
            60, 930,
            340, 300
        )

        self.sprite_quarto = pygame.image.load(
            "sprites/sprite_quarto/sprite_2.png"
        ).convert_alpha()

        self.sprite_quarto = pygame.transform.scale(
            self.sprite_quarto, (460, 490)
        )

        self.sprite_propaganda = pygame.image.load(
            "sprites/sprite_propaganda/sprite_0.png"
        ).convert_alpha()

        self.sprite_propaganda = pygame.transform.scale(
            self.sprite_propaganda, (460, 490)
        )

        self.sprite_laika = pygame.image.load(
            "sprites/sprite_laika/sprite_0.png"
        ).convert_alpha()

        self.sprite_laika = pygame.transform.scale(self.sprite_laika, (160, 160)
        )

    def desenhar(self, tela, camera_x=0, camera_y=0):
        # Chão
        tela.fill((55, 62, 55))

        # Estrada principal
        estrada_tela = self.estrada.move(-camera_x, -camera_y)

        pygame.draw.rect(
            tela,
            (85, 78, 65),
            estrada_tela
        )

        cor_estrada = (48, 49, 48)

        # Estradas secundarias
        for estrada in self.estradas_secundarias:
            estrada_tela = estrada.move(-camera_x, -camera_y)

            pygame.draw.rect(
                tela,
                cor_estrada,
                estrada_tela
            )

        cor_faixa = (175, 175, 165)

        comprimento_traco = 30
        espaco_tracos = 25
        espessura_traco = 5

        for estrada in self.estradas_secundarias:
            estrada_tela = estrada.move(-camera_x, -camera_y)

            # Estrada horizontal
            if estrada.width > estrada.height:
                y_centro = estrada_tela.centery
                x_inicio = estrada_tela.left
                x_fim = estrada_tela.right

                for x in range(
                    x_inicio,
                    x_fim,
                    comprimento_traco + espaco_tracos
                ):
                    x_final = min(x + comprimento_traco, x_fim)

                    pygame.draw.line(
                        tela,
                        cor_faixa,
                        (x, y_centro),
                        (x_final, y_centro),
                        espessura_traco
                    )

            # Estrada vertical
            else:
                x_centro = estrada_tela.centerx
                y_inicio = estrada_tela.top
                y_fim = estrada_tela.bottom

                for y in range(
                    y_inicio,
                    y_fim,
                    comprimento_traco + espaco_tracos
                ):
                    y_final = min(y + comprimento_traco, y_fim)

                    pygame.draw.line(
                        tela,
                        cor_faixa,
                        (x_centro, y),
                        (x_centro, y_final),
                        espessura_traco
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

        #quarto inical - lote 1
        quarto_tela = self.quarto_inicial.move(
            -camera_x, -camera_y
        )

        tela.blit(self.sprite_quarto, quarto_tela.topleft)


        #prédio - lote 2 e 3
        predio_tela = self.predio.move(
            -camera_x, -camera_y
        )

        pygame.draw.rect(
            tela,
            (115, 112, 104), 
            predio_tela
        )

        pygame.draw.rect(
            tela,
            (45, 44, 41), 
            predio_tela,
            4
        )
        
        #casinha_laika
        laika_tela = self.casinha_laika.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprite_laika,
            laika_tela.topleft
        )

        #prédio_militar
        predio_militar_tela = self.predio_militar.move(
            -camera_x, -camera_y
        )

        pygame.draw.rect(
            tela,
            (91, 96, 91),
            predio_militar_tela
        )

        pygame.draw.rect(
            tela,
            (35, 38, 35),
            predio_militar_tela,
            4
        )

        #prédio_propaganda
        propaganda_tela = self.predio_propaganda.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprite_propaganda,
            propaganda_tela.topleft
        )





            