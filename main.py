import pygame
from personagem import Personagem
from cenarios.quarto import Quarto
from cenarios.exterior import Exterior

pygame.init()

#janela
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Meu Jogo")

quarto = Quarto()
exterior = Exterior()
cenario_atual = quarto
personagem = Personagem(cenario_atual.paredes)

#sprites
grupo_personagem = pygame.sprite.Group()
grupo_personagem.add(personagem)

rodando = True
clock = pygame.time.Clock()

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e:
                if quarto.personagem_perto_da_porta(personagem):
                    cenario_atual = exterior

                    personagem.paredes = exterior.paredes

                    personagem.rect.topleft = (100, 200)
                    personagem.hitbox.x = personagem.rect.x + 40
                    personagem.hitbox.y = personagem.rect.y + 90

    grupo_personagem.update()

    if cenario_atual == exterior:
        #posição da câmera
        camera_x = personagem.rect.centerx - 640 // 2
        camera_y = personagem.rect.centery - 480 // 2

        camera_x = max(0, min(camera_x, exterior.LARGURA - 640))
        camera_y = max(0, min(camera_y, exterior.ALTURA - 480))

        #desenha mapa
        cenario_atual.desenhar(tela, camera_x, camera_y)

        #personagem na posição relativa à câmera
        tela.blit(
            personagem.image,
            (personagem.rect.x - camera_x,
            personagem.rect.y - camera_y)
        )

    else:
        cenario_atual.desenhar(tela)
        grupo_personagem.draw(tela)

    pygame.display.flip()


    clock.tick(60)

pygame.quit()