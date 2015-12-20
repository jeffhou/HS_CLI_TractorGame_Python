from CardCollection import CardCollection
class SortedCardCollection(CardCollection):

  def __init__(self):
    super().__init__()
  
  def addCard(self, card):
    super().addCard(card)
    self.sort()
    
  def addCards(self, cc):
    super().addCards(cc)
    self.sort()
    
  def isSubSet(self, secondList):
    firstDict = {}
    secondDict = {}
    for i in self:
      if i in firstDict:
        firstDict[i] += 1
      else:
        firstDict[i] = 1
        
    for i in secondList:
      if i in secondDict:
        secondDict[i] += 1
      else:
        secondDict[i] = 1
        
    for i in firstDict:
      if i in secondDict:
        if firstDict[i] <= secondDict[i]:
          pass
        else:
          return False
      else:
        return False
    return True