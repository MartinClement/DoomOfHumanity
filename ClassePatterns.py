__author__ = 'Full'

# -*- coding: Utf-8 -*-

from Constantes import *
import pygame
from ClassesItems import *
from math import *
from random import *

class Pattern(object):
    def __init__(self,item):
        self.item = item

    def patternLigneDroite(self,vitesse):
        if self.item.posY < 200:
            self.item.posY += vitesse/3
        else:
            self.item.posY += vitesse
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternTriangle(self,largeur=200): # Paterne en dents de scie
        if self.item.sens==1:
            if self.item.posX < self.item.spawnX+(largeur/2):
                self.item.posX += speedVaisseauEnnemis
                self.item.posY += speedVaisseauEnnemis
            else:
                self.item.sens = 0
        else:
            if self.item.posX > self.item.spawnX-(largeur/2):
                self.item.posX -= speedVaisseauEnnemis
                self.item.posY += speedVaisseauEnnemis
            else:
                self.item.sens = 1
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternSinus(self,P=200,A=50): # paterne sinusoide
        self.item.posY += speedVaisseauEnnemis
        self.item.posX = self.item.spawnX + A*sin(((2*pi)/P)*(self.item.time*5))
        self.item.time += 1
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternRacineK(self,F):
        self.item.posY += speedVaisseauEnnemis
        self.item.posX = self.item.spawnX + F*sqrt(self.item.posY)
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternLogBase(self,base,F):
        self.item.posY += speedVaisseauEnnemis
        self.item.posX = self.item.spawnX + F*log(self.item.posY,base)
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternZZagRacine(self,L,F):
        self.item.time += 1
        self.item.posY += speedVaisseauEnnemis
        if self.item.sens:
            self.item.posX = self.item.posX + F*(sqrt(self.item.time)-sqrt(self.item.time-1))
        else:
            self.item.posX = self.item.posX - F*(sqrt(self.item.time)-sqrt(self.item.time-1))
        if self.item.time % L == 0:
            self.item.time = 1
            if self.item.sens: self.item.sens = 0
            else: self.item.sens = 1
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternSquaredLooping(self,L):
        self.item.time += 1
        if self.item.sens:
            if self.item.time < L/6:
                self.item.posY += speedVaisseauEnnemis # tout droit
            elif self.item.time < L/3:                   # bas droite
                self.item.posY += speedVaisseauEnnemis
                self.item.posX += speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time < L/2:                 # haut droite
                self.item.posY -= speedVaisseauEnnemis
                self.item.posX += speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time < (2*L)/3:             # haut gauche
                self.item.posY -= speedVaisseauEnnemis
                self.item.posX -= speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time < (5*L)/6:             # bas gauche
                self.item.posY += speedVaisseauEnnemis
                self.item.posX -= speedVaisseauEnnemis
                self.item.time += 1
            else:                                 # tout droit
                self.item.posY += speedVaisseauEnnemis
                self.item.time += 1
        else:
            if self.item.time < L/6:
                self.item.posY += speedVaisseauEnnemis
            elif self.item.time < L/3:
                self.item.posY += speedVaisseauEnnemis
                self.item.posX -= speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time < L/2:
                self.item.posY -= speedVaisseauEnnemis
                self.item.posX -= speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time < (2*L)/3:
                self.item.posY -= speedVaisseauEnnemis
                self.item.posX += speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time < (5*L)/6:
                self.item.posY += speedVaisseauEnnemis
                self.item.posX += speedVaisseauEnnemis
                self.item.time += 1
            else:
                self.item.posY += speedVaisseauEnnemis
                self.item.time += 1
        if self.item.time == L:
            self.item.time = 0
            if self.item.sens: self.item.sens = 0
            else: self.item.sens = 1
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternZZag(self,L):
        self.item.time += 1
        if self.item.time < L/2:
            self.item.posX += speedVaisseauEnnemis
            self.item.time += 1
        else:
            self.item.posY += speedVaisseauEnnemis
            self.item.posX -= speedVaisseauEnnemis
            self.item.time += 1
        if self.item.time == L: self.item.time = 0
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternDodge(self,L):
        self.item.time += 1
        if self.item.sens:
            if self.item.time >= L/5 and self.item.time < (2*L)/5:
                self.item.posX -= speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time >= (3*L)/5 and self.item.time < (4*L)/5:
                self.item.posX += speedVaisseauEnnemis
                self.item.time += 1
            else: self.item.posY += speedVaisseauEnnemis
        else:
            if self.item.time >= L/5 and self.item.time < (2*L)/5:
                self.item.posX += speedVaisseauEnnemis
                self.item.time += 1
            elif self.item.time >= (3*L)/5 and self.item.time < (4*L)/5:
                self.item.posX -= speedVaisseauEnnemis
                self.item.time += 1
            else: self.item.posY += speedVaisseauEnnemis
        if self.item.time == L:
            self.item.time = 0
            if self.item.sens: self.item.sens = 0
            else: self.item.sens = 1
        if self.item.posY > longueurGameScreen+10:
            self.item.kill()

    def patternArrive(self,):
        if self.item.posY >= self.item.arriveY:
            self.item.arrive = 1
        else:
            self.item.posY += speedVaisseauEnnemis*1.4

    def patternEnnemi2(self,larg,haut):

        if self.item.sens:
            if self.item.posX < self.item.spawnX+larg/2:
                self.item.posX += speedVaisseauEnnemis
            else:
                if self.item.posY < self.item.arriveY+haut:
                    self.item.posY += speedVaisseauEnnemis
                else:
                    self.item.sens = 0
        else:
            if self.item.posX > self.item.spawnX-larg/2:
                self.item.posX -= speedVaisseauEnnemis
            else:
                if self.item.posY > self.item.arriveY:
                    self.item.posY -= speedVaisseauEnnemis
                else:
                    self.item.sens = 1

    def patternEnnemi3(self,larg,haut,group):

        if self.item.sens:
            if self.item.posX < self.item.spawnX+larg/2:
                self.item.posX += speedVaisseauEnnemis*0.8
            else:
                self.item.sens=0
        else:
            if self.item.posX > self.item.spawnX-larg/2:
                self.item.posX -= speedVaisseauEnnemis*0.8
            else:
                self.item.sens = 1
        if self.item.sensY:
            if self.item.posY < self.item.arriveY+haut:
                self.item.posY += speedVaisseauEnnemis*1.3
            else:
                self.item.sensY = 0
                self.item.tir = 1
        else:
            if self.item.posY > self.item.arriveY:
                self.item.posY -= speedVaisseauEnnemis*1.3
            else:
                self.item.sensY = 1
                self.item.tir = 1

    def patternPosition(self,x,y,vitesse):

        if self.item.posX >= x+vitesse+2:
            self.item.posX -= vitesse
        elif self.item.posX <= x-vitesse-2:
            self.item.posX += vitesse
        if self.item.posY >= y+vitesse:
            self.item.posY -= vitesse
        elif self.item.posX <= y-vitesse-2:
            self.item.posY += vitesse

    def patternHorizontal(self,larg):

        if self.item.sens:
            if self.item.posX <= self.item.spawnX+larg/2:
                self.item.posX += speedVaisseauEnnemis
            else:
                self.item.sens = 0
        else:
            if self.item.posX >= self.item.spawnX-larg/2:
                self.item.posX -= speedVaisseauEnnemis
            else:
                self.item.sens = 1