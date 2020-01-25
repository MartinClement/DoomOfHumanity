__author__ = 'Full'

# -*- coding: Utf-8 -*-

from pygame.locals import *
from random import *
from data import *

dico = loadData()

# Tailles
longueurScreen = dico["longueurScreen"]
largeurScreen = dico["largeurScreen"]
longueurGameScreen = dico["longueurGameScreen"]
largeurGameScreen =dico["largeurGameScreen"]
tailleMenu = dico["tailleMenu"]
tailleMenuVaisseau = dico["tailleMenuVaisseau"]

# Ordre des options du Menu Principale
campagneOrd = dico["campagneOrd"]
survivalOrd = dico["survivalOrd"]
chargerOrd = dico["chargerOrd"]
quitterOrd = dico["quitterOrd"]

# Ordre des options du Menu Vaisseau
vaisseau1Ord = dico["vaisseau1Ord"]
vaisseau2Ord = dico["vaisseau2Ord"]
vaisseau3Ord = dico["vaisseau3Ord"]
retourOrd = dico["retourOrd"]

# Ordre des options du Menu Choix Joueurs
nbJoueur1 = dico["nbJoueur1"]
nbJoueur2 = dico["nbJoueur2"]

# Position Menu
ordreMenuPrincipal = [campagneOrd,survivalOrd,chargerOrd,quitterOrd]
ordreMenuVaisseau = [vaisseau1Ord,vaisseau2Ord,vaisseau3Ord,retourOrd]
ordreMenuNbJoueurs = [nbJoueur1,nbJoueur2]
ordreMenu = [ordreMenuPrincipal,ordreMenuVaisseau,ordreMenuNbJoueurs]

#ATH
positionVie = dico["positionVie"]
positionScore = dico["positionScore"]


#zone jeu = (x,y,lenx,leny)
zoneJeuX = dico["zoneJeuX"]
zoneJeuY = dico["zoneJeuY"]
zoneJeu = (zoneJeuX, zoneJeuY, largeurGameScreen, longueurGameScreen)

# Sprites généraux
spriteAth = dico["spriteAth"]
spriteFondJeu = dico["spriteFondJeu"]
spriteVie0 = dico["spriteVie0"]
spriteVie1 = dico["spriteVie1"]

# Sprites Vaisseaux
spriteFiery1 = dico["spriteFiery1"]
spriteFiery2 = dico["spriteFiery2"]
spriteFiery3 = dico["spriteFiery3"]
spriteFiery1Invul = dico["spriteFiery1Invul"]
spriteFiery2Invul = dico["spriteFiery2Invul"]
spriteFiery3Invul = dico["spriteFiery3Invul"]
spriteFatalShock1 = dico["spriteFatalShock1"]
spriteFatalShock2 = dico["spriteFatalShock2"]
spriteFatalShock3 = dico["spriteFatalShock3"]
spriteFatalShock1Invul = dico["spriteFatalShock1Invul"]
spriteFatalShock2Invul = dico["spriteFatalShock2Invul"]
spriteFatalShock3Invul = dico["spriteFatalShock3Invul"]
spriteTsunami1 = dico["spriteTsunami1"]
spriteTsunami2 = dico["spriteTsunami2"]
spriteTsunami3 = dico["spriteTsunami3"]
spriteTsunami1Invul = dico["spriteTsunami1Invul"]
spriteTsunami2Invul = dico["spriteTsunami2Invul"]
spriteTsunami3Invul = dico["spriteTsunami3Invul"]


# Sprites Menus
spriteCampagne = dico["spriteCampagne"]
spriteCharger = dico["spriteCharger"]
spriteOptions = dico["spriteOptions"]
spritePassword = dico["spritePassword"]
spriteQuitter = dico["spriteQuitter"]
spriteVaisseauSelect1 = dico["spriteVaisseauSelect1"]
spriteVaisseauSelect2 = dico["spriteVaisseauSelect2"]
spriteVaisseauSelect3 = dico["spriteVaisseauSelect3"]
spriteVaisseauRetour = dico["spriteVaisseauRetour"]

# Animations
animationFiery = [spriteFiery1,spriteFiery2,spriteFiery3,spriteFiery1Invul,spriteFiery2Invul,spriteFiery3Invul]
animationFatalShock = [spriteFatalShock1,spriteFatalShock2,spriteFatalShock3,spriteFatalShock1Invul,spriteFatalShock2Invul,spriteFatalShock3Invul]
animationTsunami = [spriteTsunami1,spriteTsunami2,spriteTsunami3,spriteTsunami1Invul,spriteTsunami2Invul,spriteTsunami3Invul]
nbAnimEnnemi1 = dico["nbAnimEnnemi1"]

# Sons
sonMoveMenu = dico["sonMoveMenu"]
sonRetourMenu = dico["sonRetourMenu"]
sonValideMenu = dico["sonValideMenu"]
musiJeu = "sons/musiqueJeu.wav"
musiMenu = dico["musiMenu"]
sontir1 = dico["sonTir1"]
sontir2 = dico["sonTir2"]
sontir3 = dico["sonTir3"]
sontir4 = dico["sonTir4"]
sontir5 = dico["sonTir5"]
sonExplosion = dico["sonExplosion"]

# Divers
titreFenetre = dico["titreFenetre"]
speedVaisseau = dico["speedVaisseau"]
speedVaisseauEnnemis = dico["speedVaisseauEnnemis"]
nombreDeVies = dico["nombreDeVies"]


# Vagues : ennemi = type,spawnX,spawnY,declenchement=0,sens=0,timer=0
listeLvl1Vague1 = [[1,50,0,80,1],[1,175,0,70],[1,580,0,70],[1,randint(0,600),0,150,1],[1,randint(0,600),0,130,1],[1,randint(0,600),0,140,1]]
listeLvl1Vague2 = [[1,300,0,0,1],[1,130,0],[1,580,0,40],[2,randint(150,400),0,0,1],[1,randint(0,600),0,80,1],[1,randint(0,600),0,70,1],[1,randint(0,600),0,30,1],[1,randint(0,600),0,40,1]]
listeLvl1Vague3 = [[1,50,0,10,1],[1,175,0,20],[1,580,0,10],[2,randint(150,400),0,30,1],[2,randint(150,400),0,20,1],[1,randint(0,600),0,60,1]]
listeLvlVague4 = [[3,300,0,70],[2,randint(150,400),0,10,1],[2,randint(150,400),0,20,1],[2,randint(150,400),0,10,1]]
listeLvl1Vague5 = [[1,300,0,10,1],[1,130,0,10],[1,580,0,30],[3,300,0,20],[3,120,0,10,1],[3,430,0,15],[2,randint(150,400),0,50,1],[2,randint(150,400),0,60,1]]
listeLvl1Vague6 = [[5,300,0,10]]
vagueLvl1 = [listeLvl1Vague1,listeLvl1Vague2,listeLvl1Vague3,listeLvlVague4,listeLvl1Vague5,listeLvl1Vague6]
#vagueLvl1 = [listeLvl1Vague1]
nbLvl = 1

## TOUCHES ##


# Touches Joueur 1
J1gauche = dico["J1gauche"]
J1droite = dico["J1droite"]
J1haut = dico["J1haut"]
J1bas = dico["J1bas"]
J1speed = dico["J1speed"]
J1tir = dico["J1tir"]
J1pause = dico["J1pause"]
J1valider = dico["J1valider"]
touchesJ1 = [J1haut,J1gauche,J1bas,J1droite,J1speed,J1tir,J1pause,J1valider]

# Touches Joueur 2
J2gauche = dico["J2gauche"]
J2droite = dico["J2droite"]
J2haut = dico["J2haut"]
J2bas = dico["J2bas"]
J2speed = dico["J2speed"]
J2tir = dico["J2tir"]
J2pause = dico["J2pause"]
J2valider = dico["J2valider"]
touchesJ2 = [J2haut,J2gauche,J2bas,J2droite,J2speed,J2tir,J2pause,J2valider]

touchesAll = [touchesJ1,touchesJ2]

hardmode = 0