def printCardList(listOfCards):
  print("[", end="")
  for i in listOfCards:
    print(i.toString(), end=", ")
  print("]")
class TractorGame:

  NUM_PLAYERS = 4 #static final int NUM_PLAYERS = 4;
  NUM_DECKS = 2   #static final int NUM_DECKS = 2;
  TESTING = True  #public static final boolean TESTING = true;
  #static Player[] players;
  
  def __init__(self):
    self.startGame()
    
  def startGame(self):#public static void startGame() {

    currentRound = None#Round currentRound = null;
    TractorGame.players = []#players = new Player[NUM_PLAYERS];

    for i in range(TractorGame.NUM_PLAYERS): #for (int i = 0; i < players.length; i++) {
      TractorGame.players.append(Player(i))#players[i] = new Player(i);
    #}

    while True: #while (True) {
      if currentRound == None: #if (currentRound == null) {
        currentRound = Round(TractorGame.players[0])#currentRound = new Round(players[0]);
      else: #} else {
        currentRound = Round(TractorGame.players[currentRound.getWinner()])#currentRound = new Round(players[currentRound.getWinner()]);
      #}
      currentRound.start()#currentRound.start();
    #}
  #}

  #public static void main(String[] args) {
  #  startGame();
  #}
#}
#package tractor;

#import java.util.ArrayList;
#import java.util.List;
import random
class CardCollection:#public class CardCollection implements Iterable<Card> {
  #protected List<Card> cards;

  def __iter__(self):
    return self
    
  def __next__(self):
    if self.index == len(self.cards):
      self.index = 0
      raise StopIteration
    else:
      self.index += 1
      return self.cards[self.index - 1]
      
  def __init__(self):#public CardCollection() {
    self.index = 0
    self.cards = []#cards = new ArrayList<Card>();
  #}

  def addCards(self, cc): #public void addCards(CardCollection cc) {
    for i in cc:#for (Card i : cc) {
      self.cards.append(i)#cards.add(i);
    #}
  #}

  def addCard(self, card):#public void addCard(Card card) {
    self.cards.append(card)#cards.add(card);
  #}

  def countSuit(self, suit):#public int countSuit(int suit) {
    count = 0#int count = 0;
    for i in self.cards:#for (Card i : cards) {
      if i.getSuit() == suit:#if (i.getSuit() == suit) {
        count += 1#count++;
      #}
    #}
    return count#return count;
  #}

  def get(self, i):#public Card get(int i) {
    return self.cards[i]#return cards.get(i);
  #}

  def getCount(self, c):#public int getCount(Card c) {
    return sum(c.equals(card) for card in self.cards)#return Collections.frequency(cards, c);
  #}

  def getCardCount(self):#public int getCardCount() {
    return len(self.cards)#return cards.size();
  #}

  def isEmpty(self):#public boolean isEmpty() {
    return len(self.cards) == 0#return cards.isEmpty();
  #}

  #@Override
  #public Iterator<Card> iterator() {
  #  return cards.iterator();
  #}

  def remove(self, i):#public boolean remove(Card i) {
    if type(i) == Card:
      return self.cards.remove(i)#return cards.remove(i);
    else:
      return self.cards.pop(i)
  #}

  #public Card remove(int i) {
  #  return cards.remove(i);
  #}

  def removeAll(self):#public void removeAll() {
    self.cards.clear()#cards.removeAll(cards);
  #}

  def removeCards(self, cards):#public void removeCards(CardCollection cards) {
    
    for i in cards.cards:#for (Card i : cards) {
      printCardList(cards.cards)
      print(i.toString())
      self.cards.remove(i)#this.cards.remove(i);
    #}
  #}

  def shuffle(self):#public void shuffle() {
    if TractorGame.TESTING:
      random.seed(0)
    else:
      random.seed()#long seed = TractorGame.TESTING ? 1445123063075L : System.currentTimeMillis();
    random.shuffle(self.cards)#Collections.shuffle(cards, new Random(seed));
  #}

  def size(self):#public int size() {
    return len(self.cards)#return cards.size();
  #}
    
  def sort(self): #public void sort() {
    self.cards.sort()#Collections.sort(cards);
  #}
class SortedCardCollection(CardCollection):#public class SortedCardCollection extends CardCollection {

  def __init__(self):
    super().__init__()
  
  def addCard(self, card):#public void addCard(Card card) {
    super().addCard(card)#super.addCard(card);
    self.sort()#sort();
  #}
#
  def addCards(self, cc):#public void addCards(CardCollection cc) {
    super().addCards(cc)#super.addCards(cc);
    self.sort()#sort();
  #}

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
    
  def isSubSet1(self, o):#public boolean isSubSet(SortedCardCollection o) {
    #print("111")
    sortedSubList = self.copyCardsList(self.cards)#List<Card> sortedSubList = new ArrayList<Card>(cards);
    print("sortedSubList: ", end="")
    for i in sortedSubList:
      print(i.toString(), end="")
    print()
    #print("222")
    sortedSuperList = self.copyCardsList(o.cards)#List<Card> sortedSuperList = new ArrayList<Card>(o.cards);
    print("sortedSuperList: ", end="")
    for i in sortedSuperList:
      print(i.toString(), end="")
    print()
    #print("333")
    j = 0#int j = 0;
    for i in range(len(sortedSubList)):#for (int i = 0; i < sortedSubList.size(); i++) {
      notSubset = False#boolean notSubset = false;
      while True:#while (true) {
        print ("comparing " + sortedSubList[i].toString() + " and " + sortedSuperList[j].toString())
        if sortedSubList[i].equals(sortedSuperList[j]):#if (sortedSubList.get(i).equals(sortedSuperList.get(j))) {
          j += 1#j++;
          break#break;
        #}
        j += 1#j++;
        if j >= len(sortedSuperList):#if (j >= sortedSuperList.size()) {
          notSubset = True#notSubset = true;
          break#break;
        #}
      #}
      if notSubset or j == len(sortedSuperList):#if (notSubset || j == sortedSuperList.size()) {
        print(False)
        return False#return false;
      #}
    #}
    return True#return true;
  #}
#}
#package tractor;

#import java.util.ArrayList;
#import java.util.Scanner;
#from TractorGame import TractorGame

class Round:#public class Round {
  NUM_PLAYERS = 4#static final int NUM_PLAYERS = 4;
  NUM_DECKS = 2#static final int NUM_DECKS = 2;
  NUM_LEFTOVER = 8#static final int NUM_LEFTOVER = 8;
  roundCount = 0#static int roundCount = 0;
  #Deck mainDeck;
  #int boss;
  #ArrayList<Trick> tricks;
  #boolean[] winners;
  playerTeams = [0, 1, 0, 1]#int[] playerTeams = { 0, 1, 0, 1 };
  playerPoints = [0, 0, 0, 0]#int[] playerPoints = { 0, 0, 0, 0 };
  #private int callLevel;
#
  def __init__(self, winner):#public Round(Player winner) {
    Round.roundCount+=1#roundCount++;
    self.mainDeck = Deck(Round.NUM_DECKS)#mainDeck = new Deck(NUM_DECKS);
    self.tricks = []#tricks = new ArrayList<Trick>();
    self.boss = winner.id#boss = winner.id;
    Card.trumpValue = TractorGame.players[self.boss].level#Card.trumpValue = TractorGame.players[boss].level;
    Card.trumpSuit = -1#Card.trumpSuit = -1;
    self.callLevel = -1#callLevel = -1;
  #}
#
  def autoAssignTrumpSuit(self):#private void autoAssignTrumpSuit() {
    print("Bottom 8: ", end="")#System.out.print("Bottom 8: ");
    for i in self.mainDeck:#for (Card i : mainDeck) {
      print(i.toString() + " ", end="")#System.out.print(i.toString() + " ");
    #}
#
    for i in self.mainDeck:#for (Card i : mainDeck) {
      if i.getValue() == Card.trumpValue:#if (i.getValue() == Card.trumpValue) {
        Card.trumpSuit = i.getRawSuit()#Card.trumpSuit = i.getRawSuit();
        return#return;
      #}
    #}
    selector = None#Card selector = null;
    for i in self.mainDeck:#for (Card i : mainDeck) {
      if selector == None or selector.getValue() < i.getValue():#if (selector == null || selector.getValue() < i.getValue()) {
        if selector == None or not selector.isJoker():#if (!selector.isJoker()) {
          selector = i#selector = i;
        #}
      #}
    #}
    print(selector, end="")#System.out.print(selector);
    Card.trumpSuit = selector.getSuit()#Card.trumpSuit = selector.getSuit();
  #}
#
  def canOverrideCurrent(self, player, call):#private boolean canOverrideCurrent(Player player, Call call) {
    newCallLevel = call.getCallLevel()#int newCallLevel = call.getCallLevel();
    return newCallLevel > self.callLevel and player.has(call.card, call.count)#return newCallLevel > callLevel && player.has(call.card, call.count);
  #}
#
  def callTrumpInput(self, player):#private void callTrumpInput(Player player) {
    trumpInput = self.getUserInput("Call: ")#String trumpInput = getUserInput("Call: ");
#
    if trumpInput == "":#if (trumpInput.equals("")) {
      return#return;
    #}
    #
    call = Call(trumpInput[1:], int(trumpInput[:1]))#Call call = new Call(trumpInput.substring(1), Integer.parseInt(trumpInput.substring(0, 1)));
    if self.canOverrideCurrent(player, call):#if (canOverrideCurrent(player, call)) {
      Card.setTrumpSuit(call.getSuit())#Card.setTrumpSuit(call.getSuit());
      self.callLevel = call.getCallLevel()#callLevel = call.getCallLevel();
      if self.roundCount == 1:#if (roundCount == 1) {
        self.boss = player.id#boss = player.id;
      #}
    #}
  #}
#
  def challengersWin(self):#private void challengersWin() {
    self.determineWinners(True)#determineWinners(true);
  #}
#
  def checkBottom(self):#private void checkBottom() {
    points = 0#int points = 0;
    for i in self.mainDeck:#for (Card i : mainDeck) {
      points += i.getPoints()#points += i.getPoints();
    #}
    multiplier = 2#int multiplier = 2;
    lastTrick = self.tricks[-1]#Trick lastTrick = tricks.get(tricks.size() - 1);
    
    if lastTrick.getType() == ComboType.SINGLE:#switch (lastTrick.getType()) {#case SINGLE:
      multiplier = 2#multiplier = 2;
      #break;
    elif lastTrick.getType() == ComboType.PAIR:#case PAIR:
      multiplier = 4#multiplier = 4;
      #break;
    elif lastTrick.getType() == ComboType.TRACTOR:#case TRACTOR:
      multiplier = lastTrick.getNumCards() * 2#multiplier = lastTrick.getNumCards() * 2;
    #default:
      #break;
    #}
    print(lastTrick.getWinner())#System.out.println(tricks.get(tricks.size() - 1).getWinner());
    self.playerPoints[lastTrick.getWinner()] += points * multiplier#playerPoints[tricks.get(tricks.size()).getWinner()] += points * multiplier;
  #}
#
  def dealAndCall(self):#private void dealAndCall() {
    while self.mainDeck.size() > Round.NUM_LEFTOVER:#while (mainDeck.size() > NUM_LEFTOVER) {
      for i in range(Round.NUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
        newCard = self.mainDeck.draw()#Card newCard = mainDeck.draw();
        TractorGame.players[i].addCard(newCard)#TractorGame.players[i].addCard(newCard);
        if Card.trumpSuit == 4:#if (Card.trumpSuit == 4) {
          print("\n=== HAND (!" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
        elif Card.trumpSuit != -1:#} else if (Card.trumpSuit != -1) {
          print("\n=== HAND (" + Card.SUITS[Card.trumpSuit]  + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
        else:
          print("\n=== HAND (~" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")

        self.updateDisplay(TractorGame.players[i])#updateDisplay(TractorGame.players[i]);
        if False:#if (true) {
          self.callTrumpInput(TractorGame.players[i])#callTrumpInput(TractorGame.players[i]);
        #}
#
      #}
    #}
  #}
#
  def determineWinners(self, challengersWin):#private void determineWinners(boolean challengersWin) {
    challengerTeam = self.playerTeams[self.boss]#int challengerTeam = playerTeams[boss];
    for i in range(len(TractorGame.players)):#for (int i = 0; i < TractorGame.players.length; i++) {
      if (self.playerTeams[i] == challengerTeam) == challengersWin:#if ((playerTeams[i] == challengerTeam) == challengersWin) {
        self.winners[i] = True#winners[i] = true;
      #}
    #}
  #}
#
  def display(self, string):#private void display(String string) {
    print(string)#System.out.println(string);
  #}
#
  def getPointsForChallengers(self):#private int getPointsForChallengers() {
    points = 0#int points = 0;
    for i in range(RoundNUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
      if self.playerTeams[i] != self.playerTeams[self.boss]:#if (playerTeams[i] != playerTeams[boss]) {
        points += self.playerPoints[i]#points += playerPoints[i];
      #}
    #}
    return points#return points;
  #}
#
  def getUserInput(self, prompt):#private String getUserInput(String prompt) {
    #System.out.print(prompt);
    #@SuppressWarnings("resource")
    #Scanner scanner = new Scanner(System.in);
    #String inputString = scanner.nextLine();
    #// scanner.close()#// scanner.close();
    return input(prompt)#return inputString;
  #}
#
  def getWinner(self):#public int getWinner() { // used for creation of subsequent round
    for i in range(Round.NUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
      if self.winners[(i + self.boss + 1) % Round.NUM_PLAYERS]:#if (winners[(i + boss + 1) % NUM_PLAYERS]) {
        return (i + self.boss + 1) % Round.NUM_PLAYERS#return (i + boss + 1) % NUM_PLAYERS;
      #}
    #}
    return -1#should never happen#return -1; // should never happen
  #}
#
  def incumbentsWin(self):#private void incumbentsWin() {
    self.determineWinners(False)#determineWinners(false);
  #}
#
  def inputCardsPlayed(self, cards, player):# {#private void inputCardsPlayed(CardCollection cards, Player player) {
    print("Cards (" + str(cards.size()) + "): ", end="")#System.out.print("Cards (" + cards.size() + "): ");
    #print("!!!!!")
    for i in cards:#for (Card i : cards) {
      print(i.toString() + " ", end="")#System.out.print(i + " ");
    #print("!!!!!")
    inputString = self.getUserInput("")#String inputString = getUserInput("");
    if inputString == "":#if (inputString.equals(""))
      return#return;
    cardStrings = inputString.split(" ")#String[] cardStrings = inputString.split(" ");
    for i in cardStrings:#for (String i : cardStrings) {
      print(Card(i).cardIndex)
      cards.addCard(Card(i))#cards.addCard(new Card(i));
    #}
  #}
#
  def levelByPoints(self):#private void levelByPoints() {
    points = self.getPointsForChallengers()
    if points < 80:#if (getPointsForChallengers() < 80) {
      self.incumbentsWin()#incumbentsWin();
      if points == 0:#if (getPointsForChallengers() == 0) {
        self.levelUpWinners(3)#levelUpWinners(3);
      elif points < 40:#} else if (getPointsForChallengers() < 40) {
        self.levelUpWinners(2)#levelUpWinners(2);
      elif points < 80:#} else if (getPointsForChallengers() < 80) {
        self.levelUpWinners(1)#levelUpWinners(1);
      #}
    else:#} else {
      self.challengersWin()#challengersWin();
      self.levelUpWinners(int(points / 40) - 2)#levelUpWinners(getPointsForChallengers() / 40 - 2);
    #}
  #}
#
  def levelUpWinners(self, level):#private void levelUpWinners(int level) {
    for i in range(Round.NUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
      TractorGame.players[i].levelUp(level)#TractorGame.players[i].levelUp(level);
    #}
  #}
#
  def nextTrick(self):#private Trick nextTrick() {
    currentTrick = Trick()#Trick currentTrick = new Trick();
    if Card.trumpSuit == 4:#if (Card.trumpSuit == 4) {
      print("=== NEW TRICK (!" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")#System.out.println("=== NEW TRICK (!" + Card.VALUES[TractorGame.players[boss].level] + ")===");
    else:#} else {
      print("=== NEW TRICK (" + Card.SUITS[Card.trumpSuit] + Card.VALUES[TractorGame.players[self.boss].level] + ")===")#"=== NEW TRICK (" + Card.SUITS[Card.trumpSuit] + Card.VALUES[TractorGame.players[boss].level] + ")===");
    #}
#
    for i in TractorGame.players:#for (Player i : TractorGame.players) {
      print("Player " + str(i.id) + ": " + str(self.playerPoints[i.id]) + " points")#System.out.println("Player " + i.id + ": " + playerPoints[i.id] + " points");
    #}
#
    for i in range(Round.NUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
      #print("~~~~" + str(i))
      if len(self.tricks) == 0:#if (tricks.size() == 0) {
        playerID = (i + self.boss) % Round.NUM_PLAYERS#playerID = boss;
      else:#}else{
        playerID = (i + self.tricks[len(self.tricks) - 1].getWinner()) % Round.NUM_PLAYERS#playerID = (i + tricks.get(tricks.size() - 1).getWinner()) % NUM_PLAYERS;
      #}
#
      self.updateDisplay(TractorGame.players[playerID])#updateDisplay(TractorGame.players[playerID]);
      self.playCards(TractorGame.players[playerID], currentTrick)#playCards(TractorGame.players[playerID], currentTrick);
    #}
    self.updatePoints(currentTrick.getWinner(), currentTrick.getPoints())#updatePoints(currentTrick.getWinner(), currentTrick.getPoints());
    print("Player " + str(currentTrick.getWinner()) + " wins trick and earns " + str(currentTrick.getPoints())#System.out.println("Player " + currentTrick.getWinner() + " wins trick and earns " + currentTrick.getPoints()
        + " points!")#+ " points!");
    return currentTrick#return currentTrick;
  #}
#
  def playCardsForBottom(self, player, numCards, c):#private Card[] playCards(Player player, int numCards, ComboType c) {
    #print("@@@@@@")
    cardsPlayed = SortedCardCollection()#SortedCardCollection cardsPlayed = new SortedCardCollection();
    while cardsPlayed.size() != numCards:#while (cardsPlayed.size() != numCards) {
      #print("AAAAAAA")
      if not cardsPlayed.isSubSet(player) or cardsPlayed.size() > 8:#if (!cardsPlayed.isSubSet(player) || cardsPlayed.size() > 8) {
        cardsPlayed.removeAll()#cardsPlayed.removeAll();
      #print("BBBBBBB")
      #print("!!!!!")
      self.inputCardsPlayed(cardsPlayed, player)#inputCardsPlayed(cardsPlayed, player);
      
      #print("&&&&&&&&")
    #}
    
    cards = []#Card[] cards = new Card[numCards];
    for i in range(numCards):#for (int i = 0; i < numCards; i++) {
      cards.append(cardsPlayed.get(i))#cards[i] = cardsPlayed.get(i);
    #}
    
    return cards#return cards;
  #}
#
  def playCards(self, player, currentTrick):#private void playCards(Player player, Trick currentTrick) {
    cardsPlayed = SortedCardCollection()#CardCollection cardsPlayed = new SortedCardCollection();
    valid = False#boolean valid = false;
    combo = None#Combo combo = null;
    while not valid:#while (!valid) {
      self.inputCardsPlayed(cardsPlayed, player)#inputCardsPlayed(cardsPlayed, player);
      #printCardList(cardsPlayed)
      #printCardList(player)
      combo = Combo(player, cardsPlayed)#combo = new Combo(player, cardsPlayed);
      valid = self.validateCardsPlayed(combo, currentTrick, player)#valid = validateCardsPlayed(combo, currentTrick, player);
      #printCardList(cardsPlayed)
      #printCardList(player)
      if not valid:#if (!valid) {
        print("Invalid!")#display("Invalid!");
        cardsPlayed.removeAll()#cardsPlayed.removeAll();
        #printCardList(player)
      else:
        print("VALID!")
      #}
    printCardList(player)
    #}
    currentTrick.add(combo)#currentTrick.add(combo);
    printCardList(player)
    player.removeCards(cardsPlayed)#player.removeCards(cardsPlayed);#$$$
    printCardList(player)
  #}
#
  def populateTricks(self):#private void populateTricks() {
    while not TractorGame.players[0].isEmpty():#while (!TractorGame.players[0].isEmpty()) {
      self.tricks.append(self.nextTrick())#tricks.add(nextTrick());
    #}
  #}
#
  def replaceBottom(self):#private void replaceBottom() {
    if Card.trumpSuit == -1:#if (Card.trumpSuit == -1) {
      self.autoAssignTrumpSuit()#autoAssignTrumpSuit();
    #}
    if Card.trumpSuit == 4:#if (Card.trumpSuit == 4) {
      print("\n=== REPLACE BOTTOM (!)===")
    else:
      print("\n=== REPLACE BOTTOM (" + Card.SUITS[Card.trumpSuit] + ")===")
    

    while not self.mainDeck.isEmpty():#while (!mainDeck.isEmpty()) {
      TractorGame.players[self.boss].addCard(self.mainDeck.draw())#TractorGame.players[boss].addCard(mainDeck.draw());
    #}
    self.updateDisplay(TractorGame.players[self.boss])#updateDisplay(TractorGame.players[boss]);
    print("~~~~~~~~~~~~~~~~~~")
    if False:
      for i in self.playCardsForBottom(TractorGame.players[self.boss], 8, ComboType.NONE):#for (Card i : playCards(TractorGame.players[boss], 8, ComboType.NONE)) {
        self.mainDeck.addCard(i)#mainDeck.addCard(i);
        TractorGame.players[self.boss].remove(i)#TractorGame.players[boss].remove(i);
    else:
      for i in range(8):
        self.mainDeck.addCard(TractorGame.players[self.boss].remove(0))
    self.updateDisplay(TractorGame.players[self.boss])#updateDisplay(TractorGame.players[boss]);
  #}
#
  def start(self):#public void start() {
    self.dealAndCall()#dealAndCall();
    self.replaceBottom()#replaceBottom();
    for i in TractorGame.players:#for (Player i : TractorGame.players) {
      i.sort()#i.sort();
    #}
    self.populateTricks()#populateTricks();
    self.checkBottom()#checkBottom();
    self.levelByPoints()#levelByPoints();
  #}
#
  def updateDisplay(self, player):#private void updateDisplay(Player player) {
    print("Player " + str(player.id) + ": ", end="")#System.out.print("Player " + player.id + ": ");
    for i in player:#for (Card i : player) {
      print(i.toString() + " ", end="")#System.out.print(i.toString() + " ");
    #}
    print()#System.out.println();
  #}
#
  def updatePoints(self, winner, points):#private void updatePoints(int winner, int points) {
    self.playerPoints[winner] += points#playerPoints[winner] += points;
  #}
#
  def validateCardsPlayed(self, combo, currentTrick, player):#private boolean validateCardsPlayed(Combo combo, Trick currentTrick, Player player) {
#
    if currentTrick.isEmpty():#if (currentTrick.isEmpty()) {
      #// first combo played, as long as same suit and valid type, is valid
      print("First combo played: " + str(combo.getType()))#System.out.println("First combo played: " + combo.getType());
      return combo.getType() != ComboType.NONE#return combo.getType() != ComboType.NONE;
    #}
    first = currentTrick.combos[0]#Combo first = currentTrick.combos.get(0);
    if combo.size() == first.size():#if (combo.size() == first.size()) {
      #// number of cards is right
      if combo.getSuit() != first.getSuit():#if (combo.getSuit() != first.getSuit()) {
        #// suits aren't the same
        if player.countSuit(first.getSuit()) == combo.countSuit(first.getSuit()):#if (player.countSuit(first.getSuit()) == combo.countSuit(first.getSuit())) {
          return True#return true;
        else:#} else {
          return False#return false;
        #}
      else:#} else {
        #// suits are the same
        if combo.getType() == first.getType():#if (combo.getType() == first.getType()) {
          #// comboTypes are the same
          return True#return true;
        else:#} else {
          #// comboTypes aren't the same
          print("combos aren't the same")#System.out.println("combos aren't the same");
          if player.hasComboToPlay(first):#if (player.hasComboToPlay(first)) {
            return False#return false;
          elif player.playedRequired(first, combo):#} else if (player.playedRequired(first, combo)) {
            print("doesn't have that combo")#System.out.println("doesn't have that combo");
            return True#return true;
          #}
        #}
      #}
    #}
    return False#return false;
  #}
#
#}
##package tractor;
#
#import java.util.ArrayList;
#import java.util.Collections;
#import java.util.List;
class Player(SortedCardCollection):#public class Player extends SortedCardCollection {
  #int id, level;
  def __init__(self, i):#public Player(int i) {
    super().__init__()#super();
    self.id = i#id = i;
    self.level = 0#level = 0;
  #}
#
  def levelUp(self, level):#public void levelUp(int level) {
    self.level += level#this.level += level;
  #}
#
  def hasComboToPlay(self, firstCombo):#public boolean hasComboToPlay(Combo firstCombo) {
    #// TODO: refactor
    #// has to be pair or tractor
    #// the hard part is that tractors have multiple
    #// easiest is to find biggest number of consecutive pairs in the suit
    #// TODO make sure everything works with SHUAI
    currentCount = 0#int currentCount = 0;
    maxCount = 0#int maxCount = 0;
    startOfSuit = 0#int startOfSuit = 0;
    #// find start of suit
    for i in self.size():#for (int i = 0; i < size(); i++) {
      if self.get(i).getSuit() == firstCombo.getSuit():#if (get(i).getSuit() == firstCombo.getSuit()) {
        startOfSuit = i#startOfSuit = i;
        break#break;
      #}
    #}
    i = startOfSuit#int i = startOfSuit;
    lastPair = -1#int lastPair = -1;
    while i < self.size() - 1 and self.get(i).getSuit() == firstCombo.getSuit():#while (i < size() - 1 && get(i).getSuit() == firstCombo.getSuit()) {
      if self.get(i).equals(self.get(i + 1)):#if (get(i).equals(get(i + 1))) {// is a pair
        if lastPair == self.get(i).getPowerIndex():#if (lastPair == get(i).getPowerIndex()) {
          i += 2#i += 2;
          continue#continue;
        elif lastPair == -1 or self.get(i).getPowerIndex() != lastPair + 1:#} else if (lastPair == -1 || get(i).getPowerIndex() != lastPair + 1) {
          #// start of new pair list
          currentCount = 1#currentCount = 1;
#
        else:#} else { // continuing list of consecutive
          currentCount += 1#currentCount++;
        #}
        if currentCount > maxCount:#if (currentCount > maxCount) {
          maxCount = currentCount#maxCount = currentCount;
        #}
        lastPair = self.get(i).getPowerIndex()#lastPair = get(i).getPowerIndex();
        i += 2#i += 2;
      else: #} else { // not a pair
        i += 1#i++;
      #}
    #}
    if maxCount * 2 >= firstCombo.size():#if (maxCount * 2 >= firstCombo.size()) {
      return True#return true;
    #}
    return False#return false;
  #}
#
  def playedRequired(self, firstCombo, attemptedCombo):#public boolean playedRequired(Combo firstCombo, Combo attemptedCombo) {
    #// TODO: refactor
    handConsecPairCounts = self.consecutivePairCounts(firstCombo)#List<Integer> handConsecPairCounts = consecutivePairCounts(firstCombo);
    comboConsecPairCounts = attemptedCombo.consecutivePairCounts(firstCombo)#List<Integer> comboConsecPairCounts = attemptedCombo.consecutivePairCounts(firstCombo);
    numberOfCardsNeeded = firstCombo.size()#int numberOfCardsNeeded = firstCombo.size();
    i = 0#int i = 0;
    while numberOfCardsNeeded != 0 and i < len(handConsecPairCounts):#while (numberOfCardsNeeded != 0 && i < handConsecPairCounts.size()) {
      if i >= len(comboConsecPairCounts):#if (i >= comboConsecPairCounts.size()) {
        return False#return false;
      #}
      if handConsecPairCounts[i] * 2 <= numberOfCardsNeeded:#if (handConsecPairCounts.get(i) * 2 <= numberOfCardsNeeded) {
        if comboConsecPairCounts[i] != handConsecPairCounts[i]:#if (comboConsecPairCounts.get(i) != handConsecPairCounts.get(i)) {
          return False#return false;
        #}
        numberOfCardsNeeded -= handConsecPairCounts[i]#numberOfCardsNeeded -= handConsecPairCounts.get(i);
      else:#} else {
        if comboConsecPairCounts[i] != numberOfCardsNeeded:#if (comboConsecPairCounts.get(i) != numberOfCardsNeeded) {
          return False#return false;
        else:#} else {
          return True#return true;
        #}
      #}
      i+=1#i++;
    #}
    return True#return true;
  #}
#
  def consecutivePairCounts(self, firstCombo):#public List<Integer> consecutivePairCounts(Combo firstCombo) {
    #// TODO: refactor
    consecPairCounts = []#List<Integer> consecPairCounts = new ArrayList<Integer>();
    currentCount = 0#int currentCount = 0;
    maxCount = 0#int maxCount = 0;
    startOfSuit = 0#int startOfSuit = 0;
    #// find start of suit
    for i in range(self.size()):#for (int i = 0; i < size(); i++) {
      if self.get(i).getSuit() == firstCombo.getSuit():#if (get(i).getSuit() == firstCombo.getSuit()) {
        startOfSuit = i#startOfSuit = i;
        break#break;
      #}
    #}
    i = startOfSuit#int i = startOfSuit;
    lastPair = -1#int lastPair = -1;
    while i < self.size() - 1 and self.get(i).getSuit() == firstCombo.getSuit():#while (i < size() - 1 && get(i).getSuit() == firstCombo.getSuit()) {
      if self.get(i).equals(self.get(i + 1)):#if (get(i).equals(get(i + 1))) {// is a pair
        if lastPair == self.get(i).getPowerIndex():#if (lastPair == get(i).getPowerIndex()) {
          i += 2#i += 2;
          continue#continue;
        elif lastPair == -1 or self.get(i).getPowerIndex() != lastPair + 1:#} else if (lastPair == -1 || get(i).getPowerIndex() != lastPair + 1) {
          #// start of new pair list
          currentCount = 1#currentCount = 1;
#
        else:#} else { // continuing list of consecutive
          currentCount += 1#currentCount++;
        #}
        if currentCount > maxCount:#if (currentCount > maxCount) {
          maxCount = currentCount#maxCount = currentCount;
        #}
        lastPair = self.get(i).getPowerIndex()#lastPair = get(i).getPowerIndex();
        i += 2#i += 2;
      else: #} else { // not a pair
        i+=1#i++;
        if currentCount > 0:#if (currentCount > 0) {
          consecPairCounts.add(currentCount)#consecPairCounts.add(currentCount);
        #}
        currentCount = 0#currentCount = 0;
      #}
#
    #}
    if currentCount > 0:#if (currentCount > 0) {
      consecPairCounts.append(currentCount)#consecPairCounts.add(currentCount);
    #}
    consecPairCounts.sort()#Collections.sort(consecPairCounts);
    consecPairCounts.reverse()#Collections.reverse(consecPairCounts);
    return consecPairCounts#return consecPairCounts;
  #}
#
  def canOverride(self, player, newCallLevel):#public boolean canOverride(Player player, int newCallLevel) {
    #// TODO: refactor
    numCards = int(newCallLevel / 6) + 1#int numCards = newCallLevel / 6 + 1;
    suit = newCallLevel % 6#int suit = newCallLevel % 6;
    toCheck = None#Card toCheck = None;
    if suit == 5:#if (suit == 5) {
      toCheck = Card("J+")#toCheck = new Card("J+");
      if numCards == 1:#if (numCards == 1) {
        return False#return false;
      #}
    elif suit == 4:#} else if (suit == 4) {
      toCheck = Card("J-")#toCheck = new Card("J-");
      if numCards == 1:#if (numCards == 1) {
        return False#return false;
      #}
    else:#} else {
      toCheck = Card(Card.SUITS[suit] + Card.VALUES[Card.trumpValue])#toCheck = new Card(Card.SUITS[suit] + Card.VALUES[Card.trumpValue]);
    #}
    for i in self:#for (Card i : this) {
      if i.equals(toCheck):#if (i.equals(toCheck)) {
        numCards-=1#numCards--;
      #}
    #}
    return numCards <= 0#return numCards <= 0;
  #}
#
  def has(self, card, numCards):#public boolean has(Card card, int numCards) {
    return self.getCount(card) >= numCards#return getCount(card) >= numCards;
  #}
#
#}
##package tractor;

class Deck (CardCollection):  #public class Deck extends CardCollection {

  DECK_SIZE = 54#private static final int DECK_SIZE = 54;
  
  def __init__(self, numDecks):#public Deck(int numDecks) {
    super().__init__()#super();
    self.addDecks(numDecks)#addDecks(numDecks);
    self.shuffle()#shuffle();
  #}

  """
   * Adds a complete deck of playing cards into the main deck.
  """
  def addDeck(self):#private void addDeck() {
    for i in range(self.DECK_SIZE): #for (int i = 0; i < DECK_SIZE; i++) {
      self.addCard(Card(i))#addCard(new Card(i));
    #}
  #}

  """
   * adds multiple decks into main deck
  """
  def addDecks(self, numDecks):#private void addDecks(int numDecks) {
    for i in range(numDecks):#for (int i = 0; i < numDecks; i++) {
      self.addDeck()#addDeck();
    #}
  #}

  def draw(self): #public Card draw() {
    return self.remove(0)#return remove(0);
  #}
#}
#package tractor;

class ComboType:#public enum ComboType {
  SINGLE, PAIR, NONE, TRACTOR = range(4)#SINGLE, PAIR, NONE, TRACTOR
#}
#package tractor;

#import java.util.ArrayList;
#import java.util.Collections;
#import java.util.List;

class Combo(SortedCardCollection):#public class Combo extends SortedCardCollection {
  #Player player;

  def __init__(self, player, cardsPlayed):#public Combo(Player player, CardCollection cardsPlayed) {
    super().__init__()#super();
    self.addCards(cardsPlayed)#addCards(cardsPlayed);
    self.player = player#this.player = player;
  #}

  def isSameSuit(self):#public boolean isSameSuit() {
    suit = -1#int suit = -1;
    for i in self:#for (Card i : this) {
      if suit == -1:#if (suit == -1) {
        suit = i.getSuit()#suit = i.getSuit();
      #}
      if suit != i.getSuit():#if (suit != i.getSuit()) {
        return False#return false;
      #}
    #}
    return True#return true;
  #}

  def getSuit(self):#public int getSuit() {
    if self.isSameSuit():#if (isSameSuit()) {
      return self.cards[0].getSuit()#return cards.get(0).getSuit();
    #}
    return -1#return -1;
  #}

  def getsBeatenBy(self, challenger, first): #public boolean getsBeatenBy(Combo challenger, Combo first) {
    return self.getPower(first) < challenger.getPower(first)#return getPower(first) < challenger.getPower(first);
  #}

  def getPower(self, first):#public int getPower(Combo first) {
    if self.getType() == ComboType.NONE or self.getType() != first.getType():#if (getType() == ComboType.NONE || getType() != first.getType()) {
      return 0#return 0;
    #}
    if self.getSuit() != first.getSuit() and self.getSuit() != Card.TRUMP_SUIT:#if (getSuit() != first.getSuit() && getSuit() != Card.TRUMP_SUIT) {
      return 0#return 0;
    #}

    power = self.get(0).getPowerIndex()#int power = get(0).getPowerIndex();
    return power#return power;
  #}

  def getType(self):#public ComboType getType() {
    if self.isMixedSuit():#if (isMixedSuit()) {
      return ComboType.NONE#return ComboType.NONE;
    elif self.isSingle():#} else if (isSingle()) {
      return ComboType.SINGLE#return ComboType.SINGLE;
    elif self.isPair():#} else if (isPair()) {
      return ComboType.PAIR#return ComboType.PAIR;
    elif self.isTractor():#} else if (isTractor()) {
      return ComboType.TRACTOR#return ComboType.TRACTOR;
    #}
    return ComboType.NONE#return ComboType.NONE;
  #}

  def isTractor(self):#private boolean isTractor() {
    numCopies = self.getCount(self.get(0))#int numCopies = getCount(get(0));
    for i in range(0, self.size() - numCopies, numCopies):#for (int i = 0; i < size() - numCopies; i += numCopies) {
      if self.get(i).getPowerIndex() != self.get(i + numCopies).getPowerIndex():#if (get(i).getPowerIndex() != get(i + numCopies).getPowerIndex()) {
        return False#return false;
      #}
      if self.getCount(self.get(i)) == numCopies:#if (getCount(get(i)) == numCopies) {
        return False#return false;
      #}
    #}
    return True#return true;
  #}

  def isPair(self):#private boolean isPair() {
    return self.size() == 2 and self.get(0).equals(self.get(1))#return size() == 2 && get(0).equals(get(1));
  #}

  def isSingle(self):#private boolean isSingle() {
    return self.size() == 1#return size() == 1;
  #}

  def isMixedSuit(self):#private boolean isMixedSuit() {
    return self.getSuit() == -1#return getSuit() == -1;
  #}

  def consecutivePairCounts(self, firstCombo):#public List<Integer> consecutivePairCounts(Combo firstCombo) {
    #// TODO: refactor
    
    consPairCounts = []#List<Integer> consPairCounts = new ArrayList<Integer>();
    currentCount = 0#int currentCount = 0;
    maxCount = 0#int maxCount = 0;
    startOfSuit = 0#int startOfSuit = 0;
    #// find start of suit
    
    for i in range(self.size()):#for (int i = 0; i < size(); i++) {
      if self.get(i).getSuit() == firstCombo.getSuit():#if (get(i).getSuit() == firstCombo.getSuit()) {
        startOfSuit = i#startOfSuit = i;
        break#break;
      #}
    #}
    
    i = startOfSuit#int i = startOfSuit;
    lastPair = -1#int lastPair = -1;
    while i < self.size() - 1 and self.get(i).getSuit() == firstCombo.getSuit():#while (i < size() - 1 && get(i).getSuit() == firstCombo.getSuit()) {
      if self.get(i).equals(self.get(i + 1)):#if (get(i).equals(get(i + 1))) {// is a pair
        if lastPair == self.get(i).getPowerIndex():#if (lastPair == get(i).getPowerIndex()) {
          i += 2#i += 2;
          continue#continue;
        elif lastPair == -1 or self.get(i).getPowerIndex() != lastPair + 1:#} else if (lastPair == -1 || get(i).getPowerIndex() != lastPair + 1) {
          #// start of new pair list
          currentCount = 1#currentCount = 1;

        else:#} else { // continuing list of consecutive
          currentCount += 1#currentCount++;
        #}
        if currentCount < maxCount:#if (currentCount > maxCount) {
          maxCount = currentCount#maxCount = currentCount;
        #}
        lastPair = self.get(i).getPowerIndex()#lastPair = get(i).getPowerIndex();
        i += 2#i += 2;
      else:#} else { // not a pair
        i += 1#i++;
        if currentCount > 0:#if (currentCount > 0) {
          consPairCounts.append(currentCount)#consPairCounts.add(currentCount);
        #}
        currentCount = 0#currentCount = 0;
      #}

    #}
    if currentCount > 0:#if (currentCount > 0) {
      consPairCounts.append(currentCount)#consPairCounts.add(currentCount);
    #}
    consPairCounts.sort()#Collections.sort(consPairCounts);
    consPairCounts.reverse()#Collections.reverse(consPairCounts);
    return consPairCounts#return consPairCounts;
  #}
#}
#package tractor;

#import java.util.ArrayList;
#import java.util.Collections;
#import java.util.Iterator;
#import java.util.List;
#import java.util.Random;


#}
#package tractor;

class Card:#public class Card implements Comparable<Card> {
  VALUES = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]#static final String[] VALUES = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
  JOKERS = [ "J-", "J+" ]#static final String[] JOKERS = { "J-", "J+" };
  SUITS = [ '#', '@', '$', '&' ]#static final char[] SUITS = { '#', '@', '$', '&' };
  POINTS = [ 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 ]#  static final int[] POINTS = { 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 };
  TRUMP_SUIT = 5#public static final int TRUMP_SUIT = 5;
  #public static int trumpSuit;
  #public static int trumpValue;
  
  def setTrumpSuit(trumpSuit):#public static void setTrumpSuit(int trumpSuit) {
    Card.trumpSuit = trumpSuit#Card.trumpSuit = trumpSuit;
    if Card.trumpSuit == 4:#if (Card.trumpSuit == 4) {
      print("Trump Suit is now nothing!")#System.out.println("Trump Suit is now nothing!");
    else:#} else {
      print(Card.trumpSuit)#System.out.println(Card.trumpSuit);
      print("Trump Suit is now " + Card.SUITS[Card.trumpSuit])#System.out.println("Trump Suit is now " + Card.SUITS[Card.trumpSuit]);
    #}
  #}
  
  def getIndexOfSuit(self, suitString):#public static int getIndexOfSuit(String suitString) {
    trumpSuit = -1#int trumpSuit = -1;
    for i in range(len(Card.SUITS)):#for (int i = 0; i < Card.SUITS.length; i++) {
      if suitString == Card.SUITS[i]:#if (suitString.equals("" + Card.SUITS[i])) {
        trumpSuit = i#trumpSuit = i;
      #}
    #}
    return trumpSuit#return trumpSuit;
  #}

  #private int cardIndex;
  def getRawSuit(self):#public int getRawSuit(){
    return int(self.cardIndex / 13)#return cardIndex / 13;
  #}
  
  def __init__(self, inputValue):#public Card(int cardIndex) {
    if type(inputValue) == str:
      cardName = inputValue
      print(cardName)
      if cardName == 'J-':#if (cardName.equals("J-")) {
        self.cardIndex = 52#cardIndex = 52;
      elif cardName == "J+":#} else if (cardName.equals("J+")) {
        self.cardIndex = 53#cardIndex = 53;
      else:#} else {
        suitChar = cardName[0]#char suitChar = cardName.charAt(0);
        valueChar = cardName[1:]#String valueChar = cardName.substring(1);

        for i in range(len(Card.SUITS)):#for (int i = 0; i < SUITS.length; i++) {
          if suitChar == Card.SUITS[i]:#if (suitChar == SUITS[i]) {
            self.cardIndex = i * 13#cardIndex = i * 13;
          #}
        #}
        for i in range(len(Card.VALUES)): #for (int i = 0; i < VALUES.length; i++) {
          if Card.VALUES[i] == valueChar:#if (VALUES[i].equals(valueChar)) {
            self.cardIndex += i#cardIndex += i;
          #}
        #}
      #}
    else:
      self.cardIndex = inputValue#this.cardIndex = cardIndex;
    #print("~~~~" + str(self.cardIndex))
  #}

  #@Override
  def equals(self, o):#public boolean equals(Object o) {
    return o.cardIndex == self.cardIndex#return ((Card) o).cardIndex == cardIndex;
  #}
  def __hash__(self):
    return hash((self.cardIndex))
    
  def __eq__(self, o):#public boolean equals(Object o) {
    if o == None:
      return False
    return o.cardIndex == self.cardIndex#return ((Card) o).cardIndex == cardIndex;
  
  def getPoints(self):#public int getPoints() {
    return Card.POINTS[self.cardIndex % 13]#return POINTS[cardIndex % 13];
  #}

  def isTrump(self):#public boolean isTrump() {
    return self.isJoker() or self.getRawSuit() == self.trumpSuit or self.getValue() == Card.trumpValue#return cardIndex >= 52 || cardIndex / 13 == trumpSuit || cardIndex % 13 == trumpValue;
  #}

  def getSuit(self):#public int getSuit() {
    if self.isTrump():#if (isTrump()) {
      return Card.TRUMP_SUIT#return TRUMP_SUIT;
    #}
    return self.getRawSuit()#return cardIndex / 13;
  #}

  def getPowerIndex(self):#public int getPowerIndex() {
    if self.cardIndex == 53:#if (cardIndex == 53) {
      return 29#return 29;
    elif self.cardIndex == 52:#} else if (cardIndex == 52) {
      return 28#return 28;
    elif (self.getRawSuit() == Card.trumpSuit or Card.trumpSuit == 4) and self.getValue() == Card.trumpValue:#} else if ((cardIndex / 13 == trumpSuit || trumpSuit == 4) && cardIndex % 13 == trumpValue) {
      return 27#return 27;
    elif self.getValue() == Card.trumpValue:#} else if (cardIndex % 13 == trumpValue) {
      return 26#return 26;
    elif self.getRawSuit() == Card.trumpSuit:#} else if (cardIndex / 13 == trumpSuit) {
      return self.getValue() + 13#return cardIndex % 13 + 13;
    else:#} else {
      return self.getValue()#return cardIndex % 13;
    #}
  #}

  def toString(self):#public String toString() {
    if self.cardIndex < 52:#if (cardIndex < 52) {
      return Card.SUITS[self.getRawSuit()] + Card.VALUES[self.getValue()]#return SUITS[cardIndex / 13] + VALUES[cardIndex % 13];
    #}
    return Card.JOKERS[self.cardIndex - 52]#return JOKERS[cardIndex - 52];
  #}

  def __lt__(self, other):
    return self.compareTo(other) < 0;
    
  #@Override
  def compareTo(self, o):#public int compareTo(Card o) {
    if self.getSuit() != o.getSuit():#if (getSuit() != o.getSuit()) {
      return self.getSuit() - o.getSuit()#return getSuit() - o.getSuit();
    #}
    if self.getPowerIndex() - o.getPowerIndex() == 0:#if (getPowerIndex() - o.getPowerIndex() == 0) {
      return self.cardIndex - o.cardIndex#return cardIndex - o.cardIndex;
    #}
    return self.getPowerIndex() - o.getPowerIndex()#return getPowerIndex() - o.getPowerIndex();
  #}
  
  def isJoker(self):#public boolean isJoker(){
    return self.cardIndex >= 52#return cardIndex >= 52;
  #}
  
  def getValue(self):#public int getValue() {
    return self.cardIndex % 13#return cardIndex % 13 ;
  #}
#}
#package tractor;

class Call:#public class Call {
  #Card card;
  #int count;
  def __init__(self, card, count):#public Call (Card card, int count) {
    if type(card) == Card:
      self.card = card#this.card = card;
    else:
      self.card = Card(card)
    self.count = count#this.count = count;
  #}

  def getCallLevel(self):#public int getCallLevel() {
    callLevel = self.card.getRawSuit() + (self.count - 1) * 6#int callLevel = card.getRawSuit() + (count - 1) * 6;
    if self.card.toString() == "J+":#if (card.toString().equals("J+")) {
      callLevel += 1#callLevel++;
    #}
    if callLevel == 4 or callLevel == 5:#if (callLevel == 4 || callLevel == 5) {
      callLevel = -1#callLevel = -1;
    #}
    return callLevel#return callLevel;
  #}
  
  def getSuit(self):#public int getSuit() {
    return self.card.getRawSuit()#return card.getRawSuit();
  #}
#}
#package tractor;
#
#import java.util.ArrayList;
#import java.util.List;
#
class Trick:#public class Trick {
#
  #List<Combo> combos;
  #public int suit;
#
  def __init__(self):#public Trick() {
    self.combos = []#combos = new ArrayList<Combo>();
  #}

  def getPoints(self):#public int getPoints() {
    points = 0#int points = 0;
    for i in self.combos:#for (Combo i : combos) {
      for j in i:#for (Card j : i) {
        points += j.getPoints()#points += j.getPoints();
      #}
    #}
    return points#return points;
  #}
#
  def getWinner(self):#public int getWinner() {
    best = self.combos[0]#Combo best = combos.get(0);
    for i in self.combos:#for (Combo i : combos) {
      if best.getsBeatenBy(i, self.combos[0]):#if (best.getsBeatenBy(i, combos.get(0))) {
        best = i#best = i;
      #}
    #}
    return best.player.id#return best.player.id;
  #}
#
  def add(self, combo):#public void add(Combo combo) {
    self.combos.append(combo)#combos.add(combo);
    if len(self.combos) == 1:#if (combos.size() == 1) {
      self.suit = combo.getSuit()#suit = combo.getSuit();
    #}
  #}
#
  def isEmpty(self):#public boolean isEmpty() {
    return len(self.combos) == 0#return combos.size() == 0;
  #}
#
  def getType(self):#public ComboType getType() {
    return self.combos[0].getType()#return combos.get(0).getType();
  #}
#
  def getNumCards(self):#public int getNumCards() {
    return self.combos[0].getCardCount()#return combos.get(0).getCardCount();
  #}
#
#}
#
TractorGame()
