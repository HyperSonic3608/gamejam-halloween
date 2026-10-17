
import pygame


class Propaganda:
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

        # PISTA DA HORA
        self.pista_hora = pygame.image.load(
            "sprites/pista_hora/sprite_0.png"
        ).convert_alpha()

        self.pista_hora = pygame.transform.scale(
            self.pista_hora,
            (
                self.pista_hora.get_width() * 3,
                self.pista_hora.get_height() * 3
            )
        )

        self.fonte = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 30
        )
        self.fonte_titulo = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 36
        )
        self.fonte_instrucao = pygame.font.Font(
            "C:/Windows/Fonts/arial.ttf", 23
        )

        self.texto_carta = [
            "As ruas estao vazias.",
            "As luzes se apagam uma a uma.",
            "Algo espreita na escuridao."
        ]

    def desenhar(self, tela):
        tela.fill((55, 50, 45))

        tela.blit(self.mesa, (self.mesa_x, self.mesa_y))

        for parede in self.paredes:
            pygame.draw.rect(tela, (100, 100, 100), parede)

    def personagem_perto_da_mesa(self, personagem):
        return personagem.hitbox.colliderect(self.area_mesa)

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

        pygame.draw.polygon(tela, (211, 199, 169), pontos)
        pygame.draw.lines(
            tela, (130, 115, 87), True, pontos, 2
        )

        tinta = (0, 0, 0)

        titulo = self.fonte_titulo.render(
            "Уведомление", False, tinta
        )
        tela.blit(titulo, (x + 38, y + 35))

        pygame.draw.line(
            tela,
            (145, 128, 99),
            (x + 38, y + 82),
            (x + 210, y + 83),
            1
        )

        pos_y = y + 130

        for linha in self.texto_carta:
            texto = self.fonte.render(
                linha, False, tinta
            )
            tela.blit(texto, (x + 38, pos_y))
            pos_y += 42

        mensagem_final = self.fonte_titulo.render(
            "A hora esta chegando.",
            False,
            tinta
        )
        tela.blit(mensagem_final, (x + 38, y + 300))

        # PISTA DA HORA NA CARTA
        tela.blit(
            self.pista_hora,
            (x + 38, y + 365)
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
