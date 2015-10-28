from Player import Player
from Trick import Trick
from Deck import Deck
from Card import Card
from Call import Call
from Combo import Combo
from ComboType import ComboType
from SortedCardCollection import SortedCardCollection

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
    Card.trumpValue = Player.players[self.boss].level
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
    if self.callLevel >= 0 and call.count == 1:
      return False
    return newCallLevel > self.callLevel and player.has(call.card, call.count) and call.isValid()
  
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
    challengerTeam = self.playerTeams[self.boss]
    for i in range(len(Player.players)):
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
    while not Player.players[0].isEmpty():
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
      Player.players[self.boss].addCard(self.mainDeck.draw())
    self.updateDisplay(Player.players[self.boss])
    print("~~~~~~~~~~~~~~~~~~")
    if True:
      for i in self.playCardsForBottom(Player.players[self.boss], 8, ComboType.NONE):
        self.mainDeck.addCard(i)
        Player.players[self.boss].remove(i)
    else:
      for i in range(8):
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