class Trick:
  
  def __init__(self):
    self.combos = []

  def getPoints(self):
    points = 0
    for i in self.combos:
      for j in i:
        points += j.getPoints()
    return points
  
  def getWinner(self):
    best = self.combos[0]
    for i in self.combos:
      if best.getsBeatenBy(i, self.combos[0]):
        best = i
    return best.player.id
  
  def add(self, combo):
    self.combos.append(combo)
    if len(self.combos) == 1:
      self.suit = combo.getSuit()
  
  def isEmpty(self):
    return len(self.combos) == 0
  
  def getType(self):
    return self.combos[0].getType()
  
  def getNumCards(self):
    return self.combos[0].getCardCount()
