def printCardList(listOfCards):
  print("[", end="")
  for i in listOfCards:
    print(i.toString(), end=", ")
  print("]")  
class TractorGame:

  NUM_PLAYERS = 4
  NUM_DECKS = 2
  TESTING = True
  
  def __init__(self):
    self.startGame()
    
  def startGame(self):

    currentRound = None
    TractorGame.players = []

    for i in range(TractorGame.NUM_PLAYERS): 
      TractorGame.players.append(Player(i))

    while True: 
      if currentRound == None: 
        currentRound = Round(TractorGame.players[0])
      else: 
        currentRound = Round(TractorGame.players[currentRound.getWinner()])
      currentRound.start()
import random
class CardCollection:

  def __iter__(self):
    return self
    
  def __next__(self):
    if self.index == len(self.cards):
      self.index = 0
      raise StopIteration
    else:
      self.index += 1
      return self.cards[self.index - 1]
      
  def __init__(self):
    self.index = 0
    self.cards = []

  def addCards(self, cc): 
    for i in cc:
      self.cards.append(i)

  def addCard(self, card):
    self.cards.append(card)

  def countSuit(self, suit):
    count = 0
    for i in self.cards:
      if i.getSuit() == suit:
        count += 1
    return count

  def get(self, i):
    return self.cards[i]

  def getCount(self, c):
    return sum(c.equals(card) for card in self.cards)

  def getCardCount(self):
    return len(self.cards)

  def isEmpty(self):
    return len(self.cards) == 0


  def remove(self, i):
    if type(i) == Card:
      return self.cards.remove(i)
    else:
      return self.cards.pop(i)


  def removeAll(self):
    self.cards.clear()

  def removeCards(self, cards):
    
    for i in cards.cards:
      printCardList(cards.cards)
      print(i.toString())
      self.cards.remove(i)

  def shuffle(self):
    if TractorGame.TESTING:
      random.seed(0)
    else:
      random.seed()
    random.shuffle(self.cards)

  def size(self):
    return len(self.cards)
    
  def sort(self): 
    self.cards.sort()
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
class Round:
  NUM_PLAYERS = 4
  NUM_DECKS = 2
  NUM_LEFTOVER = 8
  roundCount = 0
  playerTeams = [0, 1, 0, 1]
  playerPoints = [0, 0, 0, 0]
  def __init__(self, winner):
    Round.roundCount+=1
    self.mainDeck = Deck(Round.NUM_DECKS)
    self.tricks = []
    self.boss = winner.id
    Card.trumpValue = TractorGame.players[self.boss].level
    Card.trumpSuit = -1
    self.callLevel = -1
  def autoAssignTrumpSuit(self):
    print("Bottom 8: ", end="")
    for i in self.mainDeck:
      print(i.toString() + " ", end="")
    for i in self.mainDeck:
      if i.getValue() == Card.trumpValue:
        Card.trumpSuit = i.getRawSuit()
        return
    selector = None
    for i in self.mainDeck:
      if selector == None or selector.getValue() < i.getValue():
        if selector == None or not selector.isJoker():
          selector = i
    print(selector, end="")
    Card.trumpSuit = selector.getSuit()
  def canOverrideCurrent(self, player, call):
    newCallLevel = call.getCallLevel()
    return newCallLevel > self.callLevel and player.has(call.card, call.count)
  def callTrumpInput(self, player):
    trumpInput = self.getUserInput("Call: ")
    if trumpInput == "":
      return
    call = Call(trumpInput[1:], int(trumpInput[:1]))
    if self.canOverrideCurrent(player, call):
      Card.setTrumpSuit(call.getSuit())
      self.callLevel = call.getCallLevel()
      if self.roundCount == 1:
        self.boss = player.id
  def challengersWin(self):
    self.determineWinners(True)
  def checkBottom(self):
    points = 0
    for i in self.mainDeck:
      points += i.getPoints()
    multiplier = 2
    lastTrick = self.tricks[-1]
    
    if lastTrick.getType() == ComboType.SINGLE:
      multiplier = 2
    elif lastTrick.getType() == ComboType.PAIR:
      multiplier = 4
    elif lastTrick.getType() == ComboType.TRACTOR:
      multiplier = lastTrick.getNumCards() * 2
    print(lastTrick.getWinner())
    self.playerPoints[lastTrick.getWinner()] += points * multiplier
  def dealAndCall(self):
    while self.mainDeck.size() > Round.NUM_LEFTOVER:
      for i in range(Round.NUM_PLAYERS):
        newCard = self.mainDeck.draw()
        TractorGame.players[i].addCard(newCard)
        if Card.trumpSuit == 4:
          print()
          print("=== HAND (!" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
        elif Card.trumpSuit != -1:
          print()
          print("=== HAND (" + Card.SUITS[Card.trumpSuit]  + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
        else:
          print()
          print("=== HAND (~" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")

        self.updateDisplay(TractorGame.players[i])
        if False:
          self.callTrumpInput(TractorGame.players[i])
  def determineWinners(self, challengersWin):
    challengerTeam = self.playerTeams[self.boss]
    for i in range(len(TractorGame.players)):
      if (self.playerTeams[i] == challengerTeam) == challengersWin:
        self.winners[i] = True
  def display(self, string):
    print(string)
  def getPointsForChallengers(self):
    points = 0
    for i in range(RoundNUM_PLAYERS):
      if self.playerTeams[i] != self.playerTeams[self.boss]:
        points += self.playerPoints[i]
    return points
  def getUserInput(self, prompt):
    return input(prompt)
  def getWinner(self):
    for i in range(Round.NUM_PLAYERS):
      if self.winners[(i + self.boss + 1) % Round.NUM_PLAYERS]:
        return (i + self.boss + 1) % Round.NUM_PLAYERS
    return -1
  def incumbentsWin(self):
    self.determineWinners(False)
  def inputCardsPlayed(self, cards, player):
    print("Cards (" + str(cards.size()) + "): ", end="")
    for i in cards:
      print(i.toString() + " ", end="")
    inputString = self.getUserInput("")
    if inputString == "":
      return
    cardStrings = inputString.split(" ")
    for i in cardStrings:
      print(Card(i).cardIndex)
      cards.addCard(Card(i))
  def levelByPoints(self):
    points = self.getPointsForChallengers()
    if points < 80:
      self.incumbentsWin()
      if points == 0:
        self.levelUpWinners(3)
      elif points < 40:
        self.levelUpWinners(2)
      elif points < 80:
        self.levelUpWinners(1)
    else:
      self.challengersWin()
      self.levelUpWinners(int(points / 40) - 2)
  def levelUpWinners(self, level):
    for i in range(Round.NUM_PLAYERS):
      TractorGame.players[i].levelUp(level)
  def nextTrick(self):
    currentTrick = Trick()
    if Card.trumpSuit == 4:
      print("=== NEW TRICK (!" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
    else:
      print("=== NEW TRICK (" + Card.SUITS[Card.trumpSuit] + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
    for i in TractorGame.players:
      print("Player " + str(i.id) + ": " + str(self.playerPoints[i.id]) + " points")
    for i in range(Round.NUM_PLAYERS):
      if len(self.tricks) == 0:
        playerID = (i + self.boss) % Round.NUM_PLAYERS
      else:
        playerID = (i + self.tricks[len(self.tricks) - 1].getWinner()) % Round.NUM_PLAYERS
      self.updateDisplay(TractorGame.players[playerID])
      self.playCards(TractorGame.players[playerID], currentTrick)
    self.updatePoints(currentTrick.getWinner(), currentTrick.getPoints())
    print("Player " + str(currentTrick.getWinner()) + " wins trick and earns " + str(currentTrick.getPoints())
        + " points!")
    return currentTrick
  def playCardsForBottom(self, player, numCards, c):
    cardsPlayed = SortedCardCollection()
    while cardsPlayed.size() != numCards:
      if not cardsPlayed.isSubSet(player) or cardsPlayed.size() > 8:
        cardsPlayed.removeAll()
      self.inputCardsPlayed(cardsPlayed, player)
      
    
    cards = []
    for i in range(numCards):
      cards.append(cardsPlayed.get(i))
    
    return cards
  def playCards(self, player, currentTrick):
    cardsPlayed = SortedCardCollection()
    valid = False
    combo = None
    while not valid:
      self.inputCardsPlayed(cardsPlayed, player)
      combo = Combo(player, cardsPlayed)
      valid = self.validateCardsPlayed(combo, currentTrick, player)
      if not valid:
        print("Invalid!")
        cardsPlayed.removeAll()
      else:
        print("VALID!")
    printCardList(player)
    currentTrick.add(combo)
    printCardList(player)
    player.removeCards(cardsPlayed)
    printCardList(player)
  def populateTricks(self):
    while not TractorGame.players[0].isEmpty():
      self.tricks.append(self.nextTrick())
  def replaceBottom(self):
    if Card.trumpSuit == -1:
      self.autoAssignTrumpSuit()
    if Card.trumpSuit == 4:
      print()
      print("=== REPLACE BOTTOM (!)===")
    else:
      print()
      print("=== REPLACE BOTTOM (" + Card.SUITS[Card.trumpSuit] + ")===")
    

    while not self.mainDeck.isEmpty():
      TractorGame.players[self.boss].addCard(self.mainDeck.draw())
    self.updateDisplay(TractorGame.players[self.boss])
    print("~~~~~~~~~~~~~~~~~~")
    if False:
      for i in self.playCardsForBottom(TractorGame.players[self.boss], 8, ComboType.NONE):
        self.mainDeck.addCard(i)
        TractorGame.players[self.boss].remove(i)
    else:
      for i in range(8):
        self.mainDeck.addCard(TractorGame.players[self.boss].remove(0))
    self.updateDisplay(TractorGame.players[self.boss])
  def start(self):
    self.dealAndCall()
    self.replaceBottom()
    for i in TractorGame.players:
      i.sort()
    self.populateTricks()
    self.checkBottom()
    self.levelByPoints()
  def updateDisplay(self, player):
    print("Player " + str(player.id) + ": ", end="")
    for i in player:
      print(i.toString() + " ", end="")
    print()
  def updatePoints(self, winner, points):
    self.playerPoints[winner] += points
  def validateCardsPlayed(self, combo, currentTrick, player):
    if currentTrick.isEmpty():
      print("First combo played: " + str(combo.getType()))
      return combo.getType() != ComboType.NONE
    first = currentTrick.combos[0]
    if combo.size() == first.size():
      if combo.getSuit() != first.getSuit():
        if player.countSuit(first.getSuit()) == combo.countSuit(first.getSuit()):
          return True
        else:
          return False
      else:
        if combo.getType() == first.getType():
          return True
        else:
          print("combos aren't the same")
          if player.hasComboToPlay(first):
            return False
          elif player.playedRequired(first, combo):
            print("doesn't have that combo")
            return True
    return False
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
    for i in self.size():
      if self.get(i).getSuit() == firstCombo.getSuit():
        startOfSuit = i
        break
    i = startOfSuit
    lastPair = -1
    while i < self.size() - 1 and self.get(i).getSuit() == firstCombo.getSuit():
      if self.get(i).equals(self.get(i + 1)):
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
      if self.get(i).equals(self.get(i + 1)):
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
      if i.equals(toCheck):
        numCards-=1
    return numCards <= 0
  def has(self, card, numCards):
    return self.getCount(card) >= numCards
class Deck (CardCollection):  

  DECK_SIZE = 54
  
  def __init__(self, numDecks):
    super().__init__()
    self.addDecks(numDecks)
    self.shuffle()

  """
   * Adds a complete deck of playing cards into the main deck.
  """
  def addDeck(self):
    for i in range(self.DECK_SIZE): 
      self.addCard(Card(i))

  """
   * adds multiple decks into main deck
  """
  def addDecks(self, numDecks):
    for i in range(numDecks):
      self.addDeck()

  def draw(self): 
    return self.remove(0)
class ComboType:
  SINGLE, PAIR, NONE, TRACTOR = range(4)
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
      if self.get(i).getPowerIndex() != self.get(i + numCopies).getPowerIndex():
        return False
      if self.getCount(self.get(i)) == numCopies:
        return False
    return True

  def isPair(self):
    return self.size() == 2 and self.get(0).equals(self.get(1))

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
      if self.get(i).equals(self.get(i + 1)):
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
class Card:
  VALUES = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]
  JOKERS = [ "J-", "J+" ]
  SUITS = [ '
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
TractorGame()