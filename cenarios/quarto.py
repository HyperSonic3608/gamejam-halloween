
import pygame


class Quarto:
    def __init__(self):
        # PORTA
        self.porta = pygame.Rect(290, 448, 60, 32)

        # PAREDES E COLISÕES
        self.paredes = [
            pygame.Rect(0, 0, 640, 32),
            pygame.Rect(0, 448, 290, 32),
            pygame.Rect(350, 448, 290, 32),
            pygame.Rect(0, 0, 32, 480),
            pygame.Rect(608, 0, 32, 480)
        ]

        # CHÃO E TAPETE
        self.tapete = pygame.Rect(180, 180, 280, 150)

        # SPRITES DA CAMA
        self.sprites_cama = [
            pygame.image.load(
                "sprites/sprite_cama/sprite_0.png"
            ).convert_alpha(),

            pygame.image.load(
                "sprites/sprite_cama/sprite_1.png"
            ).convert_alpha(),

            pygame.image.load(
                "sprites/sprite_cama/sprite_2.png"
            ).convert_alpha()
        ]

        # ESTADO DA INTRODUÇÃO
        self.acordou = False
        self.indice_cama = 0

        # CONTROLE DA ANIMAÇÃO
        self.tempo_animacao = 0
        self.intervalo_animacao = 30

        # POSIÇÃO E TAMANHO DA CAMA
        self.cama_x = 25
        self.cama_y = 100
        self.escala_cama = 5

    # ACORDAR
    def acordar(self):
        if not self.acordou:
            self.acordou = True
            self.indice_cama = 2
            self.tempo_animacao = 0

    # DESENHAR CHÃO
    def desenhar_chao(self, tela):
        tela.fill((105, 75, 52))

        # Tábuas de madeira
        for y in range(40, 448, 32):
            pygame.draw.line(
                tela,
                (80, 55, 40),
                (32, y),
                (608, y),
                2
            )

    # DESENHAR TAPETE
    def desenhar_tapete(self, tela):
        pygame.draw.rect(
            tela,
            (110, 35, 30),
            self.tapete
        )

        pygame.draw.rect(
            tela,
            (190, 145, 90),
            self.tapete,
            4
        )

        pygame.draw.line(
            tela,
            (190, 145, 90),
            (self.tapete.left + 20, self.tapete.centery),
            (self.tapete.right - 20, self.tapete.centery),
            2
        )

    # ATUALIZAR ANIMAÇÃO DA CAMA
    def atualizar_cama(self):
        if self.acordou:
            return

        self.tempo_animacao += 1

        if self.tempo_animacao >= self.intervalo_animacao:
            self.tempo_animacao = 0
            self.indice_cama = 1 - self.indice_cama

    # DESENHAR CAMA
    def desenhar_cama(self, tela):
        sprite = self.sprites_cama[self.indice_cama]

        largura = sprite.get_width() * self.escala_cama
        altura = sprite.get_height() * self.escala_cama

        sprite_ampliado = pygame.transform.scale(
            sprite,
            (largura, altura)
        )

        tela.blit(
            sprite_ampliado,
            (self.cama_x, self.cama_y)
        )

    # DESENHAR PAREDES
    def desenhar_paredes(self, tela):
        for parede in self.paredes:
            pygame.draw.rect(
                tela,
                (100, 100, 100),
                parede
            )

    # DESENHAR CENÁRIO COMPLETO
    def desenhar(self, tela):
        self.desenhar_chao(tela)
        self.desenhar_tapete(tela)
        self.atualizar_cama()
        self.desenhar_cama(tela)
        self.desenhar_paredes(tela)

    # VERIFICAR PROXIMIDADE DA PORTA
    def personagem_perto_da_porta(self, personagem):
        area_interacao = self.porta.inflate(100, 100)

        return personagem.hitbox.colliderect(
            area_interacao
        )
