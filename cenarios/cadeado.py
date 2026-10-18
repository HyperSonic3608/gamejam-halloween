
import pygame
import random


class Cadeado:
    def __init__(self):
        self.codigo_correto = "31157"
        self.codigo = ["", "", "", "", ""]
        self.palavra = "ORBIT"

        self.resolvido = False
        self.mensagem = ""

        # Paleta de papel antigo
        self.cor_fundo = (185, 180, 163)
        self.cor_elementos = (185, 180, 163)
        self.cor_linhas = (0, 0, 0)
        self.cor_texto = (0, 0, 0)
        self.cor_campo = (185, 180, 163)

        # Fontes nítidas, sem efeitos
        self.fonte_titulo = pygame.font.SysFont(
            "couriernew", 27, bold=True
        )

        self.fonte_letra = pygame.font.SysFont(
            "couriernew", 32, bold=True
        )

        self.fonte_codigo = pygame.font.SysFont(
            "couriernew", 32, bold=True
        )

        self.fonte_mensagem = pygame.font.SysFont(
            "couriernew", 18
        )

        self.fonte_aviso = pygame.font.SysFont(
            "couriernew", 18
        )

        # Campos numéricos
        self.campos = [
            pygame.Rect(200 + i * 50, 350, 42, 52)
            for i in range(5)
        ]

        self.campo_selecionado = 0

        self.botao_confirmar = pygame.Rect(
            220, 435, 200, 48
        )

        # Irregularidades fixas nos contornos
        gerador = random.Random(31)

        self.desvios = [
            [gerador.randint(-2, 2) for _ in range(4)]
            for _ in range(5)
        ]

    # ==============================================
    # TEXTO NÍTIDO, SEM EFEITOS
    # ==============================================

    def renderizar_pixelado(self, fonte, texto, escala=2):
        return fonte.render(
            str(texto),
            False,
            (0, 0, 0)
        )

    # ==============================================
    # CONTORNO IRREGULAR
    # ==============================================

    def desenhar_contorno_irregular(
        self,
        tela,
        retangulo,
        desvio,
        espessura=3
    ):
        x, y, largura, altura = (
            retangulo.x,
            retangulo.y,
            retangulo.width,
            retangulo.height
        )

        d1, d2, d3, d4 = desvio

        pontos = [
            (x + d1, y + d2),
            (x + largura + d2, y + d1),
            (x + largura + d3, y + altura + d4),
            (x + d4, y + altura + d3)
        ]

        pygame.draw.polygon(
            tela,
            self.cor_linhas,
            pontos,
            espessura
        )

        # Pequeno traço artesanal na borda inferior
        pygame.draw.line(
            tela,
            self.cor_linhas,
            (x + 3, y + altura - 2 + d1),
            (x + largura // 3, y + altura - 1 + d2),
            2
        )

    # ==============================================
    # DESENHAR CADEADO
    # ==============================================

    def desenhar(self, tela):
        tela.fill(self.cor_fundo)

        # ------------------------------------------
        # TÍTULO
        # ------------------------------------------

        titulo = self.renderizar_pixelado(
            self.fonte_titulo,
            "ACESSO RESTRITO"
        )

        tela.blit(
            titulo,
            (
                320 - titulo.get_width() // 2,
                75
            )
        )

        # Divisória irregular
        pygame.draw.line(
            tela,
            self.cor_linhas,
            (170, 120),
            (285, 120),
            4
        )

        pygame.draw.line(
            tela,
            self.cor_linhas,
            (300, 122),
            (470, 119),
            4
        )

        # ------------------------------------------
        # PALAVRA PRINCIPAL: ORBIT
        # ------------------------------------------

        for i, letra in enumerate(self.palavra):
            texto = self.renderizar_pixelado(
                self.fonte_letra,
                letra
            )

            tela.blit(
                texto,
                (
                    200 + i * 50,
                    245
                )
            )

        # ------------------------------------------
        # CAMPOS DO CÓDIGO
        # ------------------------------------------

        for i, campo in enumerate(self.campos):

            pygame.draw.rect(
                tela,
                self.cor_campo,
                campo
            )

            self.desenhar_contorno_irregular(
                tela,
                campo,
                self.desvios[i],
                4
            )

            # Destaque do campo selecionado
            if (
                i == self.campo_selecionado
                and not self.resolvido
            ):
                pygame.draw.rect(
                    tela,
                    self.cor_linhas,
                    campo,
                    3
                )

            # Número digitado
            if self.codigo[i]:
                texto = self.renderizar_pixelado(
                    self.fonte_codigo,
                    self.codigo[i]
                )

                tela.blit(
                    texto,
                    (
                        campo.centerx - texto.get_width() // 2,
                        campo.centery - texto.get_height() // 2
                    )
                )

        # ------------------------------------------
        # BOTÃO CONFIRMAR
        # ------------------------------------------

        botao = self.botao_confirmar

        pygame.draw.rect(
            tela,
            self.cor_elementos,
            botao
        )

        # Contorno grosso e irregular
        self.desenhar_contorno_irregular(
            tela,
            botao,
            [1, -2, 2, -1],
            4
        )

        # Traço superior artesanal
        pygame.draw.line(
            tela,
            self.cor_linhas,
            (botao.x + 5, botao.y + 5),
            (botao.x + botao.width - 7, botao.y + 4),
            2
        )

        texto_botao = (
            "DESBLOQUEADO"
            if self.resolvido
            else "CONFIRMAR"
        )

        texto_botao = self.renderizar_pixelado(
            self.fonte_mensagem,
            texto_botao
        )

        tela.blit(
            texto_botao,
            (
                botao.centerx - texto_botao.get_width() // 2,
                botao.centery - texto_botao.get_height() // 2
            )
        )

        # ------------------------------------------
        # MENSAGEM DE RESULTADO
        # ------------------------------------------

        if self.mensagem:
            texto = self.renderizar_pixelado(
                self.fonte_mensagem,
                self.mensagem
            )

            tela.blit(
                texto,
                (
                    320 - texto.get_width() // 2,
                    510
                )
            )

        # ------------------------------------------
        # AVISO PARA SAIR
        # ------------------------------------------

        aviso = self.renderizar_pixelado(
            self.fonte_aviso,
            "APERTE ESC PARA SAIR"
        )

        tela.blit(
            aviso,
            (
                320 - aviso.get_width() // 2,
                570
            )
        )

    # ==============================================
    # TRATAR EVENTOS
    # ==============================================

    def tratar_evento(self, evento):
        if self.resolvido:
            return

        if evento.type == pygame.MOUSEBUTTONDOWN:

            for i, campo in enumerate(self.campos):
                if campo.collidepoint(evento.pos):
                    self.campo_selecionado = i
                    return

            if self.botao_confirmar.collidepoint(evento.pos):
                self.confirmar_codigo()

        if evento.type == pygame.KEYDOWN:

            if evento.unicode and evento.unicode.isdigit():
                self.codigo[self.campo_selecionado] = (
                    evento.unicode
                )

                if self.campo_selecionado < 4:
                    self.campo_selecionado += 1

            elif evento.key == pygame.K_BACKSPACE:

                if self.codigo[self.campo_selecionado]:
                    self.codigo[self.campo_selecionado] = ""

                elif self.campo_selecionado > 0:
                    self.campo_selecionado -= 1
                    self.codigo[self.campo_selecionado] = ""

            elif evento.key == pygame.K_LEFT:
                self.campo_selecionado = max(
                    0,
                    self.campo_selecionado - 1
                )

            elif evento.key == pygame.K_RIGHT:
                self.campo_selecionado = min(
                    4,
                    self.campo_selecionado + 1
                )

            elif evento.key == pygame.K_RETURN:
                self.confirmar_codigo()

    # ==============================================
    # VALIDAR CÓDIGO
    # ==============================================

    def confirmar_codigo(self):
        tentativa = "".join(self.codigo)

        if tentativa == self.codigo_correto:
            self.resolvido = True
            self.mensagem = "CODIGO CORRETO!"

        else:
            self.mensagem = "INCORRETO, TENTE NOVAMENTE."

    # ==============================================
    # REINICIAR
    # ==============================================

    def reiniciar(self):
        self.codigo = ["", "", "", "", ""]
        self.campo_selecionado = 0
        self.resolvido = False
        self.mensagem = ""
