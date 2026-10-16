import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, paredes):
        pygame.sprite.Sprite.__init__(self)
        self.paredes = paredes
        self.sprites_respirando = []
        self.sprites_respirando.append(pygame.image.load("sprites/sprites_respirando/sprite_0.png"))
        self.sprites_respirando.append(pygame.image.load("sprites/sprites_respirando/sprite_1.png"))
        self.sprites_andando = []
        self.sprites_andando.append(pygame.image.load("sprites/sprites_andando_direita/sprite_0.png"))
        self.sprites_andando.append(pygame.image.load("sprites/sprites_andando_direita/sprite_1.png"))
        self.sprites_andando_cima = []
        self.sprites_andando_cima.append(pygame.image.load("sprites/sprites_andando_cima/sprite_0.png"))
        self.sprites_andando_cima.append(pygame.image.load("sprites/sprites_andando_cima/sprite_1.png"))
        self.sprites_andando_baixo = []
        self.sprites_andando_baixo.append(pygame.image.load("sprites/sprites_andando_baixo/sprite_0.png"))
        self.sprites_andando_baixo.append(pygame.image.load("sprites/sprites_andando_baixo/sprite_1.png"))
        self.atual = 0
        self.andando = False
        self.image = self.sprites_respirando[self.atual]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))

        #hitbox
        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 50

        self.hitbox = pygame.Rect(
            self.rect.x + 40,
            self.rect.y + 90,
            48,
            30
        )


    def update(self):
    #MOVIMENTACAO DO PERSONAGEM
        teclas = pygame.key.get_pressed()
        velocidade = 9
        andando = False
        direcao = "direita"

        movimento_x = 0
        movimento_y = 0

        if teclas[pygame.K_w]:
            movimento_y -= velocidade
            andando = True
            direcao = "cima"

        if teclas[pygame.K_s]:
            movimento_y += velocidade
            andando = True
            direcao = "baixo"

        if teclas[pygame.K_a]:
            movimento_x -= velocidade
            andando = True
            direcao = "esquerda"

        if teclas[pygame.K_d]:
            movimento_x += velocidade
            andando = True
            direcao = "direita"

        self.rect.x += movimento_x

        self.hitbox.x =self.rect.x + 40
        self.hitbox.y = self.rect.y + 90

        for parede in self.paredes:
            if self.hitbox.colliderect(parede):
                self.rect.x -= movimento_x
                self.hitbox.x = self.rect.x +40

        self.rect.y += movimento_y
        
        self.hitbox.x =self.rect.x + 40
        self.hitbox.y = self.rect.y + 90
        
        for parede in self.paredes:
            if self.hitbox.colliderect(parede):
                self.rect.y -= movimento_y
                self.hitbox.y = self.rect.y + 90

        if andando:
            if not self.andando:
                self.atual = 0

            self.atual = self.atual + 0.05

            if direcao == "cima":
                if self.atual >= len(self.sprites_andando_cima):
                    self.atual = 0

                self.image = self.sprites_andando_cima[int(self.atual)]

            elif direcao == "baixo":

                if self.atual >= len(self.sprites_andando_baixo):
                    self.atual = 0

                self.image = self.sprites_andando_baixo[int(self.atual)]

            else:

                if self.atual >= len(self.sprites_andando):
                    self.atual = 0

                imagem = self.sprites_andando[int(self.atual)]

                if direcao == "esquerda":
                    self.image = pygame.transform.flip(imagem, True, False)
                else:
                    self.image = imagem

        else:
            if self.andando:
                self.atual = 0

            self.atual = self.atual + 0.030

            if self.atual >= len(self.sprites_respirando):
                self.atual = 0

            self.image = self.sprites_respirando[int(self.atual)]

        self.andando = andando

        self.image = pygame.transform.scale(self.image, (32 * 4, 32 * 4))

        