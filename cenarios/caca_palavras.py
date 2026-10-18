
import pygame
import random


class CacaPalavras:
    def __init__(self):
        # Números do enigma
        self.numeros_linhas = [2, 8, 5, 8, 3, 7, 6]
        self.numeros_colunas = [1, 9, 0, 1, 7, 5, 2]

        # Grade de letras
        self.grade = [
            ["A", "T", "A", "S", "E", "A", "T"],
            ["O", "R", "M", "B", "T", "K", "B"],
            ["K", "I", "O", "U", "R", "I", "E"],
            ["R", "V", "N", "B", "S", "A", "H"],
            ["O", "E", "U", "E", "O", "L", "O"],
            ["L", "S", "I", "M", "V", "B", "R"],
            ["R", "I", "T", "U", "A", "L", "A"]
        ]

        # Posição e tamanho
        self.tamanho_celula = 55
        self.x_grade = 430
        self.y_grade = 220

        # Fontes monoespaçadas
        self.fonte_numeros = pygame.font.SysFont(
            "couriernew", 25
        )

        self.fonte_letras = pygame.font.SysFont(
            "couriernew", 30, bold=True
        )

        # Paleta de cores
        self.cor_fundo = (185, 180, 163)
        self.cor_celula = (185, 180, 163)
        self.cor_grade = (0, 0, 0)
        self.cor_texto = (0, 0, 0)

        # Contornos irregulares reproduzíveis
        gerador = random.Random(17)
        self.desvios = {}

        for linha in range(7):
            for coluna in range(7):
                self.desvios[(linha, coluna)] = [
                    gerador.randint(-2, 2)
                    for _ in range(4)
                ]

    # ==============================================
    # DESENHAR O CAÇA-PALAVRAS SOZINHO
    # ==============================================

    def desenhar(self, tela):
        tela.fill(self.cor_fundo)
        self._desenhar_grade(tela)

    # ==============================================
    # DESENHAR DENTRO DO PAINEL DO PUZZLE
    # ==============================================

    def desenhar_na_tela(
        self,
        tela,
        x_grade=850,
        y_grade=250,
        tamanho_celula=45
    ):
        self.x_grade = x_grade
        self.y_grade = y_grade
        self.tamanho_celula = tamanho_celula

        # Não limpa a superfície:
        # o cadeado já foi desenhado nela.
        self._desenhar_grade(tela)

    # ==============================================
    # TEXTO NÍTIDO, SEM REDUZIR E AMPLIAR
    # ==============================================

    def _renderizar_texto(self, fonte, texto):
        return fonte.render(
            str(texto),
            False,
            self.cor_texto
        )

    # ==============================================
    # CONTORNO ARTESANAL
    # ==============================================

    def _desenhar_contorno(
        self,
        tela,
        x,
        y,
        tamanho,
        desvios
    ):
        d1, d2, d3, d4 = desvios

        pontos = [
            (x + d1, y + d2),
            (x + tamanho + d2, y + d1),
            (x + tamanho + d3, y + tamanho + d4),
            (x + d4, y + tamanho + d3)
        ]

        # Contorno principal
        pygame.draw.polygon(
            tela,
            self.cor_grade,
            pontos,
            3
        )

        # Pequenos traços irregulares
        pygame.draw.line(
            tela,
            self.cor_grade,
            (x + 4, y + tamanho - 3 + d1),
            (x + tamanho // 3, y + tamanho - 2 + d2),
            2
        )

    # ==============================================
    # DESENHO DA GRADE
    # ==============================================

    def _desenhar_grade(self, tela):
        tamanho = self.tamanho_celula

        # ------------------------------------------
        # NÚMEROS DAS COLUNAS
        # ------------------------------------------

        for coluna, numero in enumerate(
            self.numeros_colunas
        ):
            texto = self._renderizar_texto(
                self.fonte_numeros,
                numero
            )

            centro_x = (
                self.x_grade
                + coluna * tamanho
                + tamanho // 2
            )

            y = self.y_grade - 35

            tela.blit(
                texto,
                (
                    centro_x - texto.get_width() // 2,
                    y
                )
            )

        # ------------------------------------------
        # NÚMEROS DAS LINHAS
        # ------------------------------------------

        for linha, numero in enumerate(
            self.numeros_linhas
        ):
            texto = self._renderizar_texto(
                self.fonte_numeros,
                numero
            )

            x = self.x_grade - 32

            centro_y = (
                self.y_grade
                + linha * tamanho
                + tamanho // 2
            )

            tela.blit(
                texto,
                (
                    x - texto.get_width() // 2,
                    centro_y - texto.get_height() // 2
                )
            )

        # ------------------------------------------
        # CÉLULAS E LETRAS
        # ------------------------------------------

        for linha in range(7):
            for coluna in range(7):

                x = self.x_grade + coluna * tamanho
                y = self.y_grade + linha * tamanho

                retangulo = pygame.Rect(
                    x,
                    y,
                    tamanho,
                    tamanho
                )

                # Fundo da célula
                pygame.draw.rect(
                    tela,
                    self.cor_celula,
                    retangulo
                )

                # Contorno irregular
                self._desenhar_contorno(
                    tela,
                    x,
                    y,
                    tamanho,
                    self.desvios[(linha, coluna)]
                )

                # Letra centralizada
                letra = self.grade[linha][coluna]

                texto = self._renderizar_texto(
                    self.fonte_letras,
                    letra
                )

                tela.blit(
                    texto,
                    (
                        x + (tamanho - texto.get_width()) // 2,
                        y + (tamanho - texto.get_height()) // 2
                    )
                )
