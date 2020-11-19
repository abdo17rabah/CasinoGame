#Guide d'utilisation:
* Ce jeu est basé sur les régles de jeu du casino, en gros titres: vous avez le droit de vous retiré quand vous voulez
    de relancer une nouvelle partie ou pas, et bien sure la mise minimale est fixé par chaque enseigne.
* Pour lancer ce jeu, et pouvoir y jouer, je vous invite a lancer votre CMD dans la page "CasinoGame.py", c'est très important si non le vous voulez que le jeu démarre.

#Conception du jeu:
* Ce jeu posséde une base de données relationnelle, MySql, toutes les données du joueurs seront stockées dès sa première participation et ses dèrnieres se metteront à jour au fur et à mesure.
* le fichier DB: comporte toutes les fonctions qui font appels a la BDD, de type update,insert select..etc.
* Le fichier Level: se compose de fonctions relatives aux diffèrents levels.
* Le fichier Levels_list : retourne le level en-cours et toutes les informations relatives a ce niveau la, à savoir l'intervalle de jeux, le nombres de coups possibles et les cotes.
* Le fichier player: est relatif aux informations du joueur à savoir son nom et son solde.
* Le fichier stats: est relatif aux differents stats de chaque joueur.
* Le fichier Game: c'est ou toute la logique du jeu occurera, à savoir la génération du random et tous les appels aux fonctions d'affichages, d'insertions de mise à jour ...etc.
* Le fichier CasinoGame: en d'autres termes le plus important, c'est la ou on fait appel au jeu, je répète il est impératif qu'on ouvre le CMD dnas ce fichier la (si on l'ouvre depuis VS ou depuis votre IDE préfèrè).

Me reste plus qu'a vous souhaiter une bonne partie.

