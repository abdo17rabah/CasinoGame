#coding:utf-8
from Player import *
from Levels_list import *
# from DB import *
import time
from threading import Timer
from DB import *

class Game:
    

    #Const
    TIMEOUT = 10

    def __init__(self ,levels_list):
        self.db = DB()
        self.db.connectDB()
        self.levels_list=levels_list
        self.levels = levels_list.getLevels()
        self.player = None
        self.dotation = None
        self.stats= None
        self.nb_python = 0
        self.mise=0
        self.currentLevel = self.levels[0]
        self.nb_coup= 0
        self.level=1
        self.gameEnded= False
        self.gain=0
        self.maxLevel=0
        self.maxMise=0
        
        
        # self.db.connect()

    def setPlayer(self, player):
        self.player=player

    def setLevel(self, level):
        self.level=level

    def setStats(self, stats):
        self.stats=stats
    
    def setNbPython(self, nb_python):
        self.nb_python=nb_python

    def setMise(self, mise):
        self.mise=mise

    def setDotation(self, dotation):
        self.dotation=dotation

    def play(self):
        # Check if the user exists or not, if not create a new one
        while True:
            #TODO: check if the player exist in the table 
            name_user = input("Je suis Python. Quel est votre pseudo ? ")
            if not name_user :
                print("Pseudo non valide")
            # elif name_user in PLAYERS :
            #     print("Username exsiste déja")
            else:
                print("Pseudo valide !")
                player=self.db.addPlayer(name_user)
                print(player)

                # PLAYERS["Pseudo"] = name_user
                # self.setPlayer(Player(name_user))
                # self.dotation=self.player.getSolde()
                break

            #Ask the player if he wants to know the rules of the game
            #TODO : Condtion to Check if the player has played already then ask if not show the rules
            answer = self.askRules()
            if(answer == True):
                self.showRules()

        
        playQuestion = self.askPlayer()
        while(self.dotation != 0 and playQuestion == True):
            while True:
                #TODO : update "mise" in stats 
                print ("### current level : "+ self.currentLevel.ToString())
                print('Entrer une mise inférieure ou égale à {} € : ?'.format(self.dotation ))
                self.mise = input()
                try:
                    self.mise = int(self.mise)
                except:
                    print('Entrez un nombre.')
                    continue
                if self.mise < 1:
                    print('Entrez a nombre postif.')
                    continue
                if self.mise > self.dotation :
                    print('Erreur, votre mise est plus elevé que votre solde.: '+str(self.dotation ))
                    continue
                self.maxMise=self.compare(self.mise,self.maxMise)
                break
            self.nb_python = self.currentLevel.getRandomNumber(self.currentLevel.getRange1(),self.currentLevel.getRange2())
            print("#### nb_python"+str(self.nb_python))
            while (self.nb_coup < self.currentLevel.getCount() ) :
                timeout = time.time() + self.TIMEOUT
                while True :
                    self.nb_user = input ("Entrez SVP votre nombre ? ")
                    try:
                        self.nb_user = int(self.nb_user)
                    except:
                        print('Please use numeric digits.')
                        continue
                    if self.nb_user < 1:
                        print('Entrez a positive number.')
                        continue
                    if time.time() > timeout:
                        triesLeft = self.currentLevel.getCount() - (self.nb_coup+1)
                        print("Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant\n\t\t\t et il vous reste {} essai(s) !" .format(triesLeft))
                        break
                    break
                self.nb_coup+= 1
                if self.nb_user > self.nb_python :
                    print ('Votre nbre est trop grand')
                elif self.nb_user < self.nb_python :
                    print ('Votre nbre est trop petit')
                else :
                    print ("Bingo ! Vous avez gagné en {} coup(s) !".format(self.nb_coup))
                    if(self.nb_coup == 1):
                        self.dotation = (self.player.getSolde()-self.mise)+(self.mise*2)
                        self.gain += (self.mise*2)-self.mise
                        self.player.setSolde(self.dotation)

                    elif (self.nb_coup == 2 ):
                        self.dotation = (self.player.getSolde()-self.mise)+self.mise
                        self.player.setSolde(self.dotation)
                        self.gain += (self.mise)-self.mise
                    else :
                        self.dotation = (self.player.getSolde()-self.mise)+(self.mise/2)
                        self.player.setSolde(self.dotation)
                        self.gain += (self.mise/2)-self.mise
                    self.maxLevel=self.compare(self.level,self.maxLevel)
                    self.level+=1
                    if(self.level > self.levels_list.getNumberLevels()):
                        print ("""Bravo ! Vous avez terminer le jeu, vos stats sont :  !\n+
                                \t- Gain Maximal : {}!\n
                                \t- Mise Maximale : {}!\n
                                \t- Level Maximale : {}!\n
                                #TODO : ajouter d'autres states (grosse perte, level min, mise min)
                        """.format(self.gain,self.maxMise,self.maxLevel))
                        #TODO: show stats
                        #self.player.showPlayerStats()
                        #TODO : ask the player if he wants to play again
                        self.gameEnded=True
                        self.askPlayer()
                    else :
                        print ("Super ! Vous passez au Level: {}!\n".format(self.level))
                        self.currentLevel = self.levels_list.getLevel(self.level-1)
                        self.nb_coup=0
                    break
            
            #TODO: Gerer les levels
            if (self.nb_user!=self.nb_python) :
                print ("Vous avez perdu, mon nombre choisi est :"+ str(self.nb_python))
                #TODO: changement de mise aprés la perte
                self.dotation-=self.mise
                self.player.setSolde(self.dotation)
                if(self.level == 0):
                    self.currentLevel = self.levels_list.getLevel(0)
                else:
                    self.currentLevel = self.levels_list.getLevel(self.level-1)
                self.nb_coup=0
            if(self.dotation == 0) :
                print ("Vous avez perdu, vous n'avez plus de solde €:"+ str(self.dotation))
                self.gameEnded = True
                break

        # printScore()
        playQuestion = self.askPlayer()
        
    def askPlayer(self):
        '''
        Asks the player if he wants to play again.
        expecting from the user to answer with yes, y, no or n
        No case sensitivity in the answer. yes, YeS, y, Y, nO . . . all works
        '''
        while(True):
            if(self.gameEnded ==True):
                answer = input("Vous possedez € " + str(self.player.getSolde()) +" Voulez vous encore jouer ? (Y/N)")
                answer = answer.lower()
                if(answer == "yes" or answer == "y"):
                    self.currentLevel = self.levels_list.getLevel(0)
                    self.level=1
                    self.nb_coup=0
                    return True
                elif(answer == "no" or answer == "n"):
                    print("Vous avez terminé votre partie avec €" + str(self.player.getSolde()) + " de solde.")
                    return False
                else:
                    print("wrong input!")
                    
            else :
                answer = input("Bonjour "+ self.player.getUserName() +". Vous possedez €" + str(self.player.getSolde()) + ". Voulez vous jouer(Y/N)? ")
                answer = answer.lower()
                if(answer == "yes" or answer == "y"):
                    return True
                elif(answer == "no" or answer == "n"):
                    print("Vous avez terminé votre partie avec €" + str(self.player.getSolde()) + " de solde.")
                    return False
                else:
                    print("wrong input!")

    def askRules(self):
        '''
        Asks the player if he wants to know the rules.
        expecting from the user to answer with yes, y, no or n
        No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
        '''
        while(True):
            answer = input("Bonjour voulez vous connaitre les régles (Y/N) ? ")
            answer = answer.lower()
            if(answer == "yes" or answer == "y"):
                return True
            elif(answer == "no" or answer == "n"):
                print("Bonne Partie !.")
                return False
            else:
                print("wrong input!")

    def compare(self,elem1,elem2):
        if(elem1>=elem2):
            return elem1
        else :
            return elem2

        
    def showRules(self):
        print(""" 
                    *  *  *  *  *  *  *  *  *  *  * Bienvenue *  *  *  *  *  *  *  *  *\n
                    Le jeu comporte 3 levels avec la possibilié que le joueur choissise son level (si ce n'est pas sa 1è fois dans le Casino).
                    En d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint\n.
                    Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10),
                    level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout) lors du 1è 
                    level, 5 au 2è level et 7 au 3è level. Chaque essai ne durera pas plus de 10 secondes. Au-delà, 
                    vous perdez votre essai. Att : si vous perdez un level, vous rejouez le level précédent.
                    Quand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place. 
                    En absence de validation de la décision, le jeu est terminé.
                    *  *  *  *  *  *  *  *  *  *  * Régles *  *  *  *  *  *  *  *  *\n
                    vous avez le droit à trois essais !\n
                    \t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n
                    \t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n
                    \t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n    
                    \t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et
                    \tvous avez le droit : 
                    \t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
                    \t\t- de quitter le jeu.\n
                    \t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n     
                    """)