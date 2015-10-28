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

  def copyCardsList(self, cardsList):
    cards = []
    for i in cardsList:
      cards.append(Card(i.cardIndex))
    return cards
    
  def isSubSet(self, secondList):
    print("[", end="")
    for i in self.cards:
      print(i.toString(), end=", ")
    print("]")
    print("[", end="")
    for i in secondList.cards:
      print(i.toString(), end=", ")
    print("]")
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
    
  def isSubSet1(self, o):
    sortedSubList = self.copyCardsList(self.cards)
    print("sortedSubList: ", end="")
    for i in sortedSubList:
      print(i.toString(), end="")
    print()
    sortedSuperList = self.copyCardsList(o.cards)
    print("sortedSuperList: ", end="")
    for i in sortedSuperList:
      print(i.toString(), end="")
    print()
    j = 0
    for i in range(len(sortedSubList)):
      notSubset = False
      while True:
        print ("comparing " + sortedSubList[i].toString() + " and " + sortedSuperList[j].toString())
        if sortedSubList[i].equals(sortedSuperList[j]):
          j += 1
          break
        j += 1
        if j >= len(sortedSuperList):
          notSubset = True
          break
      if notSubset or j == len(sortedSuperList):
        print(False)
        return False
    return True
