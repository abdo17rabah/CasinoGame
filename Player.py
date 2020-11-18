class Player:

  # Constants:
  INIT_MISE = 10
  
  def __init__(self, name_user):
    self.name_user = name_user
    self.solde = self.INIT_MISE

  def getUserName(self):
    return self.name_user

  def setSolde(self,sold):
    self.solde = sold

  def updateStats(self, stats):
    self.stats=stats

  def getSolde(self):
    return self.solde

  def getStats(self):
    return self.stats

  def showPlayerStats(self) :
    return self.stats.show()

