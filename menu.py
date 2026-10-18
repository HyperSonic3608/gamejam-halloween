
import os
import pygame


class MenuInicial:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        self.fonte = pygame.font.SysFont(
            "monospace", 24, bold=True
        )
        self.fonte_pequena = pygame.font.SysFont(
            "monospace", 18, bold=True
        )

        self.opcoes = ["JOGAR", "COMANDOS", "CRÉDITOS", "SAIR"]
        self.selecionada = 0
        self.tela_atual = "menu"

        # Carrega a logo
        caminho_logo = os.path.join(
            os.path.dirname(__file__),
            "sprites",
            "sprite_logo",
            "sprite_0.png"
        )

        self.logo = pygame.image.load(caminho_logo).convert_alpha()

        # Limita a logo para caber na parte superior da tela
        limite_largura = largura - 80
        limite_altura = altura // 2

        escala = min(
            limite_largura / self.logo.get_width(),
            limite_altura / self.logo.get_height(),
            1
        )

        novo_tamanho = (
            int(self.logo.get_width() * escala),
            int(self.logo.get_height() * escala)
        )

        self.logo = pygame.transform.scale(
            self.logo, novo_tamanho
        )

    def desenhar_texto_centralizado(self, tela, texto, fonte, cor, y):
        imagem = fonte.render(texto, True, cor)
        x = (self.largura - imagem.get_width()) // 2
        tela.blit(imagem, (x, y))

    def desenhar(self, tela):
        tela.fill((0, 0, 0))

        branco = (255, 255, 255)
        cinza = (150, 150, 150)

        if self.tela_atual == "menu":
            # Logo centralizada na parte superior
            x_logo = (self.largura - self.logo.get_width()) // 2
            tela.blit(self.logo, (x_logo, 35))

            # Opções do menu
            inicio_y = self.altura // 2 + 35
            espacamento = 42

            for i, opcao in enumerate(self.opcoes):
                cor = branco if i == self.selecionada else cinza
                prefixo = "> " if i == self.selecionada else "  "

                self.desenhar_texto_centralizado(
                    tela,
                    prefixo + opcao,
                    self.fonte,
                    cor,
                    inicio_y + i * espacamento
                )

        elif self.tela_atual == "comandos":
            self.desenhar_texto_centralizado(
                tela, "COMANDOS", self.fonte, branco, 100
            )
            comandos = [
                "WASD - MOVIMENTAR",
                "E - INTERAGIR",
                "ESC - VOLTAR"
            ]

            for i, comando in enumerate(comandos):
                self.desenhar_texto_centralizado(
                    tela, comando, self.fonte_pequena,
                    branco, 190 + i * 40
                )

        elif self.tela_atual == "creditos":
            self.desenhar_texto_centralizado(
                tela, "CREDITOS", self.fonte, branco, 100
            )
            self.desenhar_texto_centralizado(
                tela, "DESENVOLVIDO POR", self.fonte_pequena,
                branco, 200
            )
            self.desenhar_texto_centralizado(
                tela, "MATEUS", self.fonte_pequena,
                branco, 240
            )
            self.desenhar_texto_centralizado(
                tela, "ESC - VOLTAR", self.fonte_pequena,
                cinza, self.altura - 70
            )

    def tratar_evento(self, evento):
        if evento.type != pygame.KEYDOWN:
            return None

        if self.tela_atual == "menu":
            if evento.key in (pygame.K_UP, pygame.K_w):
                self.selecionada = (
                    self.selecionada - 1
                ) % len(self.opcoes)

            elif evento.key in (pygame.K_DOWN, pygame.K_s):
                self.selecionada = (
                    self.selecionada + 1
                ) % len(self.opcoes)

            elif evento.key == pygame.K_RETURN:
                opcao = self.opcoes[self.selecionada]

                if opcao == "JOGAR":
                    return "jogar"

                elif opcao == "COMANDOS":
                    self.tela_atual = "comandos"

                elif opcao == "CRÉDITOS":
                    self.tela_atual = "creditos"

                elif opcao == "SAIR":
                    return "sair"

        elif evento.key == pygame.K_ESCAPE:
            self.tela_atual = "menu"

        return None
