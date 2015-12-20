from SortedCardCollection import SortedCardCollection
class Player(SortedCardCollection):

  def __init__(self, i):
    super().__init__()
    self.id = i
    self.level = 0
    
  def levelUp(self, level):
    self.level += level
    
  def hasComboToPlay(self, firstCombo):
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
        if currentCount > maxCount:
          maxCount = currentCount
        lastPair = self.get(i).getPowerIndex()
        i += 2
      else: 
        i += 1
    if maxCount * 2 >= firstCombo.size():
      return True
    return False
  
  def playedRequired(self, firstCombo, attemptedCombo):
    handConsecPairCounts = self.consecutivePairCounts(firstCombo)
    comboConsecPairCounts = attemptedCombo.consecutivePairCounts(firstCombo)
    numberOfCardsNeeded = firstCombo.size()
    i = 0
    while numberOfCardsNeeded != 0 and i < len(handConsecPairCounts):
      if i >= len(comboConsecPairCounts):
        return False
      if handConsecPairCounts[i] * 2 <= numberOfCardsNeeded:
        if comboConsecPairCounts[i] != handConsecPairCounts[i]:
          return False
        numberOfCardsNeeded -= handConsecPairCounts[i]
      else:
        if comboConsecPairCounts[i] != numberOfCardsNeeded:
          return False
        else:
          return True
      i+=1
    return True
  
  def consecutivePairCounts(self, firstCombo):
    consecPairCounts = []
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
        if currentCount > maxCount:
          maxCount = currentCount
        lastPair = self.get(i).getPowerIndex()
        i += 2
      else: 
        i+=1
        if currentCount > 0:
          consecPairCounts.add(currentCount)
        currentCount = 0
    if currentCount > 0:
      consecPairCounts.append(currentCount)
    consecPairCounts.sort()
    consecPairCounts.reverse()
    return consecPairCounts
  
  def canOverride(self, player, newCallLevel):
    numCards = int(newCallLevel / 6) + 1
    suit = newCallLevel % 6
    toCheck = None
    if suit == 5:
      toCheck = Card("J+")
      if numCards == 1:
        return False
    elif suit == 4:
      toCheck = Card("J-")
      if numCards == 1:
        return False
    else:
      toCheck = Card(Card.SUITS[suit] + Card.VALUES[Card.trumpValue])
    for i in self:
      if i == toCheck:
        numCards-=1
    return numCards <= 0
  
  def has(self, card, numCards):
    return self.getCount(card) >= numCards
