import time

import sys

import random

class test():
   for_te = 10
   agi_te = 10
   vie_te = 10
   int_te = 10

class Aventurier():
   for_av = 6
   agi_av = random.randint(4,5)
   vie_av= 6
   int_av = random.randint(3,4)

class Alchimiste():
   for_al = random.randint(5,6)
   agi_al = 4
   vie_al = random.randint(3,4)
   int_al = random.randint(6,8)

class Assassin():
   for_as = random.randint(7,10)
   agi_as = random.randint(8,10)
   vie_as = random.randint(2,3)
   int_as = random.randint(5,7)

class Pirate():
   for_pi = random.randint(7,8)
   agi_pi = random.randint(3,5)
   vie_pi = random.randint(6,8)
   int_pi = random.randint(1,3)

class Archer():
   for_ar = random.randint(6,8)
   agi_ar = random.randint(6,8)
   vie_ar = random.randint(3,4)
   int_ar = random.randint(4,6)

class Mage():
   for_ma = 6
   agi_ma = random.randint(2,3)
   vie_ma = random.randint(6,7)
   int_ma = random.randint(8,10)

class Gambler():
   for_ga = random.randint(1,9)
   agi_ga = random.randint(1,9)
   vie_ga = random.randint(1,9)
   int_ga = random.randint(1,9)


def delay_print(s):
   for c in s:
       sys.stdout.write(c)

       sys.stdout.flush()

       time.sleep(0.01)


intro = "Bienvenue voyageur, vous vous apprêtez à pénétrer dans l’Antre du Dragon. Nombre d’histoires circulent sur ce lieu jonché, par le passé, de cadavres et de sang.", "Alors que vous vous engouffrez dans la pénombre, 7 portes se dévoilent sous vos yeux. Chacune d’entre elles présentant un emblème en son centre.","Que choisirez-vous noble visiteur : l’épée (choisir Aventurier), l’arc (choisir Archer), la dague (choisir Assassin), la baguette(choisir Mage),","le mousquet (choisir Pirate), la potion (choisir Alchimiste) ou enfin, le dé (choisir Gambler) ?"

slow_intro = "\n".join(intro)
delay_print(slow_intro)

choix = str(input("\nFaites votres choix : "))
print("Vos stats sont :")
if choix == "test":
   print("Force :", test.for_te, "Agilité :", test.agi_te, "Vie :", test.vie_te, "Intelligence :", test.int_te)
   For = test.for_te
   Agi = test.agi_te
   Vie = test.vie_te
   Int = test.int_te
if choix == "Pirate":
   print("Force :", Pirate.for_pi, "Agilité :", Pirate.agi_pi, "Vie :", Pirate.vie_pi, "Intelligence :", Pirate.int_pi)
   For = Pirate.for_pi
   Agi = Pirate.agi_pi
   Vie = Pirate.vie_pi
   Int = Pirate.int_pi
if choix == "Aventurier":
   print("Force :", Aventurier.for_av, "Agilité :", Aventurier.agi_av, "Vie :", Aventurier.vie_av, "Intelligence :", Aventurier.int_av)
   For = Aventurier.for_av
   Agi = Aventurier.agi_av
   Vie = Aventurier.vie_av
   Int = Aventurier.int_av
if choix == "Mage" :
   print("Force :", Mage.for_ma, "Agilité :", Mage.agi_ma, "Vie :", Mage.vie_ma, "Intelligence :", Mage.int_ma)
   For = Mage.for_ma
   Agi = Mage.agi_ma
   Vie = Mage.vie_ma
   Int = Mage.int_ma
if choix == "Assassin" :
   print("Force :", Assassin.for_as, " Agilité :", Assassin.agi_as, " Vie :", Assassin.vie_as, " Intelligence :", Assassin.int_as)
   For = Assassin.for_as
   Agi = Assassin.agi_as
   Vie = Assassin.vie_as
   Int = Assassin.int_as
if choix == "Gambler" :
   print("Force :", Gambler.for_ga, " Agilité :", Gambler.agi_ga, " Vie :", Gambler.vie_ga, " Intelligence :", Gambler.int_ga)
   For = Gambler.for_ga
   Agi = Gambler.agi_ga
   Vie = Gambler.vie_ga
   Int = Gambler.int_ga
if choix == "Alchimiste" :
   print("Force :", Alchimiste.for_al," Agilité :", Alchimiste.agi_al," Vie :", Alchimiste.vie_al," Intelligence :", Alchimiste.int_al)
   For = Alchimiste.for_al
   Agi = Alchimiste.agi_al
   Vie = Alchimiste.vie_al
   Int = Alchimiste.int_al
if choix == "Archer" :
   print("Force :", Archer.for_ar, " Agilité :", Archer.agi_ar, " Vie :", Archer.vie_ar, " Intelligence :", Archer.int_ar)
   For = Archer.for_ar
   Agi = Archer.agi_ar
   Vie = Archer.vie_ar
   Int = Archer.int_ar

Salle_1 = "Tandis que vous appréhendez les épreuves qui se dresseront devant vous, des flambeaux s’allument les uns après les autres tout autour de vous.","Quelques secondes de silence sont ensuite interrompues par des cris stridents et irréguliers. Vous faites maintenant face à 3 gobelins."

slow_salle1 = "\n".join(Salle_1)
delay_print(slow_salle1)

print("""
                                       . =#@#@@@@@@@@@@@%#-..   :=*#@@@@@@@=
                                     .+%@@@@@@@@@@@@@@@@%%=..-*@@##%@@@@@%.
                                    +@@@@@@@@@@@@@@@@@@%*=.+@@@%+@@@@@@@%.
                                  .%@@@@@@@@@@@@@@@@@%*- +@@@%+=#%@@@%#*:--:
                                 -@@@@@@@@@@@%@@@@@@@@*: %@@*    -@@*+%#*+.
                                .@@@#@@@@@@@#++@@@@@@@@==@@%   .+@@%*%%%@@@+----:
                                =@@@%@@@*#*-:+%@@@@@@@@= *@%*%@@####@%@@@@@%##+-..           =*
                                +@@@@@@-+*:+%@@@@@@@@@@= +@@@@@@@%@@@@@@@@@@@@@@@@%***++*:-**@#-=+#*-..+@:
                             .=#@@@@@*#==##@@@@@@@@@@@@*:%@=+#%#@@@@@@@@@@@@@@@@@@@@@##***%@@@%%%%%%@@@@%*
                           .::.#@%@@%+#%@@@@@@@@@@@@@@@@@@@+-=@@@@@@@@@@@@@@@@@@@.-*%@@@@@@@@@@@@@@@@%%@%%=.
                               .+%@@%@@@@@@@#+%@@@@@@@@@@@@%:@@@@@@@@@@@@%@@@@@@=#@@@@@@@@@@@@@@@@@@@@@@@@@@+
                                -@@@@@@@@@@*%@@@@@@@@@@@@@#-:@@@@@@@@@@@@@@@@@@#%@@@@@@@@@%@@##*@@@@@@@@@@@@@*
                             :+%@@@@@@#=--==@@@@%#@%@@@@@:.:#@@@@@@@@@@@@@@@@@%@@@@@#@@@@@%%@@@*@@@@@@@%@@@@@@=
                           =@@@@@@@@@##@#**#+#@@@@@%@@@=+:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@%%@@@@@@@=
                           .*@@@@%#-  .@@@++@@@@@%%@%%.=*=@@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@%.
                              ..       :*=:@%@%@@@#+=.=*=-%@@@@@@@@@@@=*+%####%###%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@-
                                         .*@*=+*=.:  :==--+@@@@@#+%@@@%#+#%@@@@@@@@@@@@@@@@@@%@@@@%@@@@@@@@@@@@@*-
                                         **+.:=. -:--*@@@*:%@@@@%-=#%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@%@%:
                                       *%@::-.=  =##% +@@@%=@@@@% -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@=
                                     .%@@%*+ :-:+@@@=. +@@@#@@@@* #@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
                                    .@@@@@#%  **@@@@*  .@@@@@@@@+%@@@@@@%##@@@@@@@@@@@@@@@@@@@@@@@@%#%@@@@@@@@@@@@@@@#
                                    #@@%%@@@-*@@@@@@@- :@@@@@%#%@@%@%*#*#@@@@@@@@@@@@@@@@%%%%@@@%*=*@@@@@@@@@@@@@@@@@@.
                                   .@@@@@@@@@%@@@@@@@@+=@@@@#@@@@#@@@@@@@@@@@@@@@@@#*==:..:#@@@@%..%@@@@@@@#@@@@@@@@@@-
""")

Salle_1b = "Que faites-vous dans cette situation ?","Vous attaquez physiquement (Attaque), vous lancez un sort de soin (Sort), ou bien essayez d'esquiver (Esquive) ?"

slow_salle1b = "\n".join(Salle_1b)
delay_print(slow_salle1b)

vie_max = Vie

for_go = 3

def dé() :
    x = random.randint(1,12)
    print("\nRésultat du dé :", x)
    return x

nb_gobelin=3
mort = "Le coup vous est mortel, vous avez échoué...","Pour cette fois..."


while nb_gobelin > 0 :
    choix_2 = str(input("\nFaites votres choix : "))
    if choix_2 == "Attaque":
        if For >= dé() :
            dégât = random.randint(1,nb_gobelin)
            print("Vous réussissez et tuez", dégât, "gobelin(s)")
            if dégât < 3 :
                nb_gobelin -= dégât
            if dégât == 3 :
                nb_gobelin = 0
        else :
            delay_print("Vous avez attaqué et raté votre coup lamentablement")
    if choix_2 == "Sort":
        if Int >= dé() :
            if vie_max - Vie >= 2 :
               Vie += 2
               print("Vous décidez de lancer un sort de soin et récupérez 2 points de vie ! Vous en avez",Vie)
            if vie_max - Vie == 0 :
               print("Vous êtes déjà en pleine forme !")
               continue
        else :
            delay_print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
    if choix_2 == "Esquive" :
        if Agi >= dé():
            print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
            for_go = 0
        else :
            print("L'ennemi est trop rapide, vous n'arriverez pas à esquiver !")
    if nb_gobelin > 0 :
        delay_print("\nL'ennemi attaque !")
        if for_go >= dé() :
            Vie -= nb_gobelin
            print("L'ennemi vous a touché, vous subissez", nb_gobelin,"points de dégat(s) !")
            if Vie > 0:
                print("Il vous reste", Vie, "pv(s)")
            elif Vie <= 0 :
                delay_print(mort)
                quit()
        else :
            delay_print("L'attaque a raté !")
    for_go = 3

delay_print("Vous avez triomphé ! Vous pouvez maintenant poursuivre votre avancée.")

delay_print("\nDésirez-vous avancer (Salle 2) ou bien, miser sur votre destin (Salle mystère) ?")

choix_3 = str(input("\nFaites votres choix : "))
nb_fauves = 2
for_fa = 4
vie_fa = 2

salle_2 = "\nVous entendez soudainement un bruit sourd et lointain qui s'apparente à des grognements. Vous prenez alors la décision de poursuivre votre chemin malgré l’obscurité.","Désormais, vous vous trouvez face à deux bêtes féroces qui s’apprêtent à vous dévorer jusqu’aux os.","Leurs mâchoires saillantes et fielleuses ainsi que leurs regards remplis de rage ne laissent aucun doute quant à l’adversité qui vous guettera durant cette épreuve. Pensez-vous y arriver ?","Ils se tiennent devant vous.","Que faites-vous dans cette situation ? Vous attaquez (Attaque), vous lancez un sort de soin (Sort), ou bien essayez d'esquiver (Esquive) ?"
sallemyst = "\nVous faites face à quelqu'un qui ressemble comme deux gouttes d'eau au Père Fourras. Dès l'instant où il vous voit, il vous dit:","Bonsoir cher aventurier, voulez-vous répondre à une question? Attention à votre choix car si vous répondez faux, vous riquez de perdre un peu de vie,","mais si vous répondez bien, je vous rendrai incroyablement puissant"

if choix_3 == "Salle mystère":
    sallemyst = "\n".join(sallemyst)
    delay_print(sallemyst)
    if Int >= dé():
        delay_print("\nJe vais baisser la difficulté de ma question car je vous sens très intéressé des avantages")
        delay_print("\nVoici mon énigme: 2+2 ?")
        réponse = str(input(" Votre réponse : "))
        if réponse == "4":
            delay_print("\nBravo, vous avez réussi à triompher de ma terrible énigme, quelle attribut voulez-vous augmenter ?")
            boost = str(input(" Force, Agilité, Vie, Intelligence ? : "))
            if boost == "Force":
                For += 1
                print("Vous sentez vos muscles se raffermir, votre force augmente :", For)
            if boost == "Agilité":
                Agi += 1
                print("Vous vous sentez beaucoup plus léger, votre agilité augmente :",Agi)
            if boost == "Vie":
                vie_max += 1
                print("Votre corps devient plus résistant, votre vie augmente :",vie_max)
            if boost == "Intelligence":
                Int += 1
                print("Vous discernez mieux les détails de votre environnement, votre intelligence augmente :",Int)
        else :
            delay_print("Vous n'êtes pas aussi intelligent que vous en avez l'air, je vous retire un point de vie pour la peine.")
            Vie -= 1
            print(Vie)
    else :
        delay_print("\nVoici mon énigme: Quelle est le 39ème élément du tableau périodique ? ")
        réponse = str(input(" Votre réponse : "))
        if réponse == "Yttrium":
            delay_print("Wow, vous avez triché mais bien joué !")
            delay_print("\nQuelle attribut voulez-vous augmenter ?")
            boost = str(input("\nForce, Agilité, Vie, Intelligence ? "))
            if boost == "Force" :
                For +=1
                print("Vous sentez vos muscles se raffermir, votre force augmente :",For)
            if boost == "Agilité":
                Agi +=1
                print("Vous vous sentez beaucoup plus léger, votre agilité augmente :",Agi)
            if boost == "Vie":
                vie_max +=1
                print("Votre corps devient plus résistant, votre vie augmente :",vie_max)
            if boost == "Intelligence":
                Int+=1
                print("Vous discernez mieux les détails de votre environnement, votre intelligence augmente :",Int)
        else :
            Vie -= 1
            delay_print("\nJe m'attendais à cette issue, je vous enlève quand même un point de vie :",Vie)
        for_fa = 5
    delay_print("\nVous avancez maintenant vers la suite du donjon")
    choix_3 = "Salle 2"

if choix_3 == "Salle 2":
    salle_2 = "\n".join(salle_2)
    delay_print(salle_2)
    print("""
----==+++**####%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
--==++++***##%%%@@@@@@@@@@@@@@@@@@@@@@@@-=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
==++++***####%%%@@@@@@@@@@@@@@@@@@@@@@@@=  :+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
++***#####%%%@@@@@@@@@@@@@@@@@@@@@@@@%%#+.     .-*#++*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
***###%%%%@@@@@@@@@@@@@@@@@@%*++*+- . .                 :+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
####%%%%@@@@@@@@@@@@@@@@@#=-.                             :--+#@@@@@@@@@@@@@@@@@@@@@@@@@@@
%%%%%@@@@@@@@@@@@@@@@@#=.                                    ...+@@@@@@@@@@@@@@@@@@@@@@@@@
%%%@@@@@@@@@@@@@@@@%=:                                       -::::*@@@@@@@@@@@@@@@@@@@@@@@
%@@@@@@@@@@@@@@@@@+.                                         .     +@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%#+.                                                     :*%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@+-:.          .                                           .=%*=+@@@@@@@@@@@@@@@@
@@@@@@@@+.   :=*###-. ::                                              +#. .*@@@@@@@@@@@@@@
@@@@@@@+   .=*#****=.=*=-.                                                 :@@@@@@@@@@@@@@
@@@@@+:   .  .:===*-:**+=.                                                =@@@@@@@@@@@@@@@
@@@#=..::..     .++:-=+*=                                     *%+%*-= :.+@@@@@@@@@@@@@@@@@
@#=.              .:=*=+=.                                    +@@@@@@#+-@@@@@@@@@@@@@@@@@@
@-                  --=+-.                                  .+%+@@@@@@%@@@@@@@@@@@@@@@@@@@
*                  .=-=-:                           ::.      .:-%@@@@@@@@@@@@@@@@@@@@@@@@@
:                  -===                         .=+%@@@@%*:     . :%@@@@@@@@@@@@@@@@@@@@@@
                    .=*                         #@@@@@@@@@@@*:   +#@@@@@@@@@@@@@@@@@@@@@@@
.   :.              :+.                        .%@@@@@@@@@@@@@%#%@@@@@@@@@@@@@@@@@@@@@@@@@
   .:.         .:   -=                         -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%
    """)
    while nb_fauves > 0 :
        choix_4 = str(input("\nFaites votres choix : "))
        if choix_4 == "Attaque":
            if For >= dé():
               vie_fa -= 1
               print("Vous avez touché votre cible !")
            elif For < dé():
               print("Vous avez attaqué et raté votre coup lamentablement")
        if choix_4 == "Sort":
            if Int >= dé() :
                if vie_max - Vie >= 2 :
                    Vie += 2
                    print("Vous décidez de lancer un sort de soin et récupérez 2 points de vie ! Vous en avez",Vie)
                if vie_max - Vie == 0 :
                    print("Vous êtes déjà en pleine forme ! Vous en avez", Vie)
                    continue
            else :
                delay_print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
        if choix_2 == "Esquive":
            if Agi >= dé() :
                print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
                for_fa = 0
            else:
                print("L'ennemi est trop rapide, vous n'arriverez pas à esquiver !")
        if vie_fa == 0 :
            print("La bête succombe de ses blessures et tombe !")
            nb_fauves -= 1
            vie_fa = 2
        if nb_fauves > 0 :
            print("L'ennemi attaque !")
            if for_fa >= dé() :
                Vie -= nb_fauves
                print("L'ennemi vous a touché, vous subissez", nb_fauves,"points de dégat(s) !")
                if Vie > 0:
                    print("Il vous reste", Vie, "pv(s)")
                elif Vie <= 0 :
                    delay_print(mort)
                    quit()
            else :
                delay_print("L'attaque a raté !")

print("\nVous avez une nouvelle fois gagné, où voulez-vous vous diriger ? La Salle 3 ou bien vers la Salle Annexe ? : ")
choix_5 = str(input("Faites votre choix : "))
salle_min = "C’est après ces rudes épreuves que vous vous rapprochez de l’avant-dernier combat.", "Vos pas et votre respiration deviennent de plus en plus lourds, à l'instar de l’atmosphère environnante. Dès l’instant où vous entrez dans la salle, une silhouette gigantesque engloutit la salle.","L'obscurité est telle qu’il est impossible de se repérer. Deux sources de lumière se dressent au-dessus de vous.", "Cette obscurité provient en réalité de l’ombre du monstre que vous allez combattre durant cette épreuve.", "C'est une créature hybride à tête de taureau et pourvue de cornes : Le Minotaure."
slow_sallemin = "\n".join(salle_min)


vie_mi = 12
for_mi = 5

if choix_5 == "Salle Annexe":
        delay_print("Vous entrez dans la salle de la fontaine de vie, vous pouvez boire l'eau de la fontaine pour régénerer toute votre vie")
        f = str(input("\nVoulez-vous vous arrêter à cette fontaine (Oui) ou passer votre chemin (Non) ? "))
        if f == "Non":
            delay_print("Soucieux d'un potentiel piège, vous décidez de passer votre chemin.")
        if f == "Oui":
            delay_print("Vous décidez de saisir cette chance et buvez de cette eau. Vous récupérez votre énergie mais vous sentez également plus faible.")
            Vie = vie_max
            For -= 1
            print("Votre force diminue de 1 point :",For)
        choix_5 = "Salle 3"

if choix_5 == "Salle 3" :
    delay_print(slow_sallemin)
    print("""
                                                                            :#.
                                                           .=*#%@@#+:      =@@.
                                                        .+%@@@@@@@@@@#=. :#@@*
                                                      :*@@@%*+=+#@@@@@@@@@@@@.
                                                    .*@@@@@##+=-.:+%@@@@@@@*.
                                                  .*@@@@@@%+.       :+**+:
                                               .-#@@@@@@%=.
                     :=*##%%%%##**+=:.  ..:-=*@@@@@#%%#=.
                  -#@@@@@@@@####@%@%#%@@@@@@@@@@@@@@#+.
                .#@@@@@@#*+=--:...:-:*%@@@@@@@@@@@@@@##%@%:
               :%@@@@@#=.            :=%@@@@@@@@@@@@@@@@@-
              =@@@@@%-               .:@@@@@@@@@@@#@@@@@@%+:
    :=**+=-==*@@@@@@*.              ... -*%%@@@@@@@@@@@@@@@@@%=.
      .-*%@@@@@@%#+:                 .:::.-@@@@@@@@@@@@@@@@@@@@@#+%#=:
          ...:..                       .+:-=+@@%%@@@@@@@@@@@@@@@@@@@%%%+.
                                      +%+:.:=-+#@@@@@@**@@@@@@@@@@@@@@%%%=
                                   .+@@*+. ..=**#%%-..*@@@@@@@@@@@@@@@@%%#*.
                                  :%@@+=::.   :=--.:+@@@@@@@@@@@@@@@@@@@%#**
                                  *-:*%+#+..   . :=+%@@@@@%%@@@@@@@@@@@@%#**-
                                 .:.+.++=--:. ..:=#@@@@@@@@@%%@@@@@@@@@@%#*++
                                  .-..-:.:::-=*@@@@@@@@@%@@@@@###%%#*%%#*+==*
                                  .   *+####%@%@%@@@@@@@@@%#*** .-=+*###+-:++
                                 -+.. :*###%%@@@%@@@@@@@@@@@@@@+#%@@@@@@@@@%%=
                                .--=. .-+**#%@@@%%%%%@@@%%@%@@#-=#%@@@@@@@@@#%-
                                :-.:   .-++#%%%###+##%%%%%@%#*:#=-+*@@@@@@@#+@%-
    """)
    print("Il se tient devant vous. Que voulez-vous faire : Attaque, Sort ou Esquive ?")
    while vie_mi > 0:
        choix_6 = str(input("\nFaites votre choix : "))
        if choix_6 == "Attaque":
            if For >= dé():
                vie_mi -= random.randint(1, 3)
                delay_print("Vous avez touché votre cible !")
                if vie_mi > 0 :
                    print("Il lui reste ", vie_mi," pv(s) !")
            elif For < dé():
                delay_print("Vous avez attaqué et raté votre coup lamentablement")
        if choix_6 == "Sort":
            if Int >= dé():
                if vie_max - Vie >= 2:
                    Vie += 2
                    delay_print("Vous décidez de lancer un sort de soin et récupérez 2 points de vie ! Vous en avez",Vie)
                if vie_max - Vie == 1:
                    Vie += 1
                    delay_print("Vous décidez de lancer un sort de soin et récupérez 1 point de vie ! Vous en avez",Vie)
                if vie_max - Vie == 0:
                    delay_print("Vous êtes déjà en pleine forme !")
                    continue
            else:
                delay_print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
        if choix_6 == "Esquive":
            if Agi >= dé():
                delay_print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
                for_mi = 0
            else:
                delay_print("L'ennemi est trop rapide, vous n'arriverez pas à esquiver !")
        if vie_mi == 0:
           delay_print("La colosse succonbe de ses blessures et tombe !")
        if vie_mi > 0:
            delay_print("L'ennemi attaque !")
            if for_mi >= dé():
                dégat_1 = random.randint(1, 3)
                Vie -= dégat_1
                print("L'ennemi vous a touché, vous subissez", dégat_1, "points de dégat(s) !")
                if Vie > 0:
                    print("Il vous reste", Vie, "pv(s)")
                elif Vie <= 0:
                    delay_print(mort)
                    quit()
            else:
             delay_print("L'attaque a raté !")
        for_mi = 5
delay_print("\nVous avez gagné ! Vous récupérez sur son cadavre une pierre d'âme permettant de vous octroyer un bonus et une sorte de diamand.")
choix_7 = str(input("\nVoulez-vous soigner (Soin), gagner 1 de Force (Force) 1 d'Agilité (Agilité) ou 1 d'Intelligence (Intelligence) ?"))
if choix_7 == "Soin":
    Vie = vie_max
    print("Vous avec maintenant", Vie, "points de vie.")
if choix_7 == "Force":
    For += 1
    print("Vous avez maintenant", For, "de force.")
if choix_7 == "Agilité":
    Agi += 1
    print("Vous avez maintenant", Agi, "d'agilité.")
if choix_7 == "Intelligence":
    Int += 1
    print("Vous avez maintenant", Int, "d'intelligence.")

for_drg = 6
vie_drg = 30

transition = "Vous avez vaincu énormément de monstres et maintenant, une porte terrifiante d'une hauteur inestimable se dresse devant vous","Des cadavres en bloquent l'ouverture.","Il est impossible de l'ouvrir. En cherchant un moyen d'avancer vous remarquez une porte minuscule. Vous decidez d'y pénétrer"

salle_finale = "\nVous voilà enfin arrivé, votre destin était de vous retrouver ici et une immense porte symbolise le dernier rempart à votre victoire."," Après une grande inspiration, vous décidez de la franchir, cœur battant et arme fermement tenue."," Une chaleur étouffante vous submerge tandis que vous le voyez, au fond, vous transperçant de son regard vif et faisant trembler le sol de son pas lourd."," Cette figure immense, ailée et parsemée d’écailles acérées s’approche de vous, l’ultime combat va commencer !"

sallefinale="\n".join(salle_finale)
trans = "\n".join(transition)
delay_print(trans)

sallecoffre = "\nCet endroit a l’air d’être une ancienne salle des coffres.","Vous fouillez rapidement la salle et le contenu de chacun des coffres, mais celle-ci semble déjà avoir été pillée.","Cependant, au fond de la salle, une épée gigantesque est plantée dans le sol.","Au niveau de son manche, il y a comme un réceptacle. Le seul objet ayant l'air d'y convenir est le diamant récupéré sur le Minotaure.","Une fois placé, l'épée vous est accessible et vous paraît si légère."," Le destin vous fait une offrande, peut-être que quelque chose vous attend dans la prochaine salle…","Une fois de retour devant la porte vous balayez les cadavres et ouvrez la porte sans aucun efforts."

sallecoffr="\n".join(sallecoffre)
delay_print(sallecoffre)

delay_print(sallefinale)

print("""
@@@@@-                                                      .#@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
@@@@=                                                     :#@@:#@@@*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
@@@-                                                     +@@@- %@@@@: *@####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
*-                                                     -%@@@@= .*@@*+        :: =:.  :+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
                                                     .#@@@@@@#-    :         :--=:--:.:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*-
                                                    -@@@@@@%:                   .. :=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=:.
                                                  :#@@@@@#-                      .:+@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+:
                                                 +@@@@@@*-.                            *@@@@@@@@@@@@@@@@@@@@@@@%*=.
                                                #@@@@@+-.                          .-- =@@@@@@@@@@@@@@@@@@%*+-                   .
                                              .%@@@@%=:                     .==:*#%@@@%@@@@@@@@@@@@@@@@#-.                   .=#@*
                                             .%@@@@@*                --+##*#@@@@@@@@@@@@@@@@@@@@@@@%+:                     =%@@@@*
                                            :@@@@@@+             .+#@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-.                     -*@@@@@@@*
                                            *@@@@@#             =@@@@@@@@@@@@@@@@@@@@@@@@@@@*-.                      :*@@@@@@@@@@*
                                            :#=#*+.            .@@@@@@@@@@@@@@@@@@@@@@@@%+:                        .*@@@@@@@@@@@@*
                                                               #@@@@@@@@@@@@@@@@@@@@@%+:                          +@@@@@@@@@@@@@@*
                                                               +@@@@@@@@@@@@@@@@@@*-                            =@@@@@@@@@@@@@@@@*
                                                               =+@@@@@@@@@@@@%#=.                             =@@@@@@@@@@@@@@@@@@*
""")

while vie_drg > 0 :
    choix_drag = str(input("\nFaites votres choix (Attaque, Esquive, Sort): "))
    if choix_drag == "Attaque":
        if For >= dé():
            vie_drg -= random.randint(4,6)
            print("Vous avez touché votre cible !")
            print("Il lui reste",vie_drg,"pv(s) !")
        elif For < dé():
            print("Vous avez attaqué et raté votre coup lamentablement")
    if choix_drag == "Sort":
        if Int >= dé() :
            if vie_max -Vie >= 4 :
                Vie += 4
                print("Le sort vous à sauvé ! Vous évitez la mort et récupérez 4 points de vie ! Vous en avez",Vie)
            if vie_max - Vie <= 4 :
                Vie += (vie_max-Vie)
                print("Vous décidez de lancer un sort de soin. Vous avez",Vie,"pv(s) !")
            if vie_max - Vie == 0 :
                print("Vous êtes déjà en pleine forme, continuez comme ça !")
                continue
        else :
            delay_print("Vous tentez de lancer un sort de soin mais ratez son incantation.")
    if choix_drag == "Esquive":
        if Agi >= dé() :
            print("Vous observez attentivement les mouvements ennemis et percevez la faille !")
            for_drg =0
        else:
            print("L'attaque est trop rapide, vous n'arriverez pas à esquiver !")
    if vie_drg == 0 :
        print("La bête succombe de ses blessures et tombe !")
    if vie_drg > 0 :
        print("L'ennemi attaque !")
        if for_drg >= dé() :
            Vie -= 2
            print("L'ennemi vous a touché, vous subissez 2 points de dégat(s) !")
            if Vie > 0:
                print("Il vous reste", Vie, "pv(s)")
            elif Vie <= 0 :
                delay_print(mort)
                quit()
        else :
            delay_print("L'attaque a raté !")
    for_drg = 6

delay_print("Le monstre s'écroule, vous vous précipitez vers lui pour lui asséner le coup fatal.....")
print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   =@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@%*+-:....:-==+#%@@@@@@@@@@@@@@@@@@*@@%=    -@@@@@@@@@@@@%*+-=**####@@@@@@@@@@@@@@@@@@@@@@@@@@@
@%+-.                ..:=%@@@@@@@@@@@@#.%--  :%%+ #@@@@@@@@@#+:--*#%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.             :-=+#%@@@@@@@@@@@@@@@**@#     .@@@@+ #@@@@@@@%#*+#*+*%@@#%*%%%%@@@@@@@@@@@@@@@@@@@@@@@
            +@@@@@@@@@@@@@@@@@@@@@@-.*.     %@@@@@. @@@@@@@%%@%+-=+-=+:-==**%@@@@@@@@@@%@@@@@@@@@@@@
           -#@@@@@@@@@@@@@@@@@@@@@@=        @@@@@@% #@@@%%%*#*+==+*+*+*#%*#@@@@@@@@@@@@@@@@@@@@@@@@@
          =@@@@@@@@@@@@@@@@@@@@@*-%.       #@@@@@@@++#**+++==:-==+#*+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        :@@@@@@@@@@@@@@+-.:=+*:.            +@@@@%#*##*++=---===*%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      -+@@@@@@@@@@@@@#         ..             -%@%%%#*++++===*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      +@@@@@@@@@@@@@@#        :+@@=            *@%#*#*++=+*####@%@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     -@@@@@@@@@@@@@@@@%=       .+@@@*-:....:.   +%%#######*+++*#*==*++%@@@@@@@@@@@@@@@@@@@@@@@@@##%@
    -@@@@@@@@@@@@@@@@@@#     .  .-%@@@@@@@@@@=:.  =+##*@@#+*=*#*+=*=+#%@@@@@@@@@@@@@@@@@@@@@@@@#*++%
   .@@@@@@@%##%%%**%%@%%          :=@@#+:-*@@@@%*     :%#*=-=+*+:--=+*%@@@@@@@@@@@@@@@@@@@@@@@%#*=+#
   #%@@@@@%%********#%%+           .=@@%%  =%@@+.      -+**+***=:-=+**#%@@@@@@@@@@@@@@@@@@@@@%@%%%##
  .##%#*++**#**%%##**#%%-            .+%#  .**+         -#@@@%#===++*##%%%%@@@@@@@@@@@@@@@@@%#%@%%*#
     --==-=*##+--:.   +##=            .    ..        :=#%%@%%%*++++=*+*#*+%@@@@%@@@@@@@@@@%%%#**+**#
         .::::..      +*#+                         =#@@@@@@%%+++=*=-=++==*%*#%%%%%%%%%%***=*%##*+=--
                 .   .===+=                       #@@@@@@%%#+++==----===+#*+***###%####***+==+%##*+=
                ..   =+++##=                     -@@@@%#*=-::.-====**-:-+**=*%##%%%##%#*%%***=-+%@%:
               .     -===+++                     :@@@%*=.    :**+=-=====*#==++##%%%%#*#%###%@%%#***+
                ::   :=*====                     -@@@@@@#- +.  ==----=+#+%+%%*#*+*#%%#+*%#%@@@@@@###
                     .--==+-                      *@@@@@%%:**   --+=*=+=####=.+**+=*****#@@@@@@@@@%*
                      -##**=                      -@@@@@%%#*#:  .++--+*#%%%%.  :#%++=**#*##@@@@@@%*=
                     :-+#**+.                      @@@@@@@%%*-   =-:-+*#=#*#=.   -*+=##*#+*%##@%%*+-
  ..                  ::-+==.               .       -*@@@@@@%-   =----**==#*%#.  .:-*----=+**%%#%*-.
                    -                                 .+*#@%#*  =#+=::-:==#**+-   .:---::.:##****-:
                         ..:.                           .:=**. :%=--  . ..:::.         : -=--: .::--
         ..                        =-                       .:-#+-:                      ..      .:-
            ..                      .:                       =#%#-:.                              ..
          .--:::.                                            ::-.
""")
fin = "Vous avez vaincu !","Bravo, Héros..."
delay_print(fin)
