"""
@author: Killian
"""
from pygame.locals import *
from xml.dom import minidom
from random import *
#On sépare le fichier Highscore du fichier Savedata car l'écriture de chacun de ses fichiers ne se fait pas à la même condition.

#Valeurs d'exemple, à remplacer par les valeurs de la partie
levelEx=2
armeTypeEx=1
armeLvEx=4
vaisseauEx=1
scoreEx=950
nbVieEx=3

#Évenement à effectuer si le score actuel est supérieur au score sauvegardé précédement, et si Victoire ou Game Over
def saveHS(scoreEx):
    p=open('data/highscore.xml','w')

    newdoc = minidom.Document()
    newroot = newdoc.createElement('root')
    textnode = newdoc.createElement('highscore')
    textnode.setAttribute('value', str(scoreEx))

    newdoc.appendChild(newroot)
    newroot.appendChild(textnode)

    p.write(newdoc.toprettyxml())
    p.close()

def loadHS(file):
    doc=minidom.parse(file)
    root=doc.documentElement
    x=root.getElementsByTagName('highscore')[0]
    return x.getAttribute('value')

#Évenement à effectuer à la fin de chaque niveau
def save(levelEx,armeTypeEx,armeLvEx,vaisseauEx,scoreEx,nbVieEx):
    p=open('data/savedata.xml','w')

    newdoc=minidom.Document()
    newroot = newdoc.createElement('root')
    blbl = newdoc.createElement('save')
    level=newdoc.createElement('data')
    level.setAttribute('name',"nbLvl")
    level.setAttribute('value',str(levelEx))
    arme=newdoc.createElement('data')
    arme.setAttribute('name',"arme")
    arme.setAttribute('value',str(armeTypeEx))
    lvlArme=newdoc.createElement('data')
    lvlArme.setAttribute('name',"lvlArme")
    lvlArme.setAttribute('value',str(armeLvEx))
    vaisseau=newdoc.createElement('choix')
    vaisseau.setAttribute('name',"choix")
    vaisseau.setAttribute('value',str(vaisseauEx))
    score=newdoc.createElement('data')
    score.setAttribute('name',"score")
    score.setAttribute('value',str(scoreEx))
    nbVie=newdoc.createElement('data')
    nbVie.setAttribute('name',"nbVie")
    nbVie.setAttribute('value',str(nbVieEx))


    newdoc.appendChild(newroot)
    newroot.appendChild(blbl)
    blbl.appendChild(level)
    blbl.appendChild(arme)
    blbl.appendChild(lvlArme)
    blbl.appendChild(vaisseau)
    blbl.appendChild(score)
    blbl.appendChild(nbVie)

    p.write(newdoc.toprettyxml())
    p.close()

def load(file):
    doc=minidom.parse(file)
    root=doc.documentElement
    dico={}
    for x in root.getElementsByTagName('save')[0].getElementsByTagName('data'):
        dico[x.getAttribute('name')]=int(x.getAttribute('value'))
    for x in root.getElementsByTagName('save')[0].getElementsByTagName('choix'):
        dico[x.getAttribute('name')]=eval(x.getAttribute('value'))
    return dico

#saveHS(scoreEx)
#print(loadHS('highscore.xml'))

#save(levelEx,armeTypeEx, armeLvEx, vaisseauEx, scoreEx, nbVieEx)
#print(str(load('savedata.xml')))

#----------------------------------------------------------------------------------#

#Chargement de la map
def loadMap(data):
    doc=minidom.parse(data)
    root=doc.documentElement
    sprite=loadSprites(doc)
    waves=loadWaves(doc)
    sounds=loadSounds(doc)
    return sprite,sounds,waves

def loadSprites(data):
    root=data.documentElement
    res=[]
    x=root.getElementsByTagName('sprites')[0].getElementsByTagName('sprite')
    for i in x:
        res+=[[i.getAttribute('src'),i.getAttribute('positionX'),i.getAttribute('positionY'),i.getAttribute('type')]]
    return res

def loadSounds(data):
    root=data.documentElement
    res=[]
    x=root.getElementsByTagName('sounds')[0].getElementsByTagName('sound')
    for i in x:
        res+=[[i.getAttribute('src')]]
    return res
    
#Pour chaque éléments de ce tableau, [0]=type ; [1]=spawnX ; [2]=spawnY ; [3]=declenchement ; [4]=sens ; [5]=timer
def loadWaves(data):
    root=data.documentElement
    res=[]
    x=root.getElementsByTagName('waves')[0].getElementsByTagName('wave')
    for i in x:
        a=i.getElementsByTagName('unit')
        res2=[]
        for y in a:
            res2+=[[eval(y.getAttribute('type')),eval(y.getAttribute('spawnX')),eval(y.getAttribute('spawnY')),eval(y.getAttribute('declenchement')),eval(y.getAttribute('sens')),eval(y.getAttribute('timer'))]]
        res+=[res2]
    return res

#print(str(loadMap('map1.xml')))

#----------------------------------------------------------------------------------#

#Chargement des constantes

def loadData():
    doc=minidom.parse('data/data.xml')
    root=doc.documentElement
    dico={}
    dico[root.getElementsByTagName('gameName')[0].getAttribute('name')]=root.getElementsByTagName('gameName')[0].getAttribute('value')
    
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('optionsMenuPrincipal')[0].getElementsByTagName('option'):
        dico[x.getAttribute('name')]=int(x.getAttribute('n'))
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('tailles')[0].getElementsByTagName('taille'):
        dico[x.getAttribute('name')]=int(x.getAttribute('value'))
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('optionsMenuVaisseau')[0].getElementsByTagName('option'):
        dico[x.getAttribute('name')]=int(x.getAttribute('n'))
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('optionsChoixJoueurs')[0].getElementsByTagName('option'):
        dico[x.getAttribute('name')]=int(x.getAttribute('n'))
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('ath')[0].getElementsByTagName('position'):
        dico[x.getAttribute('name')]=tuple(map(int,x.getAttribute('posi').split(',')))
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('general')[0].getElementsByTagName('sprite'):
        dico[x.getAttribute('name')]=x.getAttribute('src')
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('general')[0].getElementsByTagName('sprite'):
        dico[x.getAttribute('name')]=x.getAttribute('src')
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('joueurs')[0].getElementsByTagName('sprite'):
        dico[x.getAttribute('name')]=x.getAttribute('src')
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('menu')[0].getElementsByTagName('sprite'):
        dico[x.getAttribute('name')]=x.getAttribute('src')
    for x in root.getElementsByTagName('commandes')[0].getElementsByTagName('commande'):
        dico[x.getAttribute('id')]=eval(x.getAttribute('value'))
    for x in root.getElementsByTagName('commandes')[0].getElementsByTagName('commande'):
        dico[x.getAttribute('id')]=eval(x.getAttribute('value'))
    for x in root.getElementsByTagName('sons')[0].getElementsByTagName('son'):
        dico[x.getAttribute('name')]=x.getAttribute('src')
    for x in root.getElementsByTagName('divers')[0].getElementsByTagName('etc'):
        dico[x.getAttribute('name')]=int(x.getAttribute('value'))
    return dico
    

def loadData2(data):
    doc=minidom.parse(data)
    root=doc.documentElement
    
    gamename = root.getElementsByTagName('gameName')[0].getAttribute('name')
    
    tailles = []
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('tailles')[0].getElementsByTagName('taille'):
        tailles+=[tuple(map(int,x.getAttribute('taille').split(',')))]
    taillesMenus= list(map(int,[root.getElementsByTagName('screen')[0].getElementsByTagName('optionsMenuPrincipal')[0].getAttribute('taille'),root.getElementsByTagName('screen')[0].getElementsByTagName('optionsMenuVaisseau')[0].getAttribute('taille')]))
    ordreMenus= []
    res=[]
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('optionsMenuPrincipal')[0].getElementsByTagName('option'):
        res+=[int(x.getAttribute('n'))]
    ordreMenus+=[res]
    res=[]
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('optionsMenuVaisseau')[0].getElementsByTagName('option'):
        res+=[int(x.getAttribute('n'))]
    ordreMenus+=[res]
    res=[]
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('optionsChoixJoueurs')[0].getElementsByTagName('option'):
        res+=[int(x.getAttribute('n'))]
    ordreMenus+=[res]
    ath=[]
    for x in root.getElementsByTagName('screen')[0].getElementsByTagName('ath')[0].getElementsByTagName('position'):
        ath+=[tuple(map(int,x.getAttribute('posi').split(',')))]
    screen=[tailles,taillesMenus,ordreMenus,ath]
    
    general=[]
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('general')[0].getElementsByTagName('sprite'):
        general+=[x.getAttribute('src')]
    spritesJoueurs=[]
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('joueurs')[0].getElementsByTagName('sprite'):
        y=x.getElementsByTagName('anime')[0]
        z=x.getElementsByTagName('invu')[0]
        spritesJoueurs+=[[[y.getAttribute('src1'),y.getAttribute('src2'),y.getAttribute('src3')],[z.getAttribute('src1'),z.getAttribute('src2'),z.getAttribute('src3')]]]
        
    spritesMenu=[]
    for x in root.getElementsByTagName('sprites')[0].getElementsByTagName('menu')[0].getElementsByTagName('sprite'):
        spritesMenu+=[x.getAttribute('src')]
    sprites=[general,spritesJoueurs,spritesMenu]
    
    comJ1=[]
    comJ2=[]
    for x in root.getElementsByTagName('commandes')[0].getElementsByTagName('joueur')[0].getElementsByTagName('commande'):
        comJ1+=[x.getAttribute('value')]
    for x in root.getElementsByTagName('commandes')[0].getElementsByTagName('joueur')[1].getElementsByTagName('commande'):
        comJ2+=[x.getAttribute('value')]
    commandes=[comJ1,comJ2]
    
    sons=[]
    for x in root.getElementsByTagName('sons')[0].getElementsByTagName('son'):
        sons+=[x.getAttribute('src')]
        
    divers=[]
    for x in root.getElementsByTagName('divers')[0].getElementsByTagName('etc'):
        divers+=[x.getAttribute('value')]
        
    return [gamename,screen,sprites,commandes,sons,divers]

#print(loadData('data.xml'))




























