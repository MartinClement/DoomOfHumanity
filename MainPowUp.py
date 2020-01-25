__author__ = 'Full'

# -*- coding: Utf-8 -*

"""
Jeu Doom of Humanity: Last Hope

Script Python
Fichiers : Main.py, Classes.py, Contantes.py, Paterns.py,
"""

# Importations des modules et des autres fichiers
import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.joystick.init()

from ClasseMenus import *
from ClasseVaisseauxJoueurs import *
from ClassesItemsPowUp import *
from Constantes import *
from random import *
from data import *


def main():
    # Initialisation de la fenêtre d'affichage
    screen = pygame.display.set_mode((largeurScreen, longueurScreen))
    pygame.display.set_caption(titreFenetre)

    # Boucle principale
    continuer = 1
    while continuer:
        # Initialisation variables
        continuerJeu = 1
        continuerMenu = 1
        nbVies = nombreDeVies
        groupeJoueur = pygame.sprite.Group()
        Vaisseau(250, 700, 1,2, nbVies).add(groupeJoueur)
        tirInGame = pygame.sprite.Group()
        tirEnnemi = pygame.sprite.Group()
        pause = 0
        gameOver = 0
        groupeScrolling = pygame.sprite.Group()
        groupeAnimationStatique = pygame.sprite.Group()
        groupeAth = pygame.sprite.Group()
        groupeVie = pygame.sprite.Group()
        menu = Menu(0, groupeScrolling, groupeAnimationStatique, groupeJoueur)
        lockPause = 0
        lockGameOver = 0
        lvlEnCours = 1
        memGameOver = 0
        jeuFini = 0
        #vagueP = vagueLvl1
        ath = Ath(groupeAth)
        highscore = int(loadHS("data/highscore.xml"))

        # Boucle menu

        musiqueMenu = pygame.mixer.Sound(musiMenu)
        musiqueMenu.play(-1,0,4000)
        while continuerMenu:

            # Limitation vitesse de la boucle
            pygame.time.Clock().tick(120)  # Ticks par secondes

            # Gestion des events utilisateur
            for event in pygame.event.get():

                if event.type == QUIT:
                    return

                if event.type == KEYDOWN:

                    for joueur in groupeJoueur:
                        menu.move(event.key, joueur)

                if menu.continuer:
                    continuerMenu = 1
                else:
                    continuerMenu = 0
                keys = pygame.key.get_pressed()

                if keys[K_LALT] and keys[K_F4]:
                    return

            for scroll in groupeScrolling:
                scroll.scrollBas()
                screen.blit(scroll.image, (scroll.posX, scroll.posY))
                screen.blit(scroll.image, (scroll.posX2, scroll.posY2))

            groupeAnimationStatique.draw(screen)

            for animation in groupeAnimationStatique:
                animation.anim()

            # Blit Menu
            screen.blit(menu.image, (0, 0))
            pygame.display.flip()

        # Boucle Jeu
        musiqueMenu.fadeout(2000)
        while continuerJeu:
            for joueur in groupeJoueur:
                if joueur.hardmode == 1:
                    vagueP = [
                        [[5, 250, 0, 50, 0, 0], [5, 300, 0, 100, 0, 0], [5, 350, 0, 150, 0, 0], [5, 350, 0, 200, 0, 0]]]
                    nbLvl = 1
                    joueur.armeLvl = 3
                elif joueur.chargement == 1:
                    nbLvl = 2
                    chargement = load("data/savedata.xml")
                    lvlEnCours = chargement["nbLvl"]
                    joueur.arme = chargement["arme"]
                    joueur.armeLvl = chargement["lvlArme"]
                    joueur.vie = chargement["nbVie"]
                    ath.scoreTotal = chargement["score"]
                    joueur.choix = chargement["choix"]
                    print(chargement)
                else:
                    nbLvl = 2
            groupeScrolling.empty()
            groupScroll = []
            groupScroll += [Scrolling(10, 10, 3, 5),]
            groupScroll += [Scrolling(10, 10, 4, 13),]
            powerUpEnCour = pygame.sprite.Group()
            vague = 1
            groupeAnimationStatique.empty()
            ath.changeImageFondAth(groupeAth,menu.choix)
            contenuLvl = loadMap('data/maps/map'+str(lvlEnCours)+".xml")
            musiqueJeu = pygame.mixer.Sound(contenuLvl[1][0][0])
            musiqueJeu.play(-1,0,4000)
            for joueur in groupeJoueur:
                if joueur.hardmode == 0:
                    vagueP = contenuLvl[2]

            # Création de la vague d'ennemis
            while lvlEnCours < nbLvl + 1 and continuerJeu :
                ennemisDeVague = pygame.sprite.Group()
                for y in vagueP[vague - 1]:
                        Ennemis(y[0], y[1], y[2], y[3], y[4], y[5]).add(ennemisDeVague)
                vagueEnCours = pygame.sprite.Group()
                randomPick = randint(0, len(vagueEnCours))
                mobCounter = 0
                for ennemis in ennemisDeVague:
                    if mobCounter == randomPick:
                        ennemis.powerUp = 1
                    elif lvlEnCours == 2:
                        ennemis.powerUp = 1
                    mobCounter += 1

                clock = 0

                while len(ennemisDeVague.sprites()) != 0 or len(vagueEnCours.sprites()) != 0:
                    groupeVie.empty()
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

                    if keys[K_LALT] and keys[K_F4]:  # Alt+F4
                        return

                    if not pause and not gameOver:

                        # Mouvements tirs
                        for tir in tirInGame:
                            tir.move()
                            tir.anim()

                        for tir in tirEnnemi:
                            tir.move()
                            for vaisseauJoueur in groupeJoueur:
                                if vaisseauJoueur.alive():
                                    vaisseauJoueur.collision(tir, 1,groupeAnimationStatique)

                        # Mouvement Power Up
                        for pup in powerUpEnCour:
                            pup.move()
                            pup.anim()
                            for vaisseauJoueur in groupeJoueur:
                                vaisseauJoueur.collisionPowerUp(pup)

                        # Animation statique:
                        for animation in groupeAnimationStatique:
                            animation.anim()

                        # Actions Joueurs
                        for vaisseauJoueur in groupeJoueur:
                            vaisseauJoueur.move(keys)
                            if keys[vaisseauJoueur.Tspeed]:  # Boost vitesse
                                vaisseauJoueur.vitesse = speedVaisseau * 2
                            else:
                                vaisseauJoueur.vitesse = speedVaisseau
                            if keys[vaisseauJoueur.Ttir] and clock % 3 == 0:  # Tir
                                vaisseauJoueur.tir(tirInGame)
                            vaisseauJoueur.anim()  # animation

                        # Actions ennemis
                        for ennemi in vagueEnCours:
                            ennemi.pattern(clock, tirEnnemi)
                            ennemi.anim()

                            for vaisseauJoueur in groupeJoueur:
                                if vaisseauJoueur.alive():
                                    vaisseauJoueur.collision(ennemi, 1,groupeAnimationStatique)
                            for tirTouche in pygame.sprite.spritecollide(ennemi, tirInGame, False):
                                if ennemi.alive():
                                    ennemi.touche(tirTouche, powerUpEnCour, groupeAnimationStatique, tirInGame,ath)

                        if len(groupeJoueur.sprites()) == 0:
                            gameOver = 1

                        for scroll in groupScroll:  # Scrolling
                            scroll.scrollBas()
                            screen.blit(scroll.image, (scroll.posX, scroll.posY))
                            screen.blit(scroll.image, (scroll.posX2, scroll.posY2))

                    elif gameOver:

                        if keys[K_RETURN]:
                            gameOver = 0
                            vagueEnCours.empty()
                            ennemisDeVague.empty()
                            continuerJeu = 0

                    # Gestion Ath
                    for j in groupeJoueur:
                        if j.numero == 0:
                            ath.score = ath.scoreTotal
                            ath.nbVieRestantes = j.vie
                            ath.vaisseau = j.image
                            ath.arme = j.arme
                            ath.armeLvl = j.armeLvl

                    # Blit Jeu
                    powerUpEnCour.draw(screen)
                    vagueEnCours.draw(screen)
                    groupeJoueur.draw(screen)
                    tirInGame.draw(screen)
                    tirEnnemi.draw(screen)
                    groupeAnimationStatique.draw(screen)
                    ath.updateAth(groupeVie,ath.nbVieRestantes)
                    groupeAth.draw(screen)
                    groupeVie.draw(screen)
                    if ath.nbVieRestantes > 3:
                        screen.blit(ath.vie,positionVie)
                    screen.blit(pygame.font.Font('polices/ledPoints.ttf', 25).render(str(highscore),True,(200,200,200)), (640,57))
                    screen.blit(pygame.font.Font('polices/Akashi.ttf', 50).render("Niveau " + str(lvlEnCours),True,(0,0,0)), (660,286))
                    screen.blit(pygame.font.Font('polices/Akashi.ttf', 50).render("Vague " + str(vague),True,(0,0,0)), (660,356))
                    screen.blit(ath.txtscore,positionScore)
                    if ath.scoreTotal > highscore:
                        highscore = ath.scoreTotal

                    if pause:
                        if lockPause == 0:
                            screen.blit(pygame.image.load("images/Pause.png"), (0, 0))
                            lockPause = 1
                    else:
                        lockPause = 0
                        clock += 1

                    if gameOver:
                        if lockGameOver == 0:
                            screen.blit(pygame.image.load("images/gameOver.png"), (0, 0))
                            lockGameOver = 1
                            memGameOver = 1
                    else:
                        lockGameOver = 0
                    pygame.display.flip()
                vague += 1
                if vague > len(vagueP):
                    lvlEnCours += 1
                    vague = 1
                    musiqueJeu.fadeout(2000)
                    if lvlEnCours <= nbLvl:
                        contenuLvl = loadMap('data/maps/map'+str(lvlEnCours)+".xml")
                        musiqueJeu = pygame.mixer.Sound(contenuLvl[1][0][0])
                        musiqueJeu.play(-1,0,4000)
                        for joueur in groupeJoueur:
                            if joueur.hardmode == 0:
                                vagueP = contenuLvl[2]
                            if joueur.numero == 0:
                                save(lvlEnCours,joueur.arme,joueur.armeLvl,joueur.choix,ath.scoreTotal,joueur.vie)

            if not memGameOver: jeuFini = 1
            while jeuFini:
                if lockGameOver == 0:
                    screen.blit(pygame.image.load("images/Victoire.png"), (0, 0))
                    lockGameOver = 1
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            jeuFini = 0
            continuerJeu = 0

            saveHS(highscore)
            musiqueJeu.fadeout(2000)




if __name__ == '__main__': main()
