from ComboType import ComboType
from SortedCardCollection import SortedCardCollection
from Card import Card
class Combo(SortedCardCollection):

  def __init__(self, player, cardsPlayed):
    super().__init__()
    self.addCards(cardsPlayed)
    self.player = player

  def isSameSuit(self):
    suit = -1
    for i in self:
      if suit == -1:
        suit = i.getSuit()
      if suit != i.getSuit():
        return False
    return True

  def getSuit(self):
    if self.isSameSuit():
      return self.cards[0].getSuit()
    return -1

  def getsBeatenBy(self, challenger, first): 
    return self.getPower(first) < challenger.getPower(first)

  def getPower(self, first):
    if self.getType() == ComboType.NONE or self.getType() != first.getType():
      return 0
    if self.getSuit() != first.getSuit() and self.getSuit() != Card.TRUMP_SUIT:
      return 0

    power = self.get(0).getPowerIndex()
    return power

  def getType(self):
    if self.isMixedSuit():
      return ComboType.NONE
    elif self.isSingle():
      return ComboType.SINGLE
    elif self.isPair():
      return ComboType.PAIR
    elif self.isTractor():
      return ComboType.TRACTOR
    return ComboType.NONE

  def isTractor(self):
    numCopies = self.getCount(self.get(0))
    for i in range(0, self.size() - numCopies, numCopies):
      if self.get(i).getPowerIndex() != self.get(i + numCopies).getPowerIndex() - 1:
        return False
      if self.getCount(self.get(i)) != numCopies:
        return False
    return True

  def isPair(self):
    return self.size() == 2 and self.get(0) == self.get(1)

  def isSingle(self):
    return self.size() == 1

  def isMixedSuit(self):
    return self.getSuit() == -1

  def consecutivePairCounts(self, firstCombo):
    
    consPairCounts = []
    currentCount = 0
    maxCount = 0
    startOfSuit = 0
    
    for i in range(self.size()):
      if self.get(i).getSuit() == firstCombo.getSuit():
        startOfSuit = i
        break
    
    i = startOfSuit
    lastPair = -1
    while i < self.size() - 1 and self.get(i).getSuit() == firstCombo.getSuit():
      if self.get(i) == self.get(i + 1):
        if lastPair == self.get(i).getPowerIndex():
          i += 2
          continue
        elif lastPair == -1 or self.get(i).getPowerIndex() != lastPair + 1:
          currentCount = 1

        else:
          currentCount += 1
        if currentCount < maxCount:
          maxCount = currentCount
        lastPair = self.get(i).getPowerIndex()
        i += 2
      else:
        i += 1
        if currentCount > 0:
          consPairCounts.append(currentCount)
        currentCount = 0

    if currentCount > 0:
      consPairCounts.append(currentCount)
    consPairCounts.sort()
    consPairCounts.reverse()
    return consPairCounts
