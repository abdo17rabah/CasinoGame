from Player import *

class Stats:
    
    #Const
    TIMEOUT = 10
    def __init__(self):
        self.maxLevel=1
        self.maxMise=0
        self.gainMin=0
        self.gainMax=0
        self.maxLoss=0
        # self.idPlayer = None
        self.firstTriesCount = 0

    def updateAllStats(self,maxLevel,maxMise,gainMax,firstTriesCount,gainMin,maxLoss):
        self.maxLevel=maxLevel
        self.maxMise=maxMise
        self.gainMin=gainMin
        self.gainMax=gainMax
        self.maxLoss=maxLoss
        self.firstTriesCount = firstTriesCount

    def setMaxlevel(self,level):
        self.maxLevel=level
    
    def getMaxlevel(self):
        return self.maxLevel

    def setMaxMise(self,maxMise):
        self.maxMise=maxMise
    
    def getmaxMise(self):
        return self.maxMise

    def setMiseMin(self,miseMin):
        self.miseMin=miseMin
    
    def getMiseMin(self):
        return self.miseMin

    def setGainMax(self,gainMax):
        self.gainMax=gainMax
    
    def getGainMax(self):
        return self.gainMax

    def setMaxLoss(self,maxLoss):
        self.maxLoss=maxLoss
    
    def getMaxLoss(self):
        return self.maxLoss
    
    def setFirstTriesCount(self,firstTriesCount):
        self.firstTriesCount=firstTriesCount
    
    def getFirstTriesCount(self):
        return self.firstTriesCount

    def show(self) :
        print ("""************ Vos meilleures stats ************ \n+
                \t- Réponse dés le premier coup : {}!\n
                \t- Gain Maximal : {}!\n
                \t- Mise Maximale : {}!\n
                \t- Level Maximale : {}!\n+
                ************ Vos Mauvaises stats ************ \n+
                \t- Gain minimal : {}!\n
                \t- Mise minimale : {}!\n
                \t- Grosse Perte : {}!\n
                """.format(
                self.firstTriesCount ,
                self.gainMax,
                self.maxMise,
                self.maxLevel,
                self.gainMin,
                self.miseMin,
                self.maxLoss
                ))