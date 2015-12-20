from Player import Player
from Trick import Trick
from Deck import Deck
from Card import Card
from Call import Call
from Combo import Combo
from ComboType import ComboType
from SortedCardCollection import SortedCardCollection

def printCardList(listOfCards):
  print("[", end="")
  for i in listOfCards:
    print(i.toString(), end=", ")
  print("]")
  
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
    self.winners = [False, False, False, False]
    self.boss = winner.id
    Card.trumpValue = Player.players[self.boss].level
    Card.trumpSuit = -1
    self.callLevel = -1
    self.currentPlayer = (self.boss - 1) % self.NUM_PLAYERS
  
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
    print("TrumpSuit: " + str(Card.trumpSuit))
  
  def canOverrideCurrent(self, player, call):
    newCallLevel = call.getCallLevel()
    if self.callLevel >= 0 and call.count == 1:
      return False
    return newCallLevel > self.callLevel and player.has(call.card, call.count) and call.isValid()
  
  def callTrump(self, playerID, call):
    player = Player.players[playerID]
    if self.canOverrideCurrent(player, call):
      Card.setTrumpSuit(call.getSuit())
      self.callLevel = call.getCallLevel()
      if self.roundCount == 1:
        self.boss = player.id
  
  def callTrumpInput(self, player):
    trumpInput = self.getUserInput("Call: ") ###
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
  
  def drawCard(self):
    if self.mainDeck.size() > Round.NUM_LEFTOVER:
      self.currentPlayer = (self.currentPlayer + 1) % self.NUM_PLAYERS
      newCard = self.mainDeck.draw()
      Player.players[self.currentPlayer].addCard(newCard)
      return True
    else:
      return False
  
  def dealAndCall(self):
    while self.mainDeck.size() > Round.NUM_LEFTOVER:
      for i in range(Round.NUM_PLAYERS):
        newCard = self.mainDeck.draw()
        Player.players[i].addCard(newCard)
        if Card.trumpSuit == 4:
          print()
          print("=== HAND (!" + Card.VALUES[Player.players[self.boss].level] + ")===")
        elif Card.trumpSuit != -1:
          print()
          print("=== HAND (" + Card.SUITS[Card.trumpSuit]  + Card.VALUES[Player.players[self.boss].level] + ")===")
        else:
          print()
          print("=== HAND (~" + Card.VALUES[Player.players[self.boss].level] + ")===")

        self.updateDisplay(Player.players[i])
        if True:
          self.callTrumpInput(Player.players[i])
  def determineWinners(self, challengersWin):
    incumbentsTeam = self.playerTeams[self.boss]
    for i in range(len(Player.players)):
      if (self.playerTeams[i] == incumbentsTeam) != challengersWin:
        self.winners[i] = True
  
  def display(self, string):
    print(string)
  
  def generateAllPossibleCalls(self, player):
    calls = []
    for i in range(1,3):
      for j in Card.SUITS:
        call = Call(Card(j+Card.VALUES[Card.trumpValue]), i)
        if self.canOverrideCurrent(player, call):
          calls.append(call)
    return calls
  def getPointsForChallengers(self):
    points = 0
    for i in range(Round.NUM_PLAYERS):
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
    inputString = self.getUserInput("") ###
    if inputString == "":
      return
    cardStrings = inputString.split(" ")
    for i in cardStrings:
      print(Card(i).cardIndex)
      cards.addCard(Card(i))
  def isComplete(self):
    for i in Player.players:
      if not i.isEmpty():
        return False
    return True
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
      Player.players[i].levelUp(level)
  
  def nextTrick(self):
    currentTrick = Trick()
    if Card.trumpSuit == 4:
      print("=== NEW TRICK (!" + Card.VALUES[Player.players[self.boss].level] + ")===")
    else:
      print("=== NEW TRICK (" + Card.SUITS[Card.trumpSuit] + Card.VALUES[Player.players[self.boss].level] + ")===")
    for i in Player.players:
      print("Player " + str(i.id) + ": " + str(self.playerPoints[i.id]) + " points")
    for i in range(Round.NUM_PLAYERS):
      if len(self.tricks) == 0:
        playerID = (i + self.boss) % Round.NUM_PLAYERS
      else:
        playerID = (i + self.tricks[len(self.tricks) - 1].getWinner()) % Round.NUM_PLAYERS
      self.updateDisplay(Player.players[playerID])
      self.playCards(Player.players[playerID], currentTrick)
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
    
  def buryCards(self, cards):
    cardsPlayed = SortedCardCollection()
    for i in cards:
      cardsPlayed.addCard(i)
    if len(cards) != self.NUM_LEFTOVER:
      return False
    if not cardsPlayed.isSubSet(Player.players[self.boss]):
        return False
    for i in cardsPlayed:
      self.mainDeck.addCard(i)
      Player.players[self.boss].remove(i)
      print(Player.players[self.boss].getCardCount())
    return True
    
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
    currentTrick.add(combo)
    player.removeCards(cardsPlayed)

  def playCardsForTrick(self, player, cards, currentTrick):
    cardsPlayed = SortedCardCollection()
    cardsPlayed.addCards(cards)
    combo = Combo(player, cardsPlayed)
    valid = self.validateCardsPlayed(combo, currentTrick, player)
    if valid:
      currentTrick.add(combo)
      player.removeCards(cardsPlayed)
      return True
    else:
      return False

  def populateTricks(self):
    while not Player.players[0].isEmpty():
      self.tricks.append(self.nextTrick())
  def nextRound(self):
    return Round(Player.players[self.getWinner()])
  def prepNextTrick(self):
    self.currentPlayer = self.currentTrick.getWinner()
    self.tricks.append(self.currentTrick)
    self.currentTrick = Trick()
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
      Player.players[self.boss].addCard(self.mainDeck.draw())
    self.updateDisplay(Player.players[self.boss])
    print("~~~~~~~~~~~~~~~~~~")
    if True:
      for i in self.playCardsForBottom(Player.players[self.boss], 8, ComboType.NONE):
        self.mainDeck.addCard(i)
        Player.players[self.boss].remove(i)
    else:
      for i in range(self.NUM_LEFTOVER):
        self.mainDeck.addCard(Player.players[self.boss].remove(0))
    self.updateDisplay(Player.players[self.boss])
    
  def start(self):
    self.dealAndCall()
    self.replaceBottom()
    for i in Player.players:
      i.sort()
    self.populateTricks()
    self.checkBottom()
    self.levelByPoints()
  
  def updateDisplay(self, player):
    print("Player " + str(player.id) + ": ", end="")
    for i in player:
      print(i.toString() + " ", end="")
    print()
  def getPlayerCircle(self):
    circle = {}
    circle['current'] = Player.players[self.currentPlayer]
    circle['left'] = Player.players[(self.currentPlayer + 3) % 4]
    circle['across'] = Player.players[(self.currentPlayer + 2) % 4]
    circle['right'] = Player.players[(self.currentPlayer + 1) % 4]
    return circle
  def updatePoints(self, winner, points):
    self.playerPoints[winner] += points
  def giveBottom(self, playerID):
    while not self.mainDeck.isEmpty():
      Player.players[playerID].addCard(self.mainDeck.draw())
  def incrementCurrentPlayer(self):
    self.currentPlayer = (self.currentPlayer + 1) % 4
  def validateCardsPlayed(self, combo, currentTrick, player):
    if combo.isEmpty():
      return False
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