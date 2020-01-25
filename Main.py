__author__ = 'Full'

# -*- coding: Utf-8 -*

"""
Jeu Doom of Humanity: Last Hope

Script Python
Fichiers : Main.py, Classes.py, Contantes.py, Paterns.py,
"""

# Importations des modules et des autres fichiers
import pygame

pygame.init()
pygame.joystick.init()

from ClasseMenus import *
from ClasseVaisseauxJoueurs import *
from ClassesItems import *
from Constantes import *


def main():
    # Initialisation de la fenêtre d'affichage
    screen = pygame.display.set_mode((largeurScreen, longueurScreen))
    pygame.display.set_caption(titreFenetre)

    # Initialisation interface
    ath = pygame.image.load(spriteAth)

    # Boucle principale
    continuer = 1
    while continuer:

        # Initialisation variables
        continuerJeu = 1
        continuerMenu = 1
        nombreDeVies = 2
        groupeJoueur = pygame.sprite.Group()
        Vaisseau(250, 700, 1,nombreDeVies).add(groupeJoueur)
        tirInGame = pygame.sprite.Group()
        tirEnnemi = pygame.sprite.Group()
        pause = 0
        gameOver = 0
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        groupeScrolling = pygame.sprite.Group()
        groupeAnimationStatique = pygame.sprite.Group()
        menu = Menu(0,groupeScrolling,groupeAnimationStatique,groupeJoueur)
        lockPause = 0
        lockGameOver = 0
        lvlEnCours = 1
        memGameOver = 0
        jeuFini = 0
        vagueP = vagueLvl1

        # Boucle menu
        while continuerMenu:

            # Limitation vitesse de la boucle
            pygame.time.Clock().tick(120)  # Ticks par secondes

            # Gestion des events utilisateur
            for event in pygame.event.get():

                if event.type == QUIT:
                    return

                if event.type == KEYDOWN:

                    for joueur in groupeJoueur:
                        menu.move(event.key,joueur)

                if menu.continuer:
                    continuerMenu = 1
                else:
                    continuerMenu = 0
                keys = pygame.key.get_pressed()

                if keys[K_LALT] and keys[K_F4]:
                    return

            for scroll in groupeScrolling:
                scroll.scrollBas()
                screen.blit(scroll.image,(scroll.posX,scroll.posY))
                screen.blit(scroll.image,(scroll.posX2,scroll.posY2))

            groupeAnimationStatique.draw(screen)

            for animation in groupeAnimationStatique:
                animation.anim()

            # Blit Menu
            screen.blit(menu.image, (0,0))
            pygame.display.flip()

        # Boucle Jeu
        while continuerJeu:

            for joueur in groupeJoueur:
                if joueur.hardmode == 1:
                    vagueP = [[[5,250,0,50,0,0],[5,300,0,100,0,0],[5,350,0,150,0,0]]]

            # Création de la vague d'ennemis
            groupeScrolling.empty()
            Scrolling(10,10,3,15).add(groupeScrolling)
            vague = 1
            while lvlEnCours < nbLvl+1:

                ennemisDeVague = pygame.sprite.Group()
                for y in vagueP[vague-1]:
                    if len(y) == 3:
                        Ennemis(y[0],y[1],y[2]).add(ennemisDeVague)
                    elif len(y) == 4:
                        Ennemis(y[0],y[1],y[2],y[3]).add(ennemisDeVague)
                    elif len(y) == 5:
                        Ennemis(y[0],y[1],y[2],y[3],y[4]).add(ennemisDeVague)
                    else:
                        Ennemis(y[0],y[1],y[2],y[3],y[4],y[5]).add(ennemisDeVague)
                vagueEnCours = pygame.sprite.Group()
                clock = 0

                while len(ennemisDeVague.sprites()) != 0 or len(vagueEnCours.sprites()) != 0:

                    for ennemis in ennemisDeVague:
                        if ennemis.start == clock:
                            ennemis.add(vagueEnCours)
                            ennemis.remove(ennemisDeVague)

                    keys = pygame.key.get_pressed()

                    # Limitation vitesse de la boucle
                    pygame.time.Clock().tick(120)  # Ticks par secondes

                    # Gestion des events utilisateur
                    for event in pygame.event.get():

                        if event.type == QUIT:
                            return
                        if event.type == KEYDOWN:
                            for vaisseauJoueur in groupeJoueur:
                                if event.key == vaisseauJoueur.Tpause:
                                    if pause == 1:
                                        pause = 0
                                    else:
                                        pause = 1

                    if keys[K_LALT] and keys[K_F4]: # Alt+F4
                        return

                    if not pause and not gameOver:

                        # Mouvements tirs
                        for tir in tirInGame:
                            tir.move()
                            tir.anim()

                        for tir in tirEnnemi:
                            tir.move()
                            for vaisseauJoueur in groupeJoueur:
                                vaisseauJoueur.collision(tir,1)

                        # Actions Joueurs
                        for vaisseauJoueur in groupeJoueur:
                            if keys[vaisseauJoueur.Tgauche] or keys[vaisseauJoueur.Tdroite] or keys[vaisseauJoueur.Tbas] or keys[vaisseauJoueur.Thaut]: # Déplacements
                                vaisseauJoueur.move(keys)
                            if keys[vaisseauJoueur.Tspeed]: # Boost vitesse
                                vaisseauJoueur.vitesse = speedVaisseau * 2
                            else:
                                vaisseauJoueur.vitesse = speedVaisseau
                            if keys[vaisseauJoueur.Ttir] and clock % 3 == 0 : # Tir
                                vaisseauJoueur.tir(tirInGame)
                            vaisseauJoueur.anim() # animation

                        # Actions ennemis
                        for ennemi in vagueEnCours:
                            ennemi.pattern(clock,tirEnnemi)
                            ennemi.anim()
                            for vaisseauJoueur in groupeJoueur:
                                vaisseauJoueur.collision(ennemi,1)
                            for tirTouche in pygame.sprite.spritecollide(ennemi,tirInGame,False):
                                ennemi.touche(tirTouche)

                        if len(groupeJoueur.sprites()) == 0:
                            gameOver = 1

                        for scroll in groupeScrolling: # Scrolling
                            scroll.scrollBas()
                            screen.blit(scroll.image,(scroll.posX,scroll.posY))
                            screen.blit(scroll.image,(scroll.posX2,scroll.posY2))

                    elif gameOver:

                        if keys[K_RETURN]:
                            gameOver = 0
                            vagueEnCours.empty()
                            ennemisDeVague.empty()
                            lvlEnCours = nbLvl+1
                            vague = 0

                    # Blit Jeu
                    if not pause:
                        vagueEnCours.draw(screen)
                        groupeJoueur.draw(screen)
                        tirInGame.draw(screen)
                        tirEnnemi.draw(screen)
                        screen.blit(ath, (0,0))

                    if pause:
                        if lockPause == 0:
                            screen.blit(pygame.image.load("images/Pause.png"),(0,0))
                            lockPause = 1
                    else:
                        lockPause = 0
                        clock += 1

                    if gameOver:
                        if lockGameOver == 0:
                            screen.blit(pygame.image.load("images/gameOver.png"),(0,0))
                            lockGameOver = 1
                            lvlEnCours = nbLvl+1
                            memGameOver = 1
                    else:
                        lockGameOver = 0
                    pygame.display.flip()
                vague += 1
                if vague > len(vagueP):
                    lvlEnCours += 1
            if not memGameOver: jeuFini = 1
            while jeuFini:
                if lockGameOver == 0:
                    screen.blit(pygame.image.load("images/Victoire.png"),(0,0))
                    lockGameOver = 1
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            jeuFini = 0
            continuerJeu = 0

if __name__ == '__main__': main()