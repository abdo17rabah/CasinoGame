#coding:utf-8
import random

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
name_user= None

def play():
    global dotation, nb_python ,name_user
    while True:
        name_user = raw_input("Je suis Python. Quel est votre pseudo ? ")
        if not name_user :
            print("Pseudo non valide")
        # elif name_user in PLAYERS :
        #     print("Username exsiste déja")
        else:
            print("Pseudo valide !")
            # PLAYERS["Pseudo"] = name_user
        break

    while True:
        print('Entez votre mise:')
        mise = raw_input()
        try:
            mise = int(mise)
        except:
            print('Please use numeric digits.')
            continue
        if mise < 1:
            print('Entrez a positive number.')
            continue
        if mise > dotation:
            print('Votre mise est superieure à votre dotation: '+str(dotation))
            continue
        break
    
    playQuestion = askPlayer()
    while(dotation != 0 and playQuestion == True):
        # nb_python = getRandomNumber(level[1],level[2])
        nb_python = getRandomNumber(1,10)
        print("### J'ai choisi :"+str(nb_python))
        nb_coup = 0
        # while nb_coup<level[0] :
        while nb_coup < 3 :
            nb_user = input ("Entrez SVP votre nombre ? ")
            while True :
                try:
                    nb_user = int(nb_user)
                    #Gerer l'exception de STRING
                except:
                    print('Please use numeric digits.')
                    continue
                if nb_user < 1:
                    print('Entrez a positive number.')
                    continue
                break
            nb_coup += 1
            if nb_user > nb_python :
                print ('Votre nbre est trop grand')
            elif nb_user < nb_python :
                print ('Votre nbre est trop petit')
            else :
                print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                if(nb_coup ==1):
                    dotation=(dotation-mise)+mise*2
                elif (nb_coup ==1):
                    dotation=(dotation-mise)+mise
                else :
                    dotation =(dotation-mise)+mise/2
                break
        
        #TODO: Gerer les levels
        if (nb_coup>3) :
            print ("Vous avez perdu, mon nombre choisi est :"+ str(nb_python))
            #TODO: changement de mise aprés la perte
            dotation-=mise
    
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
        answer = raw_input("Bonjour "+ name_user +". You have $" + str(dotation) + ". Would you like to play? ")
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
            print("You ended the game with n your hand.")
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

play()