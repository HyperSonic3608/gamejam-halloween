
import pygame


class Puzzle:
    def __init__(self):
        # Porta azul que abre o cadeado
        self.porta = pygame.Rect(296, 210, 48, 48)

        self.sprite_passagem = pygame.image.load(
            "sprites/sprite_passagem/sprite_0.png"
        ).convert_alpha()

        self.sprite_passagem = pygame.transform.scale(
            self.sprite_passagem,
            (105, 105)
        )

        # Saída inferior original
        self.saida = pygame.Rect(290, 400, 60, 48)
        self.area_interacao_saida = self.saida.inflate(100, 60)

        # Nova porta na parede direita
        self.porta_final = pygame.Rect(592, 205, 48, 70)
        self.area_interacao_porta_final = (
            self.porta_final.inflate(100, 60)
        )

        # Estado da nova porta
        self.porta_final_desbloqueada = False

        # Paredes do cenário
        self.paredes = [
            pygame.Rect(0, 0, 640, 32),
            pygame.Rect(0, 448, 290, 32),
            pygame.Rect(350, 448, 290, 32),
            pygame.Rect(0, 0, 32, 480),
            pygame.Rect(608, 0, 32, 480)
        ]

    def desbloquear_porta_final(self):
        self.porta_final_desbloqueada = True

    def desenhar(self, tela):
        tela.fill((55, 50, 45))

        # Paredes
        for parede in self.paredes:
            pygame.draw.rect(
                tela,
                (100, 100, 100),
                parede
            )

        # Porta azul original
        tela.blit(
            self.sprite_passagem,
            self.porta.topleft
        )

        # Nova porta na parede direita
        if self.porta_final_desbloqueada:
            pygame.draw.rect(
                tela,
                (25, 65, 115),
                self.porta_final
            )

            pygame.draw.rect(
                tela,
                (0, 0, 0),
                self.porta_final,
                4
            )

            # Maçaneta
            pygame.draw.rect(
                tela,
                (185, 180, 163),
                (
                    self.porta_final.x + 8,
                    self.porta_final.y + 35,
                    6,
                    6
                )
            )

    def personagem_perto_da_porta(self, personagem):
        # Saída inferior original
        return personagem.hitbox.colliderect(
            self.area_interacao_saida
        )

    def personagem_perto_da_porta_azul(self, personagem):
        area_interacao = self.porta.inflate(100, 80)

        return personagem.hitbox.colliderect(
            area_interacao
        )

    def personagem_perto_da_porta_final(self, personagem):
        if not self.porta_final_desbloqueada:
            return False

        return personagem.hitbox.colliderect(
            self.area_interacao_porta_final
        )
