
import pygame


class Militar:
    def __init__(self):
        self.porta = pygame.Rect(290, 448, 60, 32)

        self.paredes = [
            pygame.Rect(0, 0, 640, 32),
            pygame.Rect(0, 448, 290, 32),
            pygame.Rect(350, 448, 290, 32),
            pygame.Rect(0, 0, 32, 480),
            pygame.Rect(608, 0, 32, 480)
        ]

        # MESA
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

        # IMAGEM DA PISTA
        self.pista_tuel = pygame.image.load(
            "sprites/pista_tunel/sprite_0.png"
        ).convert_alpha()

        self.escala_pista = 3

        self.pista_tuel = pygame.transform.scale(
            self.pista_tuel,
            (
                self.pista_tuel.get_width() * self.escala_pista,
                self.pista_tuel.get_height() * self.escala_pista
            )
        )

        # FONTES
        self.fonte = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 30
        )
        self.fonte_titulo = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 36
        )
        self.fonte_instrucao = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 23
        )

        # TEXTO DA CARTA
        self.texto_carta = [
            "As patrulhas deixaram de responder.",
            "As ordens foram suspensas apos o",
            "ultimo sinal vindo do subsolo.",
            "Nenhum soldado deve permanecer",
            "proximo as entradas."
        ]

    def desenhar(self, tela):
        tela.fill((55, 50, 45))

        tela.blit(self.mesa, (self.mesa_x, self.mesa_y))

        for parede in self.paredes:
            pygame.draw.rect(
                tela,
                (100, 100, 100),
                parede
            )

    def personagem_perto_da_mesa(self, personagem):
        return personagem.hitbox.colliderect(self.area_mesa)

    def desenhar_carta(self, tela):
        sombra = pygame.Surface(tela.get_size())
        sombra.set_alpha(175)
        sombra.fill((15, 13, 12))
        tela.blit(sombra, (0, 0))

        largura = 700
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

        pygame.draw.polygon(tela, (211, 199, 169), pontos)
        pygame.draw.lines(
            tela, (130, 115, 87), True, pontos, 2
        )

        tinta = (0, 0, 0)

        titulo = self.fonte_titulo.render(
            "ограниченный", False, tinta
        )
        tela.blit(titulo, (x + 38, y + 35))

        pygame.draw.line(
            tela,
            (145, 35, 30),
            (x + 38, y + 88),
            (x + 350, y + 88),
            2
        )

        pos_y = y + 135

        for linha in self.texto_carta:
            texto = self.fonte.render(linha, False, tinta)
            tela.blit(texto, (x + 38, pos_y))
            pos_y += 44

        mensagem_final = self.fonte_titulo.render(
            "O caminho esta abaixo.",
            False,
            tinta
        )
        tela.blit(mensagem_final, (x + 38, y + 400))

        # IMAGEM DA PISTA ABAIXO DA MENSAGEM
        tela.blit(
            self.pista_tuel,
            (x + 38, y + 445)
        )

        instrucao = self.fonte_instrucao.render(
            "[ E ] fechar", False, tinta
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
