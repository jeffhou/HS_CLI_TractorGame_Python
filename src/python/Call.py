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
  
  def toString(self):
    return str(self.count) + " of " + self.card.toString()
  
  def serialize(call):
    return call.card.toString() + "," + str(call.count)
  
  def serializeSelf(self):
    return Call.serialize(self)
  
  def deserialize(callString):
    card = Card(callString[:callString.index(",")])
    count = int(callString[callString.index(",") + 1:])
    return Call(card, count)