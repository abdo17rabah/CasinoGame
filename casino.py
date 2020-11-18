#coding:utf-8
import random
import time
from threading import Timer

#Constants:
INIT_MISE = 10
LEVELS = {
  "level1": [3,1,10],
  "level2": [5,1,20],
  "level3": [7,1,30]
}

PLAYERS={}

nb_python = None
dotation = INIT_MISE 
mise=None
name_user= None
currentLevel=list(LEVELS.values())[0]
level = 0
timeout = 10
nb_coup = 0





def play():
    global dotation, nb_python ,name_user,mise,currentLevel,level,nb_coup
    while True:
        answer = showRules()
        if(answer == True):
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
        

        name_user = input("Je suis Python. Quel est votre pseudo ? ")
        if not name_user :
            print("Pseudo non valide")
        # elif name_user in PLAYERS :
        #     print("Username exsiste déja")
        else:
            print("Pseudo valide !")
            # PLAYERS["Pseudo"] = name_user
            break

    playQuestion = askPlayer()
    while(dotation != 0 and playQuestion == True):
        while True:
            print('Entrer une mise inférieure ou égale à {} € : ?'.format(dotation))
            mise = input()
            try:
                mise = int(mise)
            except:
                print('Entrez un nombre.')
                continue
            if mise < 1:
                print('Entrez a nombre postif.')
                continue
            if mise > dotation:
                print('Erreur, votre mise est plus elevé que votre solde.: '+str(dotation))
                continue
            break
        nb_python = getRandomNumber(int(currentLevel[1]),int(currentLevel[2]))
        while (nb_coup < currentLevel[0] ) :
            timeout = time.time() + 10
            while True :
                nb_user = input ("Entrez SVP votre nombre ? ")
                try:
                    nb_user = int(nb_user)
                        #Gerer l'exception de STRING
                except:
                    print('Please use numeric digits.')
                    continue
                if nb_user < 1:
                    print('Entrez a positive number.')
                    continue
                if time.time() > timeout:
                    triesLeft = currentLevel[0] - (nb_coup+1)
                    print("Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant\n\t\t\t et il vous reste {} essai(s) !" .format(triesLeft))
                    break
                break
            nb_coup += 1
            if nb_user > nb_python :
                print ('Votre nbre est trop grand')
            elif nb_user < nb_python :
                print ('Votre nbre est trop petit')
            else :
                print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                if(nb_coup == 1):
                    dotation = (dotation-mise)+(mise*2)
                elif (nb_coup == 2 ):
                    dotation = (dotation-mise)+mise
                else :
                    dotation = (dotation-mise)+(mise/2)
                print ("Vous passez au level suivant")
                currentLevel = list(LEVELS.values())[level+1]
                level+=1
                break
        
        #TODO: Gerer les levels
        if (nb_user!=nb_python) :
            print ("Vous avez perdu, mon nombre choisi est :"+ str(nb_python))
            #TODO: changement de mise aprés la perte
            dotation-=mise
            if(level == 0):
                currentLevel = list(LEVELS.values())[0]
            else:
                currentLevel = list(LEVELS.values())[level-1]
            nb_coup=0
            
        # printScore()
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, Y, nO . . . all works
    '''
    global dotation, name_user
    while(True):
        answer = input("Bonjour "+ name_user +". Vous possedez €" + str(dotation) + ". Voulez vous jouer? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(dotation) + " in your hand.")
            return False
        else:
            print("wrong input!")

def showRules():
    '''
    Asks the player if he wants to know the rules.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
    '''
    while(True):
        answer = input("Bonjour voulez vous connaitre les régles ? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("Bonne Partie !.")
            return False
        else:
            print("wrong input!")

def getRandomNumber(range1,range2):
    '''
    returns a random item from the wheel
    '''
    return random.randint(range1, range2+1)

def printScore():
    '''
    prints the current score
    '''
    global stake

def timeOut():
    triesLeft = currentLevel[0] - nb_coup
    print("Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant\n\t\t\t et il vous reste {} essai(s) !" .format(triesLeft))
 
play()