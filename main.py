
import pygame

from personagem import Personagem
from cenarios.quarto import Quarto
from cenarios.exterior import Exterior
from cenarios.militar import Militar
from cenarios.propaganda import Propaganda
from cenarios.residencial import Residencial
from cenarios.puzzle import Puzzle


pygame.init()

tela = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Meu Jogo")

clock = pygame.time.Clock()


# ==================================================
# CENÁRIOS
# ==================================================

quarto = Quarto()
exterior = Exterior()
militar = Militar()
propaganda = Propaganda()
residencial = Residencial()
puzzle = Puzzle()


# ==================================================
# PORTAS E ÁREAS DE INTERAÇÃO
# ==================================================

porta_externa = pygame.Rect(130, 350, 160, 200)
porta_militar = pygame.Rect(980, 380, 100, 60)
porta_propaganda = pygame.Rect(250, 1290, 100, 60)
porta_residencial = pygame.Rect(1500, 1360, 100, 60)

# Área invisível para entrar no puzzle pelo exterior.
# Não desenha uma porta nessa posição.
porta_puzzle_exterior = pygame.Rect(2240, 1330, 180, 140)


# ==================================================
# PERSONAGEM
# ==================================================

cenario_atual = quarto
personagem = None

grupo_personagem = pygame.sprite.Group()


# ==================================================
# ESTADOS DAS CARTAS
# ==================================================

carta_aberta = False
carta_propaganda_aberta = False
carta_militar_aberta = False
carta_ritual_aberta = False


# ==================================================
# ESTADOS DA LAIKA
# ==================================================

tela_laika_aberta = False
carta_laika_aberta = False


# ==================================================
# FUNÇÕES AUXILIARES
# ==================================================

def atualizar_hitbox():
    if personagem is not None:
        personagem.hitbox.x = personagem.rect.x + 40
        personagem.hitbox.y = personagem.rect.y + 90


def criar_personagem(posicao, cenario):
    global personagem

    personagem = Personagem(cenario.paredes)
    personagem.rect.topleft = posicao

    atualizar_hitbox()

    grupo_personagem.empty()
    grupo_personagem.add(personagem)


def entrar_no_cenario(cenario, posicao):
    global cenario_atual
    global carta_aberta
    global carta_propaganda_aberta
    global carta_militar_aberta
    global carta_ritual_aberta
    global tela_laika_aberta
    global carta_laika_aberta

    cenario_atual = cenario

    carta_aberta = False
    carta_propaganda_aberta = False
    carta_militar_aberta = False
    carta_ritual_aberta = False

    tela_laika_aberta = False
    carta_laika_aberta = False

    personagem.paredes = cenario.paredes
    personagem.rect.topleft = posicao

    atualizar_hitbox()


def sair_para_exterior(posicao):
    entrar_no_cenario(exterior, posicao)


# ==================================================
# LOOP PRINCIPAL
# ==================================================

rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        # ------------------------------------------
        # ESC: FECHAR CARTA OU TELA DA LAIKA
        # ------------------------------------------

        if (
            evento.type == pygame.KEYDOWN
            and evento.key == pygame.K_ESCAPE
        ):

            if carta_laika_aberta:
                carta_laika_aberta = False

            elif tela_laika_aberta:
                tela_laika_aberta = False

        # ------------------------------------------
        # INTERAÇÕES COM A TECLA E
        # ------------------------------------------

        if (
            evento.type == pygame.KEYDOWN
            and evento.key == pygame.K_e
        ):

            # ======================================
            # EXTERIOR
            # ======================================

            if cenario_atual == exterior and personagem is not None:

                if carta_ritual_aberta:
                    carta_ritual_aberta = False

                elif exterior.personagem_perto_da_mesa(personagem):
                    carta_ritual_aberta = True

                elif carta_laika_aberta:
                    pass

                elif tela_laika_aberta:
                    carta_laika_aberta = True

                elif exterior.personagem_perto_da_laika(personagem):
                    tela_laika_aberta = True

                # Entrar no quarto
                elif personagem.hitbox.colliderect(porta_externa):
                    entrar_no_cenario(quarto, (270, 300))

                # Entrar no prédio militar
                elif personagem.hitbox.colliderect(porta_militar):
                    entrar_no_cenario(militar, (290, 300))

                # Entrar no prédio da propaganda
                elif personagem.hitbox.colliderect(porta_propaganda):
                    entrar_no_cenario(propaganda, (290, 300))

                # Entrar no prédio residencial
                elif personagem.hitbox.colliderect(porta_residencial):
                    entrar_no_cenario(residencial, (290, 300))

                # Entrar no puzzle pela área invisível
                elif personagem.hitbox.colliderect(
                    porta_puzzle_exterior
                ):
                    entrar_no_cenario(puzzle, (290, 300))

            # ======================================
            # RESIDENCIAL
            # ======================================

            elif cenario_atual == residencial and personagem is not None:

                if carta_aberta:
                    carta_aberta = False

                elif residencial.personagem_perto_da_mesa(personagem):
                    carta_aberta = True

                elif residencial.personagem_perto_da_porta(personagem):
                    sair_para_exterior((1500, 1350))

            # ======================================
            # QUARTO
            # ======================================

            elif cenario_atual == quarto:

                if not quarto.acordou:
                    quarto.acordar()

                    criar_personagem(
                        (quarto.cama_x + 200, quarto.cama_y + 100),
                        quarto
                    )

                elif (
                    personagem is not None
                    and quarto.personagem_perto_da_porta(personagem)
                ):
                    sair_para_exterior((180, 400))

            # ======================================
            # PRÉDIO MILITAR
            # ======================================

            elif cenario_atual == militar and personagem is not None:

                if carta_militar_aberta:
                    carta_militar_aberta = False

                elif militar.personagem_perto_da_mesa(personagem):
                    carta_militar_aberta = True

                elif militar.personagem_perto_da_porta(personagem):
                    sair_para_exterior((1000, 350))

            # ======================================
            # PRÉDIO DA PROPAGANDA
            # ======================================

            elif cenario_atual == propaganda and personagem is not None:

                if carta_propaganda_aberta:
                    carta_propaganda_aberta = False

                elif propaganda.personagem_perto_da_mesa(personagem):
                    carta_propaganda_aberta = True

                elif propaganda.personagem_perto_da_porta(personagem):
                    sair_para_exterior((180, 900))

            # ======================================
            # PUZZLE
            # ======================================

            elif cenario_atual == puzzle and personagem is not None:

                # A porta é desenhada dentro de puzzle.py.
                # Pressione E perto dela para sair.
                if puzzle.personagem_perto_da_porta(personagem):
                    sair_para_exterior((2250, 1320))

    # ==================================================
    # ATUALIZAÇÃO DO PERSONAGEM
    # ==================================================

    if (
        personagem is not None
        and not carta_aberta
        and not carta_propaganda_aberta
        and not carta_militar_aberta
        and not carta_ritual_aberta
        and not tela_laika_aberta
        and not carta_laika_aberta
    ):
        grupo_personagem.update()

    # ==================================================
    # DESENHO DOS CENÁRIOS
    # ==================================================

    if cenario_atual == exterior:

        if tela_laika_aberta:

            exterior.desenhar_tela_laika(tela)

            if carta_laika_aberta:
                exterior.desenhar_carta_laika(tela)

        else:

            camera_x = personagem.rect.centerx - tela.get_width() // 2
            camera_y = personagem.rect.centery - tela.get_height() // 2

            exterior.desenhar(tela, camera_x, camera_y)

            tela.blit(
                personagem.image,
                (
                    personagem.rect.x - camera_x,
                    personagem.rect.y - camera_y
                )
            )

            if carta_ritual_aberta:
                exterior.desenhar_carta_ritual(tela)

    else:

        cenario_atual.desenhar(tela)

        if personagem is not None:
            grupo_personagem.draw(tela)

    # ==================================================
    # CARTA DO RESIDENCIAL
    # ==================================================

    if cenario_atual == residencial and carta_aberta:
        residencial.desenhar_carta(tela)

    # ==================================================
    # CARTA DA PROPAGANDA
    # ==================================================

    if cenario_atual == propaganda and carta_propaganda_aberta:
        propaganda.desenhar_carta(tela)

    # ==================================================
    # CARTA MILITAR
    # ==================================================

    if cenario_atual == militar and carta_militar_aberta:
        militar.desenhar_carta(tela)

    # ==================================================
    # FINALIZAÇÃO DO FRAME
    # ==================================================

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

