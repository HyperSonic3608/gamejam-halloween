
import pygame
import random


class Residencial:
    def __init__(self):
        self.porta = pygame.Rect(290, 448, 60, 32)

        self.paredes = [
            pygame.Rect(0, 0, 640, 32),
            pygame.Rect(0, 448, 290, 32),
            pygame.Rect(350, 448, 290, 32),
            pygame.Rect(0, 0, 32, 480),
            pygame.Rect(608, 0, 32, 480)
        ]

        self.sprite_mesa = pygame.image.load(
            "sprites/sprite_mesa/sprite_0.png"
        ).convert_alpha()

        self.escala_mesa = 3

        largura = self.sprite_mesa.get_width() * self.escala_mesa
        altura = self.sprite_mesa.get_height() * self.escala_mesa

        self.mesa = pygame.transform.scale(
            self.sprite_mesa,
            (largura, altura)
        )

        self.mesa_x = 150
        self.mesa_y = 100

        self.area_mesa = pygame.Rect(
            self.mesa_x,
            self.mesa_y,
            largura,
            altura
        ).inflate(50, 50)

        self.sprite_pista = pygame.image.load(
            "sprites/pista_abobora/sprite_0.png"
        ).convert_alpha()

        self.escala_pista = 3

        largura_pista = (
            self.sprite_pista.get_width() * self.escala_pista
        )
        altura_pista = (
            self.sprite_pista.get_height() * self.escala_pista
        )

        self.pista_abobora = pygame.transform.scale(
            self.sprite_pista,
            (largura_pista, altura_pista)
        )

        self.texto_carta = [
            "Você finalmente chegou.",
            "",
            "Moscou já não pertence aos vivos.",
            "Nesta noite, o Halloween não é",
            "uma celebração, mas um aviso.",
            "",
            "Quando as luzes se apagarem,",
            "procure a abóbora.",
            "",
            "E nao confie no que vier",
            "depois dela.",
            "",
            "Eu estarei observando."
        ]

        self.fonte_carta = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 30
        )
        self.fonte_titulo = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 36
        )
        self.fonte_instrucao = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 23
        )

        gerador = random.Random(12)

        self.desvios_texto = [
            gerador.randint(-3, 3) for _ in self.texto_carta
        ]

        self.desvios_altura = [
            gerador.randint(-1, 2) for _ in self.texto_carta
        ]

    def personagem_perto_da_mesa(self, personagem):
        return personagem.hitbox.colliderect(self.area_mesa)

    def desenhar(self, tela):
        tela.fill((55, 50, 45))

        tela.blit(self.mesa, (self.mesa_x, self.mesa_y))

        for parede in self.paredes:
            pygame.draw.rect(tela, (100, 100, 100), parede)

    def desenhar_carta(self, tela):
        sombra = pygame.Surface(tela.get_size())
        sombra.set_alpha(175)
        sombra.fill((15, 13, 12))
        tela.blit(sombra, (0, 0))

        largura = 600
        altura = 620

        x = (tela.get_width() - largura) // 2
        y = (tela.get_height() - altura) // 2

        pontos = [
            (x + 3, y + 1),
            (x + largura - 5, y + 3),
            (x + largura, y + altura - 4),
            (x + largura - 4, y + altura),
            (x + 2, y + altura - 2),
            (x - 2, y + 6)
        ]

        pontos_sombra = [
            (px + 7, py + 8) for px, py in pontos
        ]

        pygame.draw.polygon(
            tela, (18, 15, 13), pontos_sombra
        )

        pygame.draw.polygon(
            tela, (211, 199, 169), pontos
        )

        pygame.draw.lines(
            tela,
            (130, 115, 87),
            True,
            pontos,
            2
        )

        tinta = (0, 0, 0)

        titulo = self.fonte_titulo.render(
            "Спокойной ночи",
            False,
            tinta
        )

        tela.blit(titulo, (x + 38, y + 35))

        pygame.draw.line(
            tela,
            (145, 128, 99),
            (x + 38, y + 82),
            (x + 210, y + 83),
            1
        )

        pos_y = y + 110

        for indice, linha in enumerate(self.texto_carta):
            if linha == "":
                pos_y += 16
                continue

            texto = self.fonte_carta.render(
                linha,
                False,
                tinta
            )

            tela.blit(
                texto,
                (
                    x + 38 + self.desvios_texto[indice],
                    pos_y + self.desvios_altura[indice]
                )
            )

            pos_y += 32

        tela.blit(
            self.pista_abobora,
            (x + 38, y + 440)
        )

        instrucao = self.fonte_instrucao.render(
            "[ E ] fechar",
            False,
            (0, 0, 0)
        )

        tela.blit(
            instrucao,
            (
                x + largura - instrucao.get_width() - 24,
                y + altura - 38
            )
        )

    def personagem_perto_da_porta(self, personagem):
        area_interacao = self.porta.inflate(100, 100)

        return personagem.hitbox.colliderect(area_interacao)
