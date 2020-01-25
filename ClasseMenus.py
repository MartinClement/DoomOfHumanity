__author__ = 'Full'

# -*- coding: Utf-8 -*-

import pygame
import sys
from Constantes import *
from ClassesItems import *
from ClasseVaisseauxJoueurs import *

class Menu(object):
    def __init__(self,numero,groupeScrolling=None,groupeSprite=None,groupeVaisseau=None,choix=0):
        self.numero = numero
        self.nbChoix = len(ordreMenu[self.numero])
        self.choix = choix
        self.image = pygame.image.load("images/Menu"+str(self.numero)+"sprite"+str(self.choix)+".png")
        self.sonMove = pygame.mixer.Sound(sonMoveMenu)
        self.sonRetour = pygame.mixer.Sound(sonRetourMenu)
        self.sonValide = pygame.mixer.Sound(sonValideMenu)
        self.continuer = 1
        self.groupScroll = groupeScrolling
        self.groupSprite = groupeSprite
        self.groupVaisseau = groupeVaisseau

    def move(self,key,joueur):

        if self.numero == 0: # MENU PRINCIPAL

            # Déplacements
            if key == joueur.Tbas:
                if self.choix < self.nbChoix-1: self.choix +=1
                else: self.choix = 0
                self.sonMove.play()
            if key == joueur.Thaut:
                if self.choix > 0: self.choix -= 1
                else: self.choix = self.nbChoix -1
                self.sonMove.play()

            # Validation
            if key == joueur.Tvalider:
                if self.choix == 0:
                    self.numero = 2
                    self.sonValide.play()
                elif self.choix == 1:
                    joueur.hardmode = 1
                    self.numero = 2
                    self.sonValide.play()
                    self.choix = 0
                elif self.choix == 2:
                    joueur.chargement = 1
                    self.numero = 2
                    self.sonValide.play()
                    self.choix = 0
                elif self.choix == 3:
                    sys.exit(0)
            self.nbChoix = len(ordreMenu[self.numero])

        elif self.numero == 2: # MENU CHOIX NB JOUEURS

             # Déplacements
            if key == joueur.Tdroite:
                if self.choix != self.nbChoix-1: self.choix += 1
                else: self.choix = 0
                self.sonMove.play()
            if key == joueur.Tgauche:
                if self.choix == 0 : self.choix = self.nbChoix-1
                else: self.choix -= 1
                self.sonMove.play()

            # Validation
            if key == joueur.Tvalider:
                if self.choix == 1: Vaisseau(300,750,2,2,nombreDeVies).add(self.groupVaisseau)
                self.numero = 1
                self.choix = 0
                self.sonValide.play()
            self.groupScroll.empty()
            self.groupSprite.empty()
            Scrolling(48,80,1,10).add(self.groupScroll)
            AnimationStatique(169,378,"FieryPheonix",3,2).add(self.groupSprite)
            self.nbChoix = len(ordreMenu[self.numero])

        elif self.numero == 1: # MENU CHOIX VAISSEAUX

            # Déplacements
            if key == joueur.Tdroite and self.choix != 3:
                if self.choix == 2: self.choix = 0
                else: self.choix += 1
                self.sonMove.play()
            if key == joueur.Tgauche and self.choix != 3:
                if self.choix == 0: self.choix = 2
                else: self.choix -= 1
                self.sonMove.play()
            if key == joueur.Tbas:
                if self.choix == 3: self.choix = 0
                else: self.choix = 3
                self.sonMove.play()
            if key == joueur.Thaut:
                if self.choix !=3: self.choix = 3
                else: self.choix = 0
                self.sonMove.play()

            # Validation
            if key == joueur.Tvalider:
                if self.choix == 0:
                    joueur.choix = animationFiery
                    joueur.arme = 0
                    self.continuer = 0
                    self.sonValide.play()
                elif self.choix == 1:
                    joueur.choix = animationTsunami
                    joueur.arme = 1
                    self.continuer = 0
                    self.sonValide.play()
                elif self.choix == 2 :
                    joueur.arme = 2
                    joueur.choix = animationFatalShock
                    self.continuer = 0
                    self.sonValide.play()
                elif self.choix == 3:
                    self.numero = 0
                    self.choix = 0
                    joueur.hardmode = 0
                    joueur.chargement = 0
                    self.sonRetour.play()
                self.nbChoix = len(ordreMenu[self.numero])

            # Animation
            if key == joueur.Tgauche or key == joueur.Tdroite or key == joueur.Tbas or key == joueur.Thaut:
                if self.choix == 0 :
                    self.groupScroll.empty()
                    self.groupSprite.empty()
                    Scrolling(48,80,1,10).add(self.groupScroll)
                    AnimationStatique(169,378,"FieryPheonix",3,2).add(self.groupSprite)
                if self.choix == 1 :
                    self.groupScroll.empty()
                    self.groupSprite.empty()
                    Scrolling(329,80,1,10).add(self.groupScroll)
                    AnimationStatique(452,378,"Tsunami",3).add(self.groupSprite)
                if self.choix == 2 :
                    self.groupScroll.empty()
                    self.groupSprite.empty()
                    Scrolling(609,80,1,10).add(self.groupScroll)
                    AnimationStatique(740,378,"FatalShock",3,2).add(self.groupSprite)

        self.image = pygame.image.load("images/Menu"+str(self.numero)+"sprite"+str(self.choix)+".png")
