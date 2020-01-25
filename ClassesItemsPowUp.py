__author__ = 'Full'

# -*- coding: Utf-8 -*-

import pygame
from Constantes import *
from ClassePatterns import *

class Ennemis(pygame.sprite.Sprite):
    def __init__(self,type,spawnX,spawnY,declenchement=0,sens=0,timer=0,powerUp=False):
        pygame.sprite.Sprite.__init__(self)
        self.posX = spawnX
        self.posY = spawnY
        self.spawnX = spawnX
        self.spawnY = spawnY
        self.type = type
        self.time = timer
        self.powerUp = powerUp
        self.start = declenchement
        self.animation = 0
        self.sens = sens
        self.image = pygame.image.load("images/Ennemi"+str(self.type)+"anime"+str(self.animation)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX,self.posY)
        self.arrive = 0
        self.tir = 0
        self.animTir = 0
        self.gele = 0
        if self.type == 1:
            self.hp = 60
            self.points = 100
        elif self.type == 2:
            self.hp = 200
            self.arriveY = randint(50,250)
            self.points = 150
        elif self.type == 3:
            self.hp = 160
            self.arriveY = randint(50,150)
            self.sensY = 0
            self.points = 300
        elif self.type == 5:
            self.hp = 5000
            self.arriveY = randint(50,100)
            self.sensY = 0
            self.points = 1000

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
        if self.type == 1: # Rocket alien
            Pattern(self).patternLigneDroite(10)
            Pattern(self).patternTriangle(randint(50,300))
        if self.type == 2: # Space eye
            if not self.arrive:
                Pattern(self).patternArrive()
            else:
                Pattern(self).patternEnnemi2(200,50)
                if clock%15 == 0:
                    Tir(self.posX,self.posY,2).add(group)
                    self.animTir = 1
                    self.animation = 0
        if self.type == 3: # Head pack
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
        if self.type == 5: # Mini boss
            if not self.arrive:
                Pattern(self).patternArrive()
            elif self.hp > 2500:
                Pattern(self).patternEnnemi3(450,150,group)
                if clock%20 == 0:
                    Tir(self.posX,self.posY+30,6).add(group)
                    Tir(self.posX,self.posY+30,7).add(group)
                    Tir(self.posX,self.posY+30,8).add(group)
                if clock%27 == 0:
                    pygame.mixer.Sound(sontir5).play()
                    Tir(self.posX-30,self.posY+50,9).add(group)
            elif self.hp > 2000:
                Pattern(self).patternPosition(self.spawnX,self.arriveY,speedVaisseauEnnemis)
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
                    pygame.mixer.Sound(sontir5).play()
                    Tir(self.posX-30,self.posY+50,9).add(group)
                if clock%45 == 0:
                    Tir(self.posX,self.posY,13).add(group)

        self.rect.center = (self.posX,self.posY)

    def touche(self,tir,group,groupAnim,groupTir,ath):
        AnimationStatique(tir.posX,tir.posY,'tirExplose',7,0).add(groupAnim)
        if self.type == 5:
            if self.hp <= 2500:
                self.image = pygame.image.load("images/Ennemi5anime7.png")
            else: self.image = pygame.image.load("images/Ennemi5anime6.png")
        if tir.type == 18:
            Tir(tir.posX,tir.posY-20,19).add(groupTir)
            Tir(tir.posX,tir.posY-20,20).add(groupTir)
            Tir(tir.posX,tir.posY-20,21).add(groupTir)
        elif tir.type == 22:
            Tir(tir.posX,tir.posY-20,19).add(groupTir)
            Tir(tir.posX,tir.posY-20,20).add(groupTir)
            Tir(tir.posX,tir.posY-20,21).add(groupTir)
            Tir(tir.posX,tir.posY-20,23).add(groupTir)
            Tir(tir.posX,tir.posY-20,24).add(groupTir)
        elif tir.type == 31:
            Tir(tir.posX,tir.posY-20,19).add(groupTir)
            Tir(tir.posX,tir.posY-20,20).add(groupTir)
            Tir(tir.posX,tir.posY-20,21).add(groupTir)
            Tir(tir.posX,tir.posY-20,23).add(groupTir)
            Tir(tir.posX,tir.posY-20,24).add(groupTir)
            Tir(tir.posX,tir.posY-20,32).add(groupTir)
            Tir(tir.posX,tir.posY-20,33).add(groupTir)

        elif tir.type in (26,29):
            self.gele = 1
        elif tir.type == 27:
            if self.gele:
                tir.degat = tir.degat * 2
        self.hp -= tir.degat
        tir.kill()
        if self.hp <= 0:
            self.kill()
            AnimationStatique(self.posX,self.posY,'ennemisExplose',14,0).add(groupAnim)
            pygame.mixer.Sound(sonExplosion).play()
            if self.powerUp:
                PowerUp(self.posX,self.posY,randint(1,3)).add(group)
            ath.scoreTotal += self.points

class PowerUp(pygame.sprite.Sprite):
    def __init__(self,positionX,positionY,type):
        pygame.sprite.Sprite.__init__(self)
        self.posX = positionX
        self.posY = positionY
        self.spawnX = positionX
        self.spawnY = positionY
        self.time = 0
        self.type = type
        self.image = pygame.image.load("images/coeur"+str(self.type)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX,self.posY)

    def move(self):
        if self.posY < 800:
            self.posY += 5
        else:
            self.kill()
        self.rect.center = (self.posX,self.posY)

    def anim(self):
        if self.time % 20 == 0:
            if self.type != 4:
                self.type += 1
            else:
                self.type = 1
            self.image = pygame.image.load("images/coeur"+str(self.type)+".png")
        self.time += 1

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

        if self.type in (1,11,14,16,17,19,20,21,23,24,32,33):
            self.degat = 20
        elif self.type in (15,18,22,26) :
            self.degat = 40
        elif self.type in (25,27,29,31):
            self.degat = 60
        elif self.type in (28,30):
            self.degat = 100

        if self.type in (7,8):
            self.img = 6
        elif self.type in (16,17):
            self.img = 14
        elif self.type in (19,20,21):
            self.img = 3
        elif self.type == 22:
            self.img = 18
        else:
            self.img = self.type

        self.image = pygame.image.load("images/Tir"+str(self.img)+"anime"+str(self.animation)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX,self.posY)

    def move(self):
        if self.type in (1,14,15,25,26,27,28,29,30):
            self.posY -= 40
            if self.posY < -50:
                self.kill()
        elif self.type == 16:
            self.posY -= 40
            self.posX -= 4
            if self.posY < -50:
                self.kill()
        elif self.type == 17:
            self.posY -= 40
            self.posX += 4
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
            if self.type in (4,7,20):self.posX -= 2
            elif self.type in (5,8,21):self.posX += 2
            if self.posY > longueurGameScreen+50:
                self.kill()
        elif self.type == 9:
            self.posY += 25
            if self.posY > longueurGameScreen+50:
                self.kill()
        elif self.type in (11,12):
            self.posY +=3
            if self.type == 11: self.posX -= 5
            elif self.type == 12: self.posX += 5
        elif self.type in (23,24):
            self.posY +=10
            if self.type == 23: self.posX -= 15
            elif self.type == 24: self.posX += 15
        elif self.type == 13:
            Pattern(self).patternSinus(200,25)
            self.posY += 10
        elif self.type in (18,19,22,31):
            self.posY -= 20
            if self.posY < -50:
                self.kill()
        elif self.type == 20:
            self.posY -= 20
            self.posX += 3
            if self.posY < -50:
                self.kill()
        elif self.type == 21:
            self.posY -= 20
            self.posX -= 3
            if self.posY < -50:
                self.kill()
        elif self.type  ==  32:
            self.posX += 20
        elif self.type  ==  33:
            self.posX -= 20

        self.rect.center = (self.posX,self.posY)

    def anim(self):
        if self.type in (18,31):
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
            if self.posY < self.spawnY + longueurGameScreen + 10:
                self.posY += self.vitesse
            else:
                self.posY = self.posY2 - self.hauteur + self.vitesse
            if self.posY2 < self.spawnY + longueurGameScreen + 10:
                self.posY2 += self.vitesse
            else:
                self.posY2 = self.posY - self.hauteur

class AnimationStatique(pygame.sprite.Sprite):
    def __init__(self,positionX,positionY,type,nbAnim,reload = 1):
        pygame.sprite.Sprite.__init__(self)
        self.reload = reload
        self.type = type
        self.nbAnim = nbAnim
        self.animation = 1
        self.image = pygame.image.load("images/"+str(self.type)+str(self.animation)+".png")
        self.rect = self.image.get_rect()
        self.rect.center = (positionX,positionY)

    def anim(self):
        if self.animation < self.nbAnim:
            self.animation += 1
            self.image = pygame.image.load("images/"+str(self.type)+str(self.animation)+".png")
        elif self.reload :
            self.animation = 1
            self.image = pygame.image.load("images/"+str(self.type)+str(self.animation)+".png")
        else:
            self.kill()

class Ath(pygame.sprite.Sprite):
    def __init__(self,group):
        pygame.sprite.Sprite.__init__(self)

        self.txt_vie = pygame.font.SysFont('liberationsans', 40)
        self.txt_Point = pygame.font.Font('polices/ledPoints.ttf', 70)
        self.typeAth = 0
        self.vaisseau = pygame.image.load("images/FieryPheonix1.png")
        self.vie = ""
        self.nbVieRestantes = 0
        self.score = 0
        self.scoreTotal = 0
        self.arme = 0
        self.armeLvl = 0
        ElemAth(2,self.score,self.vaisseau,self.arme,self.armeLvl,666,474).add(group) #Arme en cours
        ElemAth(4,self.score,self.vaisseau,self.arme,self.armeLvl,732,720).add(group)


    def changeImageFondAth(self,group,typeAth):
        ElemAth(0,self.score,self.vaisseau,self.arme,self.armeLvl,0,0,typeAth).add(group) #Ath


    def updateAth(self,group,nbVieRestantes):
        self.score = str(self.score)
        while len(self.score) != 5:
            self.score = "0" + self.score
        if nbVieRestantes == 1:
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,670,627).add(group)
        elif nbVieRestantes == 2:
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,670,627).add(group)
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,747,627).add(group)
        elif nbVieRestantes == 3:
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,670,627).add(group)
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,747,627).add(group)
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,823,627).add(group)
        elif nbVieRestantes > 3:
            ElemAth(1,self.score,self.vaisseau,self.arme,self.armeLvl,670,624).add(group)
            ElemAth(4,self.score,self.vaisseau,self.arme,self.armeLvl,732,639).add(group)
            self.vie =  self.txt_vie.render(str(self.nbVieRestantes),True,(255,255,255))
        if self.armeLvl == 1:
            ElemAth(3,self.score,self.vaisseau,self.arme,self.armeLvl,832,589).add(group)
        elif self.armeLvl == 2:
            ElemAth(3,self.score,self.vaisseau,self.arme,self.armeLvl,832,566).add(group)
        elif self.armeLvl == 3:
            ElemAth(3,self.score,self.vaisseau,self.arme,self.armeLvl,832,543).add(group)
        elif self.armeLvl == 4:
            ElemAth(3,self.score,self.vaisseau,self.arme,self.armeLvl,832,520).add(group)
        elif self.armeLvl == 5:
            ElemAth(3,self.score,self.vaisseau,self.arme,self.armeLvl,832,497).add(group)
        ElemAth(2,self.score,self.vaisseau,self.arme,self.armeLvl,666,474).add(group)
        self.txtscore = self.txt_Point.render(str(self.score),True,(200,200,200))

class ElemAth(pygame.sprite.Sprite):
    def __init__(self,type,score,vaisseau,arme,armeLvl,posX,posY,typeAth=0):
        pygame.sprite.Sprite.__init__(self)
        if type == 0: #Ath
            self.image = pygame.image.load("images/ATH"+ str(typeAth) + ".png")
            self.rect = self.image.get_rect()
            self.rect.topleft = (posX,posY)
        elif type == 1: #Vaisseau des vies
            self.image = vaisseau
            self.rect = self.image.get_rect()
            self.rect.topleft = (posX,posY)
        elif type ==  2: #Arme
            self.image = pygame.image.load("images/arme" + str(arme+1)+".png")
            self.rect = self.image.get_rect()
            self.rect.topleft = (posX,posY)
        elif type == 3:
            self.image = pygame.image.load("images/CurseurNiveau.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = (posX,posY)
        elif type == 4:
            self.image = pygame.image.load("images/CroixMultiplicateur.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = (posX,posY)