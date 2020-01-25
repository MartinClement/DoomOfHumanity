__author__ = 'Full'

# -*- coding: Utf-8 -*-

import pygame
import Constantes
from ClassesItemsPowUp import *

class Vaisseau(pygame.sprite.Sprite):
    def __init__(self,positionX,positionY,numero,arme,vie=3):
        pygame.sprite.Sprite.__init__(self)
        self.posX = positionX
        self.posY = positionY
        self.numero = numero-1 # Numero du joueur
        self.choix = animationFatalShock
        self.image =  pygame.image.load(spriteFatalShock1)
        self.animation = 0
        self.vitesse = speedVaisseau
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX,self.posY)
        self.hitbox = pygame.Rect(self.posX+20,self.posY+20,20,20)
        self.vie = vie
        self.hardmode = 0
        self.arme = arme
        self.armeLvl = 1
        self.buffer = 0
        self.typeArme = 0
        self.invul = 0
        self.timerInvul = 0
        self.chargement = 0

        # Touches
        self.Thaut = touchesAll[self.numero][0]
        self.Tgauche = touchesAll[self.numero][1]
        self.Tbas = touchesAll[self.numero][2]
        self.Tdroite = touchesAll[self.numero][3]
        self.Tspeed = touchesAll[self.numero][4]
        self.Ttir = touchesAll[self.numero][5]
        self.Tpause = touchesAll[self.numero][6]
        self.Tvalider = touchesAll[self.numero][7]

    def move(self,keys):
        if keys[self.Tdroite]:
            if self.posX < (zoneJeu[0]+zoneJeu[2]-61-self.vitesse):
                self.posX += self.vitesse
            else:
                self.posX = zoneJeu[0]+zoneJeu[2]-60
        if keys[self.Tgauche]:
            if self.posX > (zoneJeu[0]+self.vitesse):
                self.posX -= self.vitesse
            else:
                self.posX = zoneJeu[0]
        if keys[self.Tbas]:
            if self.posY < (zoneJeu[1]+zoneJeu[3]-61-self.vitesse):
                self.posY += self.vitesse
            else:
                self.posY = zoneJeu[1]+zoneJeu[3]-60
        if keys[self.Thaut]:
            if self.posY > (zoneJeu[1]+self.vitesse):
                self.posY -= self.vitesse
            else:
                self.posY = zoneJeu[1]
        self.rect.topleft = (self.posX,self.posY)
        if self.invul:
            self.hitbox = pygame.Rect(5000,5000,20,20)
            self.timerInvul += 1
            if self.timerInvul > 100:
                self.timerInvul = 0
                self.invul = 0
        else:
            self.hitbox = pygame.Rect(self.posX+20,self.posY+20,20,20)

    def anim(self):

            if self.animation < 2:
                self.animation += 1
            else:
                self.animation = 0
            if self.invul:
                self.image = pygame.image.load(self.choix[self.animation+3])
            else:
                self.image = pygame.image.load(self.choix[self.animation])

    def touche(self):
        self.vie -= 1
        self.posX = 250
        self.posY = 700
        if self.vie == 0:
            self.kill()
        self.rect.topleft = (self.posX,self.posY)
        self.invul = 1
        if self.arme ==1:
            self.typeArme = 0
        if self.armeLvl > 1:
            self.armeLvl -= 1

    def collision(self,ennemi,kill=0,groupAnim=None):
        res = self.hitbox.colliderect(ennemi.rect)
        if kill and res:
            if ennemi.type == 5:
                AnimationStatique(self.posX,self.posY,'ennemisExplose',14,0).add(groupAnim)
                pygame.mixer.Sound(sonExplosion).play()
                self.touche()
            else:
                AnimationStatique(ennemi.posX,ennemi.posY,'ennemisExplose',14,0).add(groupAnim)
                pygame.mixer.Sound(sonExplosion).play()
                ennemi.kill()
                self.touche()
        elif res:
            AnimationStatique(self.posX,self.posY,'ennemisExplose',14,0).add(groupAnim)
            pygame.mixer.Sound(sonExplosion).play()
            self.touche()

    def collisionPowerUp(self,pup):
        res = self.rect.colliderect(pup.rect)
        if res:
            if pup.type == 4:
                self.vie += 1
            elif (self.arme+1) == pup.type:
                if self.armeLvl < 3:
                    self.armeLvl += 1
                else:
                    self.vie += 1
            else:
                if self.armeLvl > 1:
                    self.armeLvl -= 1
                self.arme = pup.type -1
            if self.arme == 1:
                self.typeArme = 0
            pup.kill()

    def tir(self,group):

        if self.arme == 0:

            if self.armeLvl == 1:
                Tir(self.posX+31,self.posY-10,14).add(group)
            elif self.armeLvl == 2 :
                Tir(self.posX+31,self.posY-10,15).add(group)
            elif self.armeLvl == 3 :
                Tir(self.posX+31,self.posY-10,15).add(group)
                Tir(self.posX+5,self.posY,16).add(group)
                Tir(self.posX+55,self.posY,17).add(group)
            pygame.mixer.Sound(sontir1).play()

        elif self.arme == 2:
            if self.buffer % 3 == 0:
                if self.armeLvl == 1:
                    pygame.mixer.Sound(sontir4).play()
                    Tir(self.posX+31,self.posY-10,18).add(group)
                elif self.armeLvl == 2:
                    pygame.mixer.Sound(sontir4).play()
                    Tir(self.posX+31,self.posY-10,22).add(group)
                else:
                    pygame.mixer.Sound(sontir4).play()
                    Tir(self.posX+31,self.posY-10,31).add(group)

            self.buffer += 1
        else:
            if self.armeLvl == 1:
                if self.typeArme == 0:
                    if self.buffer % 10 == 0:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,26).add(group)
                        self.typeArme = 1
                        self.buffer = 0
                elif self.typeArme == 1:
                    if self.buffer == 2:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,25).add(group)
                        self.typeArme = 2
                elif self.typeArme == 2:
                    if self.buffer == 4:
                        pygame.mixer.Sound(sontir2).play()
                        Tir(self.posX+31,self.posY-10,27).add(group)
                        self.typeArme = 0
            if self.armeLvl == 2:
                if self.typeArme == 0:
                    if self.buffer % 10 == 0:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,26).add(group)
                        self.typeArme = 1
                        self.buffer = 0
                elif self.typeArme == 1:
                    if self.buffer == 2:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,25).add(group)
                        self.typeArme = 2
                elif self.typeArme == 2:
                    if self.buffer == 4:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,27).add(group)
                        self.typeArme = 3
                elif self.typeArme == 3:
                    if self.buffer == 6:
                        pygame.mixer.Sound(sontir2).play()
                        Tir(self.posX+31,self.posY-10,27).add(group)
                        self.typeArme = 0
            if self.armeLvl == 3:
                if self.typeArme == 0:
                    if self.buffer % 10 == 0:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,29).add(group)
                        self.typeArme = 1
                        self.buffer = 0
                elif self.typeArme == 1:
                    if self.buffer == 2:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,28).add(group)
                        self.typeArme = 2
                elif self.typeArme == 2:
                    if self.buffer == 4:
                        pygame.mixer.Sound(sontir3).play()
                        Tir(self.posX+31,self.posY-10,30).add(group)
                        self.typeArme = 3
                elif self.typeArme == 3:
                    if self.buffer == 6:
                        pygame.mixer.Sound(sontir2).play()
                        Tir(self.posX+31,self.posY-10,30).add(group)
                        self.typeArme = 0
            self.buffer += 1