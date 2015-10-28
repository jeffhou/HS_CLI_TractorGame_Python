from Card import Card

class Call:

  def __init__(self, card, count):
    if type(card) == Card:
      self.card = card
    else:
      self.card = Card(card)
    self.count = count

  def getCallLevel(self):
    callLevel = self.card.getRawSuit() + (self.count - 1) * 6
    if self.card.toString() == "J+":
      callLevel += 1
    if callLevel == 4 or callLevel == 5:
      callLevel = -1
    return callLevel
  
  def getSuit(self):
    return self.card.getRawSuit()
    
  def isValid(self):
    return self.card.getPowerIndex() >= 26