import pygame


class Exterior:
    LARGURA = 2560
    ALTURA = 1920

    ESPESSURA_MURALHA = 32
    COR_CHAO = (55, 62, 55)

    def __init__(self):
        self.paredes = [
            pygame.Rect(0, 0, self.LARGURA, self.ESPESSURA_MURALHA),
            pygame.Rect(
                0, self.ALTURA - self.ESPESSURA_MURALHA,
                self.LARGURA, self.ESPESSURA_MURALHA
            ),
            pygame.Rect(0, 0, self.ESPESSURA_MURALHA, self.ALTURA),
            pygame.Rect(
                self.LARGURA - self.ESPESSURA_MURALHA,
                0, self.ESPESSURA_MURALHA, self.ALTURA
            ),
        ]

        self.estrada = pygame.Rect(250, 0, 140, self.ALTURA)

        self.estradas_secundarias = [
            pygame.Rect(0, 400, 1590, 100),
            pygame.Rect(1990, 400, 570, 100),
            pygame.Rect(0, 900, 590, 100),
            pygame.Rect(990, 900, 1570, 100),
            pygame.Rect(0, 1400, 2560, 100),
            pygame.Rect(490, 0, 100, 1920),
            pygame.Rect(990, 500, 100, 1420),
            pygame.Rect(1490, 0, 100, 1000),
            pygame.Rect(1490, 1400, 100, 520),
            pygame.Rect(1990, 0, 100, 1920),
        ]

        self.posto = pygame.Rect(440, 70, 120, 100)

        # Muralhas
        self.muralha_frente = pygame.image.load(
            "sprites/sprites_muralha/sprite_0.png"
        ).convert_alpha()

        self.muralha_lateral = pygame.image.load(
            "sprites/sprites_muralha/sprite_1.png"
        ).convert_alpha()

        # Quarto inicial
        self.quarto_inicial = pygame.Rect(10, -60, 460, 490)

        self.sprite_quarto = pygame.image.load(
            "sprites/sprite_quarto/sprite_2.png"
        ).convert_alpha()

        self.sprite_quarto = pygame.transform.scale(
            self.sprite_quarto, (460, 490)
        )

        # Prédio militar
        self.base_militar = pygame.Rect(520, -60, 1030, 480)

        self.sprite_militar = pygame.image.load(
            "sprites/sprite_militar/sprite_0.png"
        ).convert_alpha()

        self.sprite_militar = pygame.transform.scale(
            self.sprite_militar, (1040, 490)
        )

        # Casinha da Laika
        self.casinha_laika = pygame.Rect(600, 1500, 160, 160)
        self.area_laika = self.casinha_laika.inflate(100, 100)

        self.sprite_laika_original = pygame.image.load(
            "sprites/sprite_laika/sprite_0.png"
        ).convert_alpha()

        self.sprite_laika = pygame.transform.scale(
            self.sprite_laika_original, (160, 160)
        )

        # Imagem da pista encontrada na carta da Laika
        self.pista_laika_original = pygame.image.load(
            "sprites/pista_laika/sprite_0.png"
        ).convert_alpha()

        # Prédio residencial
        self.predio_residencial = pygame.Rect(1090, 980, 920, 430)

        self.sprite_edificio = pygame.image.load(
            "sprites/sprite_edificio/sprite_0.png"
        ).convert_alpha()

        self.sprite_edificio = pygame.transform.scale(
            self.sprite_edificio, (920, 430)
        )

        # Prédio da propaganda
        self.predio_propaganda = pygame.Rect(60, 930, 340, 300)

        self.sprite_propaganda = pygame.image.load(
            "sprites/sprite_propaganda/sprite_0.png"
        ).convert_alpha()

        self.sprite_propaganda = pygame.transform.scale(
            self.sprite_propaganda, (460, 490)
        )

        # Caldeirão
        self.caldeirao = pygame.Rect(2150, 140, 96, 96)

        self.sprites_caldeirao = [
            pygame.transform.scale(
                pygame.image.load(
                    "sprites/sprite_caldeirao/sprite_0.png"
                ).convert_alpha(),
                (96, 96)
            ),
            pygame.transform.scale(
                pygame.image.load(
                    "sprites/sprite_caldeirao/sprite_1.png"
                ).convert_alpha(),
                (96, 96)
            )
        ]

        # Mesa do lote 5
        self.mesa = pygame.Rect(2260, 140, 96, 96)

        self.sprite_mesa = pygame.image.load(
            "sprites/sprite_mesa/sprite_0.png"
        ).convert_alpha()

        self.sprite_mesa = pygame.transform.scale(
            self.sprite_mesa, (96, 96)
        )

        self.quadro_caldeirao = 0
        self.tempo_animacao_caldeirao = 0

        # Abóboras
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

        # Edifício do puzzle
        self.predio_puzzle = pygame.Rect(2090, 945, 460, 490)

        self.sprite_puzzle = pygame.image.load(
            "sprites/sprite_quarto/sprite_2.png"
        ).convert_alpha()

        self.sprite_puzzle = pygame.transform.scale(
            self.sprite_puzzle, (460, 490)
        )

    def desenhar(self, tela, camera_x=0, camera_y=0):
        # Chão
        tela.fill(self.COR_CHAO)

        # Estrada principal
        estrada_tela = self.estrada.move(-camera_x, -camera_y)
        pygame.draw.rect(tela, (85, 78, 65), estrada_tela)

        cor_estrada = (48, 49, 48)

        # Estradas secundárias
        for estrada in self.estradas_secundarias:
            estrada_tela = estrada.move(-camera_x, -camera_y)
            pygame.draw.rect(tela, cor_estrada, estrada_tela)

        # Faixas das estradas
        cor_faixa = (175, 175, 165)
        comprimento_traco = 30
        espaco_tracos = 25
        espessura_traco = 5

        for estrada in self.estradas_secundarias:
            estrada_tela = estrada.move(-camera_x, -camera_y)

            if estrada.width > estrada.height:
                y_centro = estrada_tela.centery

                for x in range(
                    estrada_tela.left,
                    estrada_tela.right,
                    comprimento_traco + espaco_tracos
                ):
                    x_final = min(
                        x + comprimento_traco,
                        estrada_tela.right
                    )

                    pygame.draw.line(
                        tela,
                        cor_faixa,
                        (x, y_centro),
                        (x_final, y_centro),
                        espessura_traco
                    )
            else:
                x_centro = estrada_tela.centerx

                for y in range(
                    estrada_tela.top,
                    estrada_tela.bottom,
                    comprimento_traco + espaco_tracos
                ):
                    y_final = min(
                        y + comprimento_traco,
                        estrada_tela.bottom
                    )

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
            pygame.draw.rect(tela, cor_muralha, parede_tela)

        # Muralhas superior e inferior
        largura_sprite = self.muralha_frente.get_width()
        altura_sprite = self.muralha_frente.get_height()

        for x in range(0, self.LARGURA, largura_sprite):
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

        # Muralhas laterais
        altura_sprite = self.muralha_lateral.get_height()
        largura_sprite = self.muralha_lateral.get_width()

        for y in range(0, self.ALTURA, altura_sprite):
            tela.blit(
                self.muralha_lateral,
                (-camera_x, y - camera_y)
            )

            tela.blit(
                self.muralha_lateral,
                (
                    self.LARGURA - largura_sprite - camera_x,
                    y - camera_y
                )
            )

        # Quarto inicial
        quarto_tela = self.quarto_inicial.move(
            -camera_x, -camera_y
        )
        tela.blit(self.sprite_quarto, quarto_tela.topleft)

        # Prédio militar
        militar_tela = self.base_militar.move(
            -camera_x, -camera_y
        )
        tela.blit(self.sprite_militar, militar_tela.topleft)

        # Casinha da Laika
        laika_tela = self.casinha_laika.move(
            -camera_x, -camera_y
        )
        tela.blit(self.sprite_laika, laika_tela.topleft)

        # Prédio da propaganda
        propaganda_tela = self.predio_propaganda.move(
            -camera_x, -camera_y
        )
        tela.blit(self.sprite_propaganda, propaganda_tela.topleft)

        # Prédio residencial
        edificio_tela = self.predio_residencial.move(
            -camera_x, -camera_y
        )
        tela.blit(self.sprite_edificio, edificio_tela.topleft)

        # Caldeirão animado
        self.quadro_caldeirao = (
            pygame.time.get_ticks() // 300
        ) % 2

        caldeirao_tela = self.caldeirao.move(
            -camera_x, -camera_y
        )

        tela.blit(
            self.sprites_caldeirao[self.quadro_caldeirao],
            caldeirao_tela.topleft
        )

        # Mesa do lote 5
        mesa_tela = self.mesa.move(-camera_x, -camera_y)
        tela.blit(self.sprite_mesa, mesa_tela.topleft)

        # Abóboras animadas
        quadro_abobora = (pygame.time.get_ticks() // 300) % 2

        for abobora in self.aboboras:
            abobora_tela = abobora.move(
                -camera_x, -camera_y
            )

            tela.blit(
                self.sprites_abobora[quadro_abobora],
                abobora_tela.topleft
            )

        # Edifício do puzzle
        puzzle_tela = self.predio_puzzle.move(
            -camera_x, -camera_y
        )
        tela.blit(self.sprite_puzzle, puzzle_tela.topleft)

    # INTERAÇÃO COM A LAIKA

    def personagem_perto_da_laika(self, personagem):
        return personagem.hitbox.colliderect(self.area_laika)

    def desenhar_tela_laika(self, tela):
        # Fundo igual ao chão do mapa
        tela.fill(self.COR_CHAO)

        imagem = self.sprite_laika_original

        largura_maxima = int(tela.get_width() * 0.75)
        altura_maxima = int(tela.get_height() * 0.75)

        largura_original, altura_original = imagem.get_size()

        escala = min(
            largura_maxima / largura_original,
            altura_maxima / altura_original
        )

        largura = max(1, round(largura_original * escala))
        altura = max(1, round(altura_original * escala))

        casinha_grande = pygame.transform.scale(
            imagem, (largura, altura)
        )

        x = (tela.get_width() - largura) // 2
        y = (tela.get_height() - altura) // 2

        tela.blit(casinha_grande, (x, y))

        fonte = pygame.font.Font(None, 30)

        texto = fonte.render(
            "E - ler     ESC - voltar",
            False,
            (0, 0, 0)
        )

        tela.blit(
            texto,
            (
                (tela.get_width() - texto.get_width()) // 2,
                tela.get_height() - 55
            )
        )

    def desenhar_carta_laika(self, tela):
        # Fundo escurecido
        camada = pygame.Surface(
            tela.get_size(),
            pygame.SRCALPHA
        )
        camada.fill((0, 0, 0, 150))
        tela.blit(camada, (0, 0))

        # Carta
        largura = 900
        altura = 700

        x = (tela.get_width() - largura) // 2
        y = (tela.get_height() - altura) // 2

        carta = pygame.Rect(x, y, largura, altura)

        pygame.draw.rect(
            tela, (228, 217, 188), carta, border_radius=8
        )
        pygame.draw.rect(
            tela, (130, 115, 87), carta,
            width=4, border_radius=8
        )

        fonte_titulo = pygame.font.Font(None, 52)
        fonte_texto = pygame.font.Font(None, 34)
        fonte_rodape = pygame.font.Font(None, 26)

        # Texto preto, sem antialiasing
        cor_texto = (0, 0, 0)

        # Título centralizado
        titulo = fonte_titulo.render(
            "Лайка",
            False,
            cor_texto
        )
        tela.blit(
            titulo,
            (carta.centerx - titulo.get_width() // 2, y + 30)
        )

        # Texto alinhado à esquerda
        linhas = [
            "Em homenagem àquela que nunca voltou.",
            "Seu nome marcou a história da exploração espacial",
            "e permanece como lembrança de um dos primeiros",
            "passos da humanidade rumo às estrelas."
        ]

        margem_esquerda = x + 55
        inicio_texto_y = y + 120
        espacamento = 42

        for i, linha in enumerate(linhas):
            texto = fonte_texto.render(
                linha,
                False,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    margem_esquerda,
                    inicio_texto_y + i * espacamento
                )
            )

        # Pista menor na parte inferior
        imagem = self.pista_laika_original

        largura_maxima = 350
        altura_maxima = 200

        largura_original, altura_original = imagem.get_size()

        escala = min(
            largura_maxima / largura_original,
            altura_maxima / altura_original
        )

        largura_pista = max(1, round(largura_original * escala))
        altura_pista = max(1, round(altura_original * escala))

        pista = pygame.transform.scale(
            imagem,
            (largura_pista, altura_pista)
        )

        pista_x = carta.centerx - largura_pista // 2
        pista_y = y + 370

        tela.blit(pista, (pista_x, pista_y))

        # Instrução no rodapé
        rodape = fonte_rodape.render(
            "ESC - voltar",
            False,
            cor_texto
        )

        tela.blit(
            rodape,
            (
                carta.centerx - rodape.get_width() // 2,
                carta.bottom - 40
            )
        )