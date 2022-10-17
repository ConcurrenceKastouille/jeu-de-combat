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

    choix = int(input("Choisissez votre personnage : 1,2,3 ou 4"))

    print("")

    if choix == 1:
        tonperso = Personnages(Paysan.etat(), Paysan.donneDegat(), Paysan.donneNom())
        print("Vous avez choisi le Paysan pour votre personnage.")
    elif choix == 2:
        tonperso = Personnages(Roi.etat(), Roi.donneDegat(), Roi.donneNom())
        print("Vous avez choisi le Roi pour votre personnage.")
    elif choix == 3:
        tonperso = Personnages(Viking.etat(), Viking.donneDegat(), Viking.donneNom())
        print("Vous avez choisi le Viking pour votre personnage.")
    elif choix == 4:
        tonperso = Personnages(Dieu.etat(), Dieu.donneDegat(), Dieu.donneNom())
        print("Vous avez choisi le Dieu pour votre personnage.")

    choix2 = int(input("Choisissez le personnage adversaire : 1,2,3 ou 4"))

    print("")

    if choix2 == 1:
        perso_adversaire = Personnages(Paysan.etat(), Paysan.donneDegat(), Paysan.donneNom())
        print("Vous avez choisi le Paysan pour votre adversaire.")
    elif choix2 == 2:
        perso_adversaire = Personnages(Roi.etat(), Roi.donneDegat(), Roi.donneNom())
        print("Vous avez choisi le Roi pour votre adversaire.")
    elif choix2 == 3:
        perso_adversaire = Personnages(Viking.etat(), Viking.donneDegat(), Viking.donneNom())
        print("Vous avez choisi le Viking pour votre adversaire.")
    elif choix2 == 4:
        perso_adversaire = Personnages(Dieu.etat(), Dieu.donneDegat(), Dieu.donneNom())
        print("Vous avez choisi le Dieu pour votre adversaire.")

    print("......................Lancement du combat......................")
    print("")

    while tonperso.etat() > 0 and perso_adversaire.etat() > 0:

        #Donne les caractéristiques des deux personnages à chaque manche

        print("Les caractéristiques actuelles de ton personnage sont: Vie ->", tonperso.etat(), "| Dégât ->", tonperso.donneDegat())
        print("Les caractéristiques actuelles du personnage de l'adversaire sont: Vie ->", perso_adversaire.etat(), "| Dégât ->", perso_adversaire.donneDegat())
        print("")

        #Choix de l'action du joueur

        a = input("Choisis ton action : attaque (attaquer) , regen (reprendre de la vie), upattaque (augmenter ses dégâts)")

        while a != "attaque" and a != "regen" and a != "upattaque":
            print(" /!\ Vous n'avez pas fait une action proposée /!\ ")
            a = input("Choisis ton action : attaque (attaquer) , regen (reprendre de la vie), upattaque (augmenter ses dégâts)")

        print("")

        #Augmente l'attaque du joueur

        if a == "upattaque":
            c = randint(1,3)
            print("Vos dégâts ont augmenté de", c)
            tonperso.setDegat(c)

        #Augmente la vie du joueur

        elif a == "regen":
            c = randint(1,4)
            print("Votre vie a augmentée de", c)
            tonperso.setEtat(tonperso.etat() + c)

        #Le joueur attaque l'ordinateur

        else:
            perso_adversaire.perdVie(tonperso.donneDegat())
            print("L'adversaire a pris", tonperso.donneDegat(), "de dégâts.")

        #Choix de l'action de l'ordinateur

        print("")
        print("L'adversaire choisi une action..")
        sleep(2)
        print("")

        b = choice(["attaque", "regen", "upattaque"])

        #Augmente l'attaque de l'ordinateur

        if b == "upattaque":
            c = randint(1,3)
            print("Les dégâts de votre adversaire ont augmenté de", c)
            perso_adversaire.setDegat(c)

        #Augmente la vie de l'ordinateur

        elif a == "regen":
            c = randint(1,4)
            print("La vie de votre adversaire a augmentée de", c)
            perso_adversaire.setEtat(perso_adversaire.etat() + c)

        #L'ordinateur attaque le joueur

        else:
            tonperso.perdVie(perso_adversaire.donneDegat())
            print("Tu as pris", perso_adversaire.donneDegat(), "de dégâts.")

        sleep(1.5)
        print("")

    if tonperso.etat() <= 0 and perso_adversaire.etat() > 0:
        print("Défaite ! Le combattant", perso_adversaire.donneNom(), "vient de gagner le combat ! Il lui reste", perso_adversaire.etat(), "points de vie.")
        return None
    if perso_adversaire.etat() <= 0 and tonperso.etat() > 0:
        print("Victoire ! Le combattant", tonperso.donneNom(), "vient de gagner le combat ! Il lui reste", tonperso.etat(), "points de vie.")
        return None
    else:
        print("Match nul ! Les deux combattants sont morts..")
        return None


                        # Tous les personnages

Paysan = Personnages(randint(20,30), randint(2,3), "Paysan")
Roi = Personnages(randint(30,40), randint(3,4), "Roi")
Viking = Personnages(randint(60,70), randint(4,5), "Viking")
Dieu = Personnages(randint(120,140), randint(8,10), "Dieu")




