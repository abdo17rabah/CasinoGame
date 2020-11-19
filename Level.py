import random

class Level :
    
    def __init__(self, count, range1,range2):
        self.count = count
        self.range1=range1
        self.range2=range2
        self.cote = None

    def getCount(self):
        return self.count

    def setCount(self,count):
        self.count=count

    def setRange1(self,range1):
        self.range1=range1

    def setRange2(self,range2):
        self.range2=range2

    def getRange1(self):
        return self.range1

    def getRange2(self):
        return self.range2

    def setCote(self,cote):
        self.cote = cote

    def getCote(self):
        return self.cote

    def getRandomNumber(self,range1,range2):
    # '''
    # returns a random item from the wheel
    # '''
        return random.randint(range1, range2+1)

    def ToString(self):
        return str([self.count,self.range1,self.range2])

    

    

    