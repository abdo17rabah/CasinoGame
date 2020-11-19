class Player:

  # Constants:
  INIT_MISE = 10
  
  def __init__(self, name_user):
    self.name_user = name_user
    self.solde = self.INIT_MISE
    self.stats=None

  def getUserName(self):
    return self.name_user

  def setSolde(self,sold):
    self.solde = sold

  def getSolde(self):
    return self.solde

  def setStats(self, stats):
    self.stats=stats

  def getStats(self):
    return self.stats

  def showPlayerStats(self) :
    return self.stats.show()

