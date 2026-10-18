
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

        self.logo = pygame.image.load(
            caminho_logo
        ).convert_alpha()

        # Redimensiona a logo sem aumentá-la
        limite_largura = largura - 40
        limite_altura = int(altura * 0.90)

        escala = min(
            limite_largura / self.logo.get_width(),
            limite_altura / self.logo.get_height(),
        )

        novo_tamanho = (
            int(self.logo.get_width() * escala),
            int(self.logo.get_height() * escala)
        )

        self.logo = pygame.transform.scale(
            self.logo, novo_tamanho
        )

        # Áreas clicáveis dos botões
        self.botoes = []

    def desenhar_texto_centralizado(
        self, tela, texto, fonte, cor, y
    ):
        imagem = fonte.render(texto, True, cor)
        x = (self.largura - imagem.get_width()) // 2
        tela.blit(imagem, (x, y))

    def desenhar(self, tela):
        tela.fill((0, 0, 0))

        branco = (255, 255, 255)
        cinza = (150, 150, 150)

        if self.tela_atual == "menu":
            # Logo centralizada
            x_logo = (self.largura - self.logo.get_width()) // 2
            tela.blit(self.logo, (x_logo, 35))

            # Opções do menu
            inicio_y = self.altura // 2 + 35
            espacamento = 42

            self.botoes = []

            for i, opcao in enumerate(self.opcoes):
                prefixo = "> " if i == self.selecionada else "  "
                texto = prefixo + opcao

                cor = branco if i == self.selecionada else cinza
                imagem = self.fonte.render(texto, True, cor)

                x = (self.largura - imagem.get_width()) // 2
                y = inicio_y + i * espacamento

                tela.blit(imagem, (x, y))

                # Área clicável um pouco maior que o texto
                botao = imagem.get_rect(
                    topleft=(x, y)
                ).inflate(40, 14)

                self.botoes.append(botao)

        elif self.tela_atual == "comandos":
            self.desenhar_texto_centralizado(
                tela, "COMANDOS", self.fonte, branco, 100
            )

            comandos = [
                "WASD - MOVIMENTAR",
                "E - INTERAGIR",
                "ESC - VOLTAR",
                "P - PAUSE"
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
                tela, "MATEUS MELO", self.fonte_pequena,
                branco, 240
            )
            self.desenhar_texto_centralizado(
                tela, "ESC - VOLTAR", self.fonte_pequena,
                cinza, self.altura - 70
            )

    def tratar_evento(self, evento):
        if self.tela_atual == "menu":

            # Navegação pelo teclado
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_UP, pygame.K_w):
                    self.selecionada = (
                        self.selecionada - 1
                    ) % len(self.opcoes)

                elif evento.key in (pygame.K_DOWN, pygame.K_s):
                    self.selecionada = (
                        self.selecionada + 1
                    ) % len(self.opcoes)

                elif evento.key == pygame.K_RETURN:
                    return self.executar_opcao(
                        self.opcoes[self.selecionada]
                    )

            # Destaca a opção sob o cursor
            elif evento.type == pygame.MOUSEMOTION:
                for i, botao in enumerate(self.botoes):
                    if botao.collidepoint(evento.pos):
                        self.selecionada = i
                        break

            # Executa a opção clicada
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    for i, botao in enumerate(self.botoes):
                        if botao.collidepoint(evento.pos):
                            self.selecionada = i
                            return self.executar_opcao(
                                self.opcoes[i]
                            )

        else:
            if (
                evento.type == pygame.KEYDOWN
                and evento.key == pygame.K_ESCAPE
            ):
                self.tela_atual = "menu"

        return None

    def executar_opcao(self, opcao):
        if opcao == "JOGAR":
            return "jogar"

        elif opcao == "COMANDOS":
            self.tela_atual = "comandos"

        elif opcao == "CRÉDITOS":
            self.tela_atual = "creditos"

        elif opcao == "SAIR":
            return "sair"

        return None
