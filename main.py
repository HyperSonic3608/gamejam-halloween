import pygame

from personagem import Personagem
from cenarios.quarto import Quarto
from cenarios.exterior import Exterior
from cenarios.militar import Militar
from cenarios.propaganda import Propaganda
from cenarios.residencial import Residencial
from cenarios.puzzle import Puzzle
from cenarios.cadeado import Cadeado
from cenarios.caca_palavras import CacaPalavras
from cenarios.corredor_final import CorredorFinal


pygame.init()

# ==================================================
# JANELA
# ==================================================

LARGURA_TELA = 1600
ALTURA_TELA = 900

tela = pygame.display.set_mode(
    (LARGURA_TELA, ALTURA_TELA)
)

pygame.display.set_caption("Meu Jogo")

clock = pygame.time.Clock()


# ==================================================
# FONTES
# ==================================================

fonte_dialogo = pygame.font.SysFont("monospace", 22, bold=True)
fonte_nome = pygame.font.SysFont("monospace", 18, bold=True)
fonte_fim = pygame.font.SysFont("monospace", 48, bold=True)
fonte_instrucao = pygame.font.SysFont("monospace", 22, bold=True)

# ==================================================
# IMAGENS DA CENA FINAL
# ==================================================

imagem_final_0 = pygame.image.load(
    "sprites/cena_final/sprite_0.png"
).convert()

imagem_final_1 = pygame.image.load(
    "sprites/cena_final/sprite_1.png"
).convert()

imagem_final_0 = pygame.transform.scale(
    imagem_final_0,
    (LARGURA_TELA, ALTURA_TELA)
)

imagem_final_1 = pygame.transform.scale(
    imagem_final_1,
    (LARGURA_TELA, ALTURA_TELA)
)

imagens_finais = [
    imagem_final_0,
    imagem_final_1
]

tempo_animacao_final = 0.0
indice_imagem_final = 0


# ==================================================
# CENÁRIOS
# ==================================================

quarto = Quarto()
exterior = Exterior()
militar = Militar()
propaganda = Propaganda()
residencial = Residencial()
puzzle = Puzzle()
corredor_final = CorredorFinal()

cadeado = Cadeado()
caca_palavras = CacaPalavras()


# ==================================================
# PAINEL DO CADEADO E CAÇA-PALAVRAS
# ==================================================

LARGURA_PAINEL = 1100
ALTURA_PAINEL = 650

painel_puzzle = pygame.Surface(
    (LARGURA_PAINEL, ALTURA_PAINEL)
)

posicao_painel = pygame.Rect(
    (LARGURA_TELA - LARGURA_PAINEL) // 2,
    (ALTURA_TELA - ALTURA_PAINEL) // 2,
    LARGURA_PAINEL,
    ALTURA_PAINEL
)


# ==================================================
# PORTAS E ÁREAS DE INTERAÇÃO
# ==================================================

porta_externa = pygame.Rect(130, 350, 160, 200)
porta_militar = pygame.Rect(980, 380, 100, 60)
porta_propaganda = pygame.Rect(250, 1290, 100, 60)
porta_residencial = pygame.Rect(1500, 1360, 100, 60)

porta_puzzle_exterior = pygame.Rect(
    2240, 1330, 180, 140
)


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

tela_laika_aberta = False
carta_laika_aberta = False


# ==================================================
# ESTADOS DO CADEADO E DO FINAL
# ==================================================

tela_cadeado_aberta = False
porta_azul_desbloqueada = False

final_iniciado = False

etapa_final = "corredor"
tempo_etapa_final = 0.0
opacidade_sala = 0
dialogo_atual = 0
tempo_dialogo = 0.0

# Duração da transição para a tela final.
tempo_transicao_fim = 0.0
DURACAO_TRANSICAO_FIM = 3.0

dialogos_finais = [
    ("Maria", "Você dormiu de novo assistindo a esse documentário?"),
    ("Maria", "Anda, Ivan! Você vai perder o Halloween!"),
]


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
    global tela_cadeado_aberta

    cenario_atual = cenario

    carta_aberta = False
    carta_propaganda_aberta = False
    carta_militar_aberta = False
    carta_ritual_aberta = False

    tela_laika_aberta = False
    carta_laika_aberta = False
    tela_cadeado_aberta = False

    personagem.paredes = cenario.paredes
    personagem.rect.topleft = posicao

    atualizar_hitbox()


def sair_para_exterior(posicao):
    if final_iniciado:
        return

    entrar_no_cenario(exterior, posicao)


def entrar_no_corredor_final():
    global final_iniciado
    global etapa_final
    global tempo_etapa_final

    if final_iniciado or personagem is None:
        return

    final_iniciado = True
    etapa_final = "corredor"
    tempo_etapa_final = 0.0

    entrar_no_cenario(
        corredor_final,
        (280, 340)
    )

    corredor_final.iniciar(personagem)


# ==================================================
# DIÁLOGOS FINAIS
# ==================================================

def desenhar_dialogo_final(superficie, nome, texto):
    altura_caixa = 175
    y = ALTURA_TELA - altura_caixa - 35

    pygame.draw.rect(
        superficie,
        (12, 12, 15),
        (100, y, LARGURA_TELA - 200, altura_caixa),
    )

    pygame.draw.rect(
        superficie,
        (255, 255, 255),
        (100, y, LARGURA_TELA - 200, altura_caixa),
        3,
    )

    texto_nome = fonte_nome.render(
        nome,
        True,
        (225, 195, 135)
    )

    superficie.blit(texto_nome, (140, y + 22))

    palavras = texto.split()
    linhas = []
    linha_atual = ""

    largura_maxima = LARGURA_TELA - 300

    for palavra in palavras:
        tentativa = (
            palavra if not linha_atual
            else linha_atual + " " + palavra
        )

        if fonte_dialogo.size(tentativa)[0] <= largura_maxima:
            linha_atual = tentativa
        else:
            linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    for indice, linha in enumerate(linhas):
        imagem_texto = fonte_dialogo.render(
            linha,
            True,
            (240, 237, 228)
        )

        superficie.blit(
            imagem_texto,
            (140, y + 65 + indice * 38)
        )


# ==================================================
# LOOP PRINCIPAL
# ==================================================

rodando = True

while rodando:

    dt = min(clock.tick(60) / 1000, 0.05)

    # ==================================================
    # EVENTOS
    # ==================================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False
            continue

        if final_iniciado:
            continue

        # ------------------------------------------
        # CADEADO E CAÇA-PALAVRAS
        # ------------------------------------------

        if tela_cadeado_aberta:

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    tela_cadeado_aberta = False
                else:
                    cadeado.tratar_evento(evento)

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                posicao_local = (
                    evento.pos[0] - posicao_painel.x,
                    evento.pos[1] - posicao_painel.y
                )

                evento_painel = pygame.event.Event(
                    pygame.MOUSEBUTTONDOWN,
                    {
                        "pos": posicao_local,
                        "button": evento.button
                    }
                )

                cadeado.tratar_evento(evento_painel)

            continue

        # ESC: fechar telas
        if (
            evento.type == pygame.KEYDOWN
            and evento.key == pygame.K_ESCAPE
        ):

            if carta_laika_aberta:
                carta_laika_aberta = False

            elif tela_laika_aberta:
                tela_laika_aberta = False

        # Interações com E
        if not (
            evento.type == pygame.KEYDOWN
            and evento.key == pygame.K_e
        ):
            continue

        # ==========================================
        # EXTERIOR
        # ==========================================

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

            elif personagem.hitbox.colliderect(porta_externa):
                entrar_no_cenario(quarto, (270, 300))

            elif personagem.hitbox.colliderect(porta_militar):
                entrar_no_cenario(militar, (290, 300))

            elif personagem.hitbox.colliderect(porta_propaganda):
                entrar_no_cenario(propaganda, (290, 300))

            elif personagem.hitbox.colliderect(porta_residencial):
                entrar_no_cenario(residencial, (290, 300))

            elif personagem.hitbox.colliderect(porta_puzzle_exterior):
                entrar_no_cenario(puzzle, (290, 300))

        # ==========================================
        # RESIDENCIAL
        # ==========================================

        elif cenario_atual == residencial and personagem is not None:

            if carta_aberta:
                carta_aberta = False

            elif residencial.personagem_perto_da_mesa(personagem):
                carta_aberta = True

            elif residencial.personagem_perto_da_porta(personagem):
                sair_para_exterior((1500, 1350))

        # ==========================================
        # QUARTO
        # ==========================================

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

        # ==========================================
        # PRÉDIO MILITAR
        # ==========================================

        elif cenario_atual == militar and personagem is not None:

            if carta_militar_aberta:
                carta_militar_aberta = False

            elif militar.personagem_perto_da_mesa(personagem):
                carta_militar_aberta = True

            elif militar.personagem_perto_da_porta(personagem):
                sair_para_exterior((1000, 350))

        # ==========================================
        # PRÉDIO DA PROPAGANDA
        # ==========================================

        elif cenario_atual == propaganda and personagem is not None:

            if carta_propaganda_aberta:
                carta_propaganda_aberta = False

            elif propaganda.personagem_perto_da_mesa(personagem):
                carta_propaganda_aberta = True

            elif propaganda.personagem_perto_da_porta(personagem):
                sair_para_exterior((180, 900))

        # ==========================================
        # PUZZLE
        # ==========================================

        elif cenario_atual == puzzle and personagem is not None:

            if (
                not porta_azul_desbloqueada
                and puzzle.personagem_perto_da_porta_azul(personagem)
            ):
                cadeado.reiniciar()
                tela_cadeado_aberta = True

            elif puzzle.personagem_perto_da_porta_final(personagem):
                entrar_no_corredor_final()

            elif puzzle.personagem_perto_da_porta(personagem):
                sair_para_exterior((2250, 1320))

    # ==================================================
    # ATUALIZAR ESTADO DO CADEADO
    # ==================================================

    if cadeado.resolvido:
        porta_azul_desbloqueada = True
        puzzle.desbloquear_porta_final()

    # ==================================================
    # SEQUÊNCIA AUTOMÁTICA DO FINAL
    # ==================================================

    if final_iniciado:

        tempo_etapa_final += dt

        if etapa_final == "corredor":

            grupo_personagem.update()
            atualizar_hitbox()

            corredor_final.atualizar(personagem, dt)

            if corredor_final.escurecimento_concluido:
                etapa_final = "chamada"
                tempo_etapa_final = 0.0

        elif etapa_final == "chamada":

            if tempo_etapa_final >= 3.5:
                etapa_final = "despertar"
                tempo_etapa_final = 0.0
                opacidade_sala = 0

        elif etapa_final == "despertar":

            opacidade_sala = min(
                255,
                int((tempo_etapa_final / 3.5) * 255)
            )

            # A animação começa assim que a cena começa a ganhar cor.
            tempo_animacao_final += dt

            if tempo_animacao_final >= 0.5:
                tempo_animacao_final = 0.0
                indice_imagem_final = 1 - indice_imagem_final

            if tempo_etapa_final >= 3.5:
                etapa_final = "dialogo"
                tempo_etapa_final = 0.0
                dialogo_atual = 0
                tempo_dialogo = 0.0

        elif etapa_final == "dialogo":

            # Continua alternando as artes durante os diálogos.
            tempo_animacao_final += dt

            if tempo_animacao_final >= 0.5:
                tempo_animacao_final = 0.0
                indice_imagem_final = 1 - indice_imagem_final

            tempo_dialogo += dt

            duracao_dialogo = [5.0, 4.5]

            if tempo_dialogo >= duracao_dialogo[dialogo_atual]:

                dialogo_atual += 1
                tempo_dialogo = 0.0

                if dialogo_atual >= len(dialogos_finais):
                    etapa_final = "fim"
                    tempo_etapa_final = 0.0
                    tempo_transicao_fim = 0.0

        elif etapa_final == "fim":

            # Aumenta gradualmente o escurecimento.
            tempo_transicao_fim = min(
                tempo_transicao_fim + dt,
                DURACAO_TRANSICAO_FIM
            )

    # ==================================================
    # ATUALIZAÇÃO NORMAL DO PERSONAGEM
    # ==================================================

    pode_atualizar_personagem = (
        personagem is not None
        and not final_iniciado
        and not tela_cadeado_aberta
        and not carta_aberta
        and not carta_propaganda_aberta
        and not carta_militar_aberta
        and not carta_ritual_aberta
        and not tela_laika_aberta
        and not carta_laika_aberta
    )

    if pode_atualizar_personagem:
        grupo_personagem.update()
        atualizar_hitbox()

    # ==================================================
    # DESENHO DO CENÁRIO NORMAL
    # ==================================================

    if not final_iniciado:

        if cenario_atual == exterior:

            if tela_laika_aberta:

                exterior.desenhar_tela_laika(tela)

                if carta_laika_aberta:
                    exterior.desenhar_carta_laika(tela)

            else:

                camera_x = (
                    personagem.rect.centerx - LARGURA_TELA // 2
                )

                camera_y = (
                    personagem.rect.centery - ALTURA_TELA // 2
                )

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

            # Instrução inicial para levantar da cama
            if cenario_atual == quarto and not quarto.acordou:

                texto = fonte_instrucao.render(
                    "Aperte E para levantar",
                    False,
                    (255, 255, 255)
                )

                x = (LARGURA_TELA - texto.get_width()) // 2
                y = ALTURA_TELA - 80

                tela.blit(texto,(x, y))

            # Instrução para sair pela porta
            if (
                cenario_atual == quarto
                and quarto.acordou
                and personagem is not None
                and quarto.personagem_perto_da_porta(personagem)
            ):
                texto = fonte_instrucao.render(
                    "aperte E na porta para sair",
                    False,
                    (255, 255, 255)
                )

                x = (LARGURA_TELA - texto.get_width()) // 2
                y = ALTURA_TELA - 80

                tela.blit(texto, (x, y))

        # Cartas
        if cenario_atual == residencial and carta_aberta:
            residencial.desenhar_carta(tela)

        if cenario_atual == propaganda and carta_propaganda_aberta:
            propaganda.desenhar_carta(tela)

        if cenario_atual == militar and carta_militar_aberta:
            militar.desenhar_carta(tela)

        # Painel do cadeado e caça-palavras
        if tela_cadeado_aberta:

            painel_puzzle.fill((185, 180, 163))

            pygame.draw.rect(
                painel_puzzle,
                (0, 0, 0),
                painel_puzzle.get_rect(),
                5
            )

            cadeado.desenhar(painel_puzzle)

            caca_palavras.desenhar_na_tela(
                painel_puzzle,
                x_grade=600,
                y_grade=170,
                tamanho_celula=50
            )

            tela.blit(
                painel_puzzle,
                posicao_painel.topleft
            )

    # ==================================================
    # DESENHO DA SEQUÊNCIA FINAL
    # ==================================================

    else:

        if etapa_final in ("corredor", "chamada"):

            if etapa_final == "corredor":

                camera_x = max(
                    0,
                    personagem.rect.centerx - LARGURA_TELA // 2
                )

                corredor_final.desenhar(tela, camera_x)

                tela.blit(
                    personagem.image,
                    (
                        personagem.rect.x - camera_x,
                        personagem.rect.y
                    )
                )

                tela.blit(
                    corredor_final.tela_preta,
                    (0, 0)
                )

            else:
                tela.fill((0, 0, 0))

            if etapa_final == "chamada":
                desenhar_dialogo_final(
                    tela,
                    "Maria",
                    "Ivan... Ivan..."
                )

        elif etapa_final == "despertar":

            # Usa a arte em vez da sala antiga desenhada no Pygame.
            tela.blit(
                imagens_finais[indice_imagem_final],
                (0, 0)
            )

            # Efeito de aparecimento durante o despertar.
            camada_escura = pygame.Surface(
                (LARGURA_TELA, ALTURA_TELA)
            )

            camada_escura.fill((0, 0, 0))

            camada_escura.set_alpha(
                255 - opacidade_sala
            )

            tela.blit(camada_escura, (0, 0))

        elif etapa_final == "dialogo":

            # Exibe a arte animada durante os diálogos.
            tela.blit(
                imagens_finais[indice_imagem_final],
                (0, 0)
            )

            nome, texto = dialogos_finais[dialogo_atual]

            desenhar_dialogo_final(
                tela,
                nome,
                texto
            )

        elif etapa_final == "fim":

            # Progresso da transição: 0.0 até 1.0.
            progresso = min(
                tempo_transicao_fim / DURACAO_TRANSICAO_FIM,
                1.0
            )

            # Desenha a imagem de fundo.
            tela.blit(
                imagens_finais[indice_imagem_final],
                (0, 0)
            )

            # A imagem escurece progressivamente.
            camada_escura = pygame.Surface(
                (LARGURA_TELA, ALTURA_TELA)
            )

            camada_escura.fill((0, 0, 0))

            camada_escura.set_alpha(
                int(255 * progresso)
            )

            tela.blit(
                camada_escura,
                (0, 0)
            )

            # O texto FIM aparece gradualmente.
            texto_fim = fonte_fim.render(
                "FIM",
                True,
                (255, 255, 255)
            )

            texto_fim.set_alpha(
                int(255 * progresso)
            )

            retangulo_fim = texto_fim.get_rect(
                center=(
                    LARGURA_TELA // 2,
                    ALTURA_TELA // 2
                )
            )

            tela.blit(
                texto_fim,
                retangulo_fim
            )

    # ==================================================
    # FINALIZAÇÃO
    # ==================================================

    pygame.display.flip()


pygame.quit()