class Card:

  VALUES = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]
  JOKERS = [ "J-", "J+" ]
  SUITS = [ '#', '@', '$', '&' ]
  POINTS = [ 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 ]
  TRUMP_SUIT = 5
  
  def setTrumpSuit(trumpSuit):
    Card.trumpSuit = trumpSuit
    if Card.trumpSuit == 4:
      print("Trump Suit is now nothing!")
    else:
      print(Card.trumpSuit)
      print("Trump Suit is now " + Card.SUITS[Card.trumpSuit])
  
  def getIndexOfSuit(self, suitString):
    trumpSuit = -1
    for i in range(len(Card.SUITS)):
      if suitString == Card.SUITS[i]:
        trumpSuit = i
    return trumpSuit

  def getRawSuit(self):
    return int(self.cardIndex / 13)
  
  def __init__(self, inputValue):
    if type(inputValue) == str:
      cardName = inputValue
      print(cardName)
      if cardName == 'J-':
        self.cardIndex = 52
      elif cardName == "J+":
        self.cardIndex = 53
      else:
        suitChar = cardName[0]
        valueChar = cardName[1:]

        for i in range(len(Card.SUITS)):
          if suitChar == Card.SUITS[i]:
            self.cardIndex = i * 13
        for i in range(len(Card.VALUES)): 
          if Card.VALUES[i] == valueChar:
            self.cardIndex += i
    else:
      self.cardIndex = inputValue

  def equals(self, o):
    return o.cardIndex == self.cardIndex
  def __hash__(self):
    return hash((self.cardIndex))
    
  def __eq__(self, o):
    if o == None:
      return False
    return o.cardIndex == self.cardIndex
  
  def getPoints(self):
    return Card.POINTS[self.cardIndex % 13]

  def isTrump(self):
    return self.isJoker() or self.getRawSuit() == self.trumpSuit or self.getValue() == Card.trumpValue

  def getSuit(self):
    if self.isTrump():
      return Card.TRUMP_SUIT
    return self.getRawSuit()

  def getPowerIndex(self):
    if self.cardIndex == 53:
      return 29
    elif self.cardIndex == 52:
      return 28
    elif (self.getRawSuit() == Card.trumpSuit or Card.trumpSuit == 4) and self.getValue() == Card.trumpValue:
      return 27
    elif self.getValue() == Card.trumpValue:
      return 26
    elif self.getRawSuit() == Card.trumpSuit:
      return self.getValue() + 13
    else:
      return self.getValue()

  def toString(self):
    if self.cardIndex < 52:
      return Card.SUITS[self.getRawSuit()] + Card.VALUES[self.getValue()]
    return Card.JOKERS[self.cardIndex - 52]

  def __lt__(self, other):
    return self.compareTo(other) < 0;
    
  def compareTo(self, o):
    if self.getSuit() != o.getSuit():
      return self.getSuit() - o.getSuit()
    if self.getPowerIndex() - o.getPowerIndex() == 0:
      return self.cardIndex - o.cardIndex
    return self.getPowerIndex() - o.getPowerIndex()
  
  def isJoker(self):
    return self.cardIndex >= 52
  
  def getValue(self):
    return self.cardIndex % 13
