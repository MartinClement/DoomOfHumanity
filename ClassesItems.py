__author__ = 'Full'

# -*- coding: Utf-8 -*-

import pygame
from ClassePatterns import *

class Ennemis(pygame.sprite.Sprite):
    def __init__(self,type,spawnX,spawnY,declenchement=0,sens=0,timer=0,powerUp=None):
        pygame.sprite.Sprite.__init__(self)
        self.posX = spawnX
        self.posY = spawnY
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.type = type
        self.time = timer
        self.start = declenchement
        self.animation = 0
        self.powerUp = powerUp
        self.sens = sens
        self.image = pygame.image.load("images/Ennemi"+str(self.type)+"anime"+str(self.animation)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX,self.posY)
        self.arrive = 0
        self.tir = 0
        self.animTir = 0
        if self.type == 1:
            self.hp = 60
        elif self.type == 2:
            self.hp = 200
            self.arriveY = randint(50,250)
        elif self.type == 3:
            self.hp = 160
            self.arriveY = randint(50,150)
            self.sensY = 0
        elif self.type == 5:
            self.hp = 5000
            self.arriveY = randint(50,100)
            self.sensY = 0

    def anim(self):

        if self.animTir:
            if self.time % 3 == 0:
                if self.type == 3:
                    if self.animation < 3:
                        self.animation += 1
                    else:
                        self.animTir = 0
                        self.animation =0
                if self.type == 2:
                    if self.animation < 2:
                        self.animation += 1
                    else:
                        self.animTir = 0
                        self.animation =0
            self.time += 1
            self.image = pygame.image.load("images/Ennemi"+str(self.type)+"anime"+str(self.animation)+"tir.png")
        else:
            if self.type == 5 and self.hp <= 2500:
                if self.animation < 5:
                    self.animation += 1
                else:
                    self.animation = 3
            elif self.type == 1 or self.type == 3 or (self.type == 5 and self.hp >2500) :
                if self.animation < 2:
                    self.animation += 1
                else:
                    self.animation = 0
            else:
                self.animation = 0
            self.image = pygame.image.load("images/Ennemi"+str(self.type)+"anime"+str(self.animation)+".png")

    def pattern(self,clock,group):
        if self.type == 1: #Rocket alien
            Pattern(self).patternLigneDroite(10)
            Pattern(self).patternTriangle(randint(50,300))
        if self.type == 2: #Space eye
            if not self.arrive:
                Pattern(self).patternArrive()
            else:
                Pattern(self).patternEnnemi2(200,50)
                if clock%15 == 0:
                    Tir(self.posX,self.posY,2).add(group)
                    self.animTir = 1
                    self.animation = 0
        if self.type == 3: #Head pack
            if not self.arrive:
                Pattern(self).patternArrive()
            else:
                Pattern(self).patternEnnemi3(200,150,group)
                if self.tir:
                    Tir(self.posX,self.posY,3).add(group)
                    Tir(self.posX,self.posY,4).add(group)
                    Tir(self.posX,self.posY,5).add(group)
                    self.animTir = 1
                    self.animation = 0
                    self.tir = 0
        if self.type == 5:
            if not self.arrive:
                Pattern(self).patternArrive()
            elif self.hp > 2500:
                Pattern(self).patternEnnemi3(450,150,group)
                if clock%20 == 0:
                    Tir(self.posX,self.posY+30,6).add(group)
                    Tir(self.posX,self.posY+30,7).add(group)
                    Tir(self.posX,self.posY+30,8).add(group)
                if clock%27 == 0:
                    Tir(self.posX-30,self.posY+50,9).add(group)
            elif self.hp > 2000:
                Pattern(self).patternPosition(self.spawnX,self.arriveY)
                if clock%20 == 0 and clock%40 != 0:
                    Tir(self.posX,self.posY+30,6).add(group)
                    Tir(self.posX,self.posY+30,7).add(group)
                    Tir(self.posX,self.posY+30,8).add(group)
                if clock%40 == 0:
                    Tir(self.posX-30,self.posY+50,10).add(group)
                    Tir(self.posX-30,self.posY+50,11).add(group)
                    Tir(self.posX-30,self.posY+50,12).add(group)
            else:
                Pattern(self).patternHorizontal(450)
                if clock%12 == 0 and clock%24 != 0:
                    Tir(self.posX,self.posY+30,6).add(group)
                    Tir(self.posX,self.posY+30,7).add(group)
                    Tir(self.posX,self.posY+30,8).add(group)
                if clock%24 == 0:
                    Tir(self.posX-30,self.posY+50,10).add(group)
                    Tir(self.posX-30,self.posY+50,11).add(group)
                    Tir(self.posX-30,self.posY+50,12).add(group)
                if clock%27 == 0:
                    Tir(self.posX-30,self.posY+50,9).add(group)
                if clock%45 == 0:
                    Tir(self.posX,self.posY,13).add(group)

        self.rect.center = (self.posX,self.posY)

    def touche(self,tir):
        self.hp -= tir.degat
        if self.hp <= 0:
            self.kill()
        tir.kill()

class Tir(pygame.sprite.Sprite):
    def __init__(self,positionX,positionY,type):
        pygame.sprite.Sprite.__init__(self)
        self.posX = positionX
        self.posY = positionY
        self.spawnX = positionX
        self.spawnY = positionY
        self.time = 0
        self.animation = 0
        self.type = type
        self.degat = 20
        if self.type in (7,8):
            self.img = 6
        else:
            self.img = self.type
        self.image = pygame.image.load("images/Tir"+str(self.img)+"anime"+str(self.animation)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX,self.posY)

    def move(self):
        if self.type == 1:
            self.posY -= 40
            if self.posY < -50:
                self.kill()
        elif self.type == 2:
            self.posY += 10
            if self.posY > longueurGameScreen+50:
                self.kill()
        elif self.type in (3,6,10):
            self.posY += 10
            if self.posY > longueurGameScreen+50:
                self.kill()
        elif self.type in (4,5,7,8):
            self.posY += 8
            if self.type in (4,7):self.posX -= 2
            elif self.type in (5,8):self.posX += 2
            if self.posY > longueurGameScreen+50:
                self.kill()
        elif self.type == 9:
            self.posY += 25
            if self.posY > longueurGameScreen+50:
                self.kill()
        elif self.type in (11,12):
            self.posY +=3
            if self.type == 11: self.posX-=5
            elif self.type == 12: self.posX+=5
        elif self.type == 13:
            Pattern(self).patternSinus(200,25)
            self.posY += 10

        self.rect.center = (self.posX,self.posY)

    def anim(self):
        if self.animation < 2:
            self.animation += 1
        else:
            self.animation = 0
        self.image = pygame.image.load("images/Tir"+str(self.type)+"anime"+str(self.animation)+".png")

class Scrolling(pygame.sprite.Sprite):
    def __init__(self,positionX,positionY,type,vitesse):
        pygame.sprite.Sprite.__init__(self)
        self.spawnX = positionX
        self.spawnY = positionY
        self.posX = positionX
        self.posY = positionY
        self.type = type
        self.vitesse = vitesse
        self.image = pygame.image.load("images/Scrolling"+str(self.type)+".png")
        self.rect = self.image.get_rect()
        self.hauteur = self.rect.height
        self.largeur = self.rect.width
        self.posX2 = self.posX
        self.posY2 = self.posY
        self.init = 0

    def scrollBas(self):
        if self.init == 0:
            self.posY2 = self.spawnY - self.hauteur
            self.init = 1
        else:
            if self.posY < self.spawnY + self.hauteur - self.vitesse*2:
                self.posY += self.vitesse
            else:
                self.posY = self.spawnY - self.hauteur
            if self.posY2 < self.spawnY + self.hauteur - self.vitesse*2:
                self.posY2 += self.vitesse
            else:
                self.posY2 = self.spawnY - self.hauteur

class AnimationStatique(pygame.sprite.Sprite):
    def __init__(self,positionX,positionY,type,nbAnim,buffer = 1,reload = 1):
        pygame.sprite.Sprite.__init__(self)
        self.reload = reload
        self.type = type
        self.nbAnim = nbAnim
        self.animation = 1
        self.image = pygame.image.load("images/"+str(self.type)+str(self.animation)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (positionX,positionY)
        self.buffer = buffer
        self.time = 0

    def anim(self):
        if self.time % self.buffer == 0:
            if self.animation < self.nbAnim:
                self.animation += 1
                self.image = pygame.image.load("images/"+str(self.type)+str(self.animation)+".png")
            elif self.reload :
                self.animation = 1
                self.image = pygame.image.load("images/"+str(self.type)+str(self.animation)+".png")
            else:
                self.kill()
            self.time += 1
        else:
            self.time += 1
