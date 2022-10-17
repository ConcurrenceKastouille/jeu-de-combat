                        # Classe Personnages

class Personnages:

    def __init__(self, vie, dgt, nom):
        self.__vieperso = vie
        self.__dgtperso = dgt
        self.__nom = nom

    def etat(self):
        return self.__vieperso

    def setEtat(self, etatnew):
        self.__vieperso = etatnew

    def donneDegat(self):
        return self.__dgtperso

    def setDegat(self, dgt):
        self.__dgtperso += dgt

    def perdVie(self, perd):
        self.setEtat(self.etat() - perd)

    def donneNom(self):
        return self.__nom

                        # Fonction game()

from random import randint, choice
from time import sleep

def game():

    #Sélection des personnages

    print("......................Sélection des Personnages......................")
    print("")
    print("Choix 1 : Nom -> Paysan | Vie -> entre 20 et 30 points de vie | Dégâts -> entre 2 et 3 dégâts")
    print("Choix 2 : Nom -> Roi | Vie -> entre 30 et 40 points de vie | Dégâts -> entre 3 et 4 dégâts")
    print("Choix 3 : Nom -> Viking | Vie -> entre 60 et 70 points de vie | Dégâts -> entre 4 et 5 dégâts")
    print("Choix 4 : Nom -> Dieu | Vie -> entre 120 et 140 points de vie | Dégâts -> entre 8 et 10 dégâts")

    choix = int(input("Joueur 1 : Choisissez votre personnage : 1,2,3 ou 4"))

    print("")

    if choix == 1:
        joueur1 = Personnages(Paysan.etat(), Paysan.donneDegat(), Paysan.donneNom())
        print("Joueur 1 a choisi le Paysan pour son personnage.")
    elif choix == 2:
        joueur1 = Personnages(Roi.etat(), Roi.donneDegat(), Roi.donneNom())
        print("Joueur 1 a choisi le Roi pour son personnage.")
    elif choix == 3:
        joueur1 = Personnages(Viking.etat(), Viking.donneDegat(), Viking.donneNom())
        print("Joueur 1 a choisi le Viking pour son personnage.")
    elif choix == 4:
        joueur1 = Personnages(Dieu.etat(), Dieu.donneDegat(), Dieu.donneNom())
        print("Joueur 1 a choisi le Dieu pour son personnage.")

    choix2 = int(input("Joueur 2 : Choisissez votre personnage : 1,2,3 ou 4"))

    print("")

    if choix2 == 1:
        joueur2 = Personnages(Paysan.etat(), Paysan.donneDegat(), Paysan.donneNom())
        print("Joueur 2 a choisi le Paysan pour son personnage.")
    elif choix2 == 2:
        joueur2 = Personnages(Roi.etat(), Roi.donneDegat(), Roi.donneNom())
        print("Joueur 2 a choisi le Roi pour son personnage.")
    elif choix2 == 3:
        joueur2 = Personnages(Viking.etat(), Viking.donneDegat(), Viking.donneNom())
        print("Joueur 2 a choisi le Viking pour son personnage.")
    elif choix2 == 4:
        joueur2 = Personnages(Dieu.etat(), Dieu.donneDegat(), Dieu.donneNom())
        print("Joueur 2 a choisi le Dieu pour son personnage.")

    print("......................Lancement du combat......................")
    print("")

    while joueur1.etat() > 0 and joueur2.etat() > 0:

        #Donne les caractéristiques des deux personnages à chaque manche

        print("Joueur 1 : Vie ->", joueur1.etat(), "| Dégât ->", joueur1.donneDegat())
        print("Joueur 2 : Vie ->", joueur2.etat(), "| Dégât ->", joueur2.donneDegat())
        print("")

        #Choix de l'action du joueur 1

        a = input("Au tour du joueur 1, choisi ton action : attaque (attaquer) , regen (reprendre de la vie), upattaque (augmenter ses dégâts)")

        while a != "attaque" and a != "regen" and a != "upattaque":
            print(" /!\ Vous n'avez pas fait une action proposée /!\ ")
            a = input("Choisis ton action : attaque (attaquer) , regen (reprendre de la vie), upattaque (augmenter ses dégâts)")

        print("")

        #Augmente l'attaque du joueur 1

        if a == "upattaque":
            c = randint(1,3)
            print("Les dégâts de joueur 1 ont augmenté de", c)
            joueur1.setDegat(c)

        #Augmente la vie du joueur 1

        elif a == "regen":
            c = randint(1,4)
            print("La vie de joueur 1 a augmentée de", c)
            joueur1.setEtat(joueur1.etat() + c)

        #Le joueur 1 attaque le joueur 2

        else:
            joueur2.perdVie(joueur1.donneDegat())
            print("Joueur 2 a pris", joueur1.donneDegat(), "de dégâts.")

        #Donne les caractéristiques des deux personnages à chaque manche

        sleep(1.5)
        print("")
        print("Joueur 1 : Vie ->", joueur1.etat(), "| Dégât ->", joueur1.donneDegat())
        print("Joueur 2 : Vie ->", joueur2.etat(), "| Dégât ->", joueur2.donneDegat())
        print("")

        #Choix de l'action de joueur 2

        z = input("Au tour du joueur 2, choisi ton action : attaque (attaquer) , regen (reprendre de la vie), upattaque (augmenter ses dégâts)")

        while z != "attaque" and z != "regen" and z != "upattaque":
            print(" /!\ Vous n'avez pas fait une action proposée /!\ ")
            z = input("Choisis ton action : attaque (attaquer) , regen (reprendre de la vie), upattaque (augmenter ses dégâts)")

        print("")

        #Augmente l'attaque du joueur 2

        if z == "upattaque":
            c = randint(1,3)
            print("Les dégâts de joueur 2 ont augmenté de", c)
            joueur2.setDegat(c)

        #Augmente la vie du joueur 2

        elif z == "regen":
            c = randint(1,4)
            print("La vie de joueur 2 a augmentée de", c)
            joueur2.setEtat(joueur2.etat() + c)

        #Le joueur 2 attaque le joueur 1

        else:
            joueur1.perdVie(joueur2.donneDegat())
            print("Joueur 1 a pris", joueur2.donneDegat(), "de dégâts.")

        sleep(1.5)
        print("")

    if joueur1.etat() <= 0 and joueur2.etat() > 0:
        print("Victoire du joueur 2 ! Le combattant", joueur2.donneNom(), "vient de gagner le combat ! Il lui reste", joueur2.etat(), "points de vie.")
        return None
    if joueur2.etat() <= 0 and joueur1.etat() > 0:
        print("Victoire du joueur 1 ! Le combattant", joueur1.donneNom(), "vient de gagner le combat ! Il lui reste", joueur1.etat(), "points de vie.")
        return None
    else:
        print("Match nul ! Les deux combattants sont morts..")
        return None


                        # Tous les personnages

Paysan = Personnages(randint(20,30), randint(2,3), "Paysan")
Roi = Personnages(randint(30,40), randint(3,4), "Roi")
Viking = Personnages(randint(60,70), randint(4,5), "Viking")
Dieu = Personnages(randint(120,140), randint(8,10), "Dieu")
