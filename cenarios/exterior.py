
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
        self.base_militar = pygame.Rect(
            520, -60,
            1030, 480
        )

        #casinha_laika - lote 17
        self.casinha_laika = pygame.Rect(
            600, 1500,  # posição x, y
            160, 160    # largura e altura
        )

        #edificio - lote 13 e 14
        self.predio_residencial = pygame.Rect(
            1090, 980,
            920, 430
        )

        #prédio_propaganda - lote 11
        self.predio_propaganda = pygame.Rect(
            60, 930,
            340, 300
        )

        # Caldeirão - lote 5
        self.caldeirao = pygame.Rect(
            2150, 140,
            96, 96
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

        self.sprite_militar = pygame.image.load(
            "sprites/sprite_militar/sprite_0.png"
        ).convert_alpha()

        self.sprite_militar = pygame.transform.scale(
            self.sprite_militar, (1040, 490)
        )

        self.sprite_edificio = pygame.image.load(
            "sprites/sprite_edificio/sprite_0.png"
        ).convert_alpha()

        self.sprite_edificio = pygame.transform.scale(
            self.sprite_edificio, (920, 430)
        )

        self.sprites_caldeirao = [
            pygame.transform.scale(
            pygame.image.load(
                "sprites/sprite_caldeirao/sprite_0.png"
            ).convert_alpha(), (96, 96)),

            pygame.transform.scale(
            pygame.image.load(
                "sprites/sprite_caldeirao/sprite_1.png"
            ).convert_alpha(), (96, 96))
        ]

        self.quadro_caldeirao = 0
        self.tempo_animacao_caldeirao = 0

        self.sprites_abobora = [
            pygame.image.load(
                "sprites/sprite_abobora/sprite_0.png"
            ).convert_alpha(),
        
            pygame.image.load(
                "sprites/sprite_abobora/sprite_1.png"
            ).convert_alpha()
        ]

        self.aboboras = [
            pygame.Rect(700, 250, 64, 64),
            pygame.Rect(1200, 300, 64, 64),
            pygame.Rect(2200, 250, 64, 64),
        ]

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
        militar_tela = self.base_militar.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprite_militar,
            militar_tela.topleft
        )
        
        #casinha_laika
        laika_tela = self.casinha_laika.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprite_laika,
            laika_tela.topleft
        )
        

        #prédio_propaganda
        propaganda_tela = self.predio_propaganda.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprite_propaganda,
            propaganda_tela.topleft
        )

        # prédio residencial - lotes 13 e 14
        edificio_tela = self.predio_residencial.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprite_edificio,
            edificio_tela.topleft
        )

        # Caldeirão - lote 5
        caldeirao_tela = self.caldeirao.move(
            -camera_x, -camera_y
        )

        self.quadro_caldeirao = (
            pygame.time.get_ticks() // 300
        ) % 2

        tela.blit(
            self.sprites_caldeirao[self.quadro_caldeirao],
            caldeirao_tela.topleft
        )

        quadro_abobora = (pygame.time.get_ticks() // 300) % 2

        for abobora in self.aboboras:
            abobora_tela = abobora.move(
                -camera_x, -camera_y
        )

        tela.blit(
            self.sprites_abobora[quadro_abobora],
            abobora_tela.topleft
        )





            