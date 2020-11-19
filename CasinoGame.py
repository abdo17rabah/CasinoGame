from Levels_list import *
from Game import *

# from DB import *

class CasinoGame :
    levels_list = Levels_list()
    game= Game(levels_list)
    game.play()


