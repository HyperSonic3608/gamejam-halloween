
import pygame


class CorredorFinal:
    def __init__(self):
        self.altura = 900
        self.largura_tela = 1600

        # Limites superior e inferior.
        # Não existe parede fechando o corredor à direita.
        self.paredes = [
            pygame.Rect(-1000000000, 0, 2000000000, 80),
            pygame.Rect(-1000000000, 820, 2000000000, 80),
        ]

        # Configuração do escurecimento.
        self.distancia_inicio = 0
        self.distancia_para_escurecer = 2400
        self.opacidade = 0
        self.opacidade_maxima = 255
        self.escurecimento_concluido = False

        # Camada preta do tamanho da janela.
        info_tela = pygame.display.Info()

        self.tela_preta = pygame.Surface(
            (info_tela.current_w, info_tela.current_h)
        )
        self.tela_preta.fill((0, 0, 0))
        self.tela_preta.set_alpha(0)

        # Cores do cenário.
        self.cor_chao = (48, 45, 40)
        self.cor_parede = (76, 72, 64)
        self.cor_detalhe = (93, 87, 75)

    def iniciar(self, personagem):
        """Reinicia o corredor e o escurecimento."""
        self.distancia_inicio = personagem.rect.x
        self.opacidade = 0
        self.escurecimento_concluido = False
        self.tela_preta.set_alpha(0)

    def atualizar(self, personagem, dt):
        """Escurece a tela conforme Ivan caminha para a direita."""
        if self.escurecimento_concluido:
            return

        distancia = personagem.rect.x - self.distancia_inicio

        progresso = max(
            0,
            min(1, distancia / self.distancia_para_escurecer)
        )

        self.opacidade = int(
            progresso * self.opacidade_maxima
        )

        self.tela_preta.set_alpha(self.opacidade)

        if self.opacidade >= self.opacidade_maxima:
            self.opacidade = self.opacidade_maxima
            self.escurecimento_concluido = True

    def desenhar(self, tela, camera_x=0):
        """Desenha o corredor horizontal usando a posição da câmera."""
        tela.fill(self.cor_chao)

        largura = tela.get_width()
        altura = tela.get_height()

        # Parede superior.
        pygame.draw.rect(
            tela,
            self.cor_parede,
            (0, 0, largura, 80)
        )

        # Parede inferior.
        pygame.draw.rect(
            tela,
            self.cor_parede,
            (0, altura - 80, largura, 80)
        )

        # Detalhes repetidos para dar continuidade ao corredor.
        inicio = int(camera_x // 160) * 160

        for mundo_x in range(
            inicio,
            inicio + largura + 320,
            160
        ):
            x = mundo_x - camera_x

            # Detalhes na parede superior.
            pygame.draw.rect(
                tela,
                self.cor_detalhe,
                (x, 0, 50, 80)
            )

            # Linha de detalhe próxima ao chão.
            pygame.draw.line(
                tela,
                self.cor_detalhe,
                (x, altura - 120),
                (x + 75, altura - 120),
                2
            )
