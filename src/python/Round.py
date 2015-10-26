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
    Card.trumpValue = TractorGame.players[boss].level#Card.trumpValue = TractorGame.players[boss].level;
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
        if not selector.isJoker():#if (!selector.isJoker()) {
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
    call = Call(trumpInput[1], int(trumpInput[:1]))#Call call = new Call(trumpInput.substring(1), Integer.parseInt(trumpInput.substring(0, 1)));
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
    while len(self.mainDeck) > Round.NUM_LEFTOVER:#while (mainDeck.size() > NUM_LEFTOVER) {
      for i in range(Round.NUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
        newCard = self.mainDeck.draw()#Card newCard = mainDeck.draw();
        TractorGame.players[i].addCard(newCard)#TractorGame.players[i].addCard(newCard);
        if Card.trumpSuit == 4:#if (Card.trumpSuit == 4) {
          print("\n=== HAND (!" + Card.VALUES[TractorGame.players[self.boss].level] + ")===")
        elif Card.trumpSuit != -1:#} else if (Card.trumpSuit != -1) {
          print("\n=== HAND (" + Card.SUITS[Card.trumpSuit]  + Card.VALUES[TractorGame.players[boss].level] + ")===")
        else:
          print("\n=== HAND (~" + Card.VALUES[TractorGame.players[boss].level] + ")===")

        self.updateDisplay(TractorGame.players[i])#updateDisplay(TractorGame.players[i]);
        if True:#if (true) {
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
    for i in cards:#for (Card i : cards) {
      print(i.toString(), end="")#System.out.print(i + " ");
    #}
    inputString = self.getUserInput("")#String inputString = getUserInput("");
    if inputString == "":#if (inputString.equals(""))
      return#return;
    cardStrings = inputString.split(" ")#String[] cardStrings = inputString.split(" ");
    for i in cardStrings:#for (String i : cardStrings) {
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
      print("Player " + str(i.id) + ": " + str(playerPoints[i.id]) + " points")#System.out.println("Player " + i.id + ": " + playerPoints[i.id] + " points");
    #}
#
    for i in range(Round.NUM_PLAYERS):#for (int i = 0; i < NUM_PLAYERS; i++) {
      #int playerID;
      if len(self.tricks) == 0:#if (tricks.size() == 0) {
        playerID = self.boss#playerID = boss;
      else:#}else{
        playerID = (i + self.tricks[len(self.tricks) - 1].getWinner()) % Round.NUM_PLAYERS#playerID = (i + tricks.get(tricks.size() - 1).getWinner()) % NUM_PLAYERS;
      #}
#
      self.updateDisplay(TractorGame.players[playerID])#updateDisplay(TractorGame.players[playerID]);
      self.playCards(TractorGame.players[playerID], currentTrick)#playCards(TractorGame.players[playerID], currentTrick);
    #}
    self.updatePoints(currentTrick.getWinner(), currentTrick.getPoints())#updatePoints(currentTrick.getWinner(), currentTrick.getPoints());
    println("Player " + str(currentTrick.getWinner()) + " wins trick and earns " + str(currentTrick.getPoints())#System.out.println("Player " + currentTrick.getWinner() + " wins trick and earns " + currentTrick.getPoints()
        + " points!")#+ " points!");
    return currentTrick#return currentTrick;
  #}
#
  def playCards(self, player, numCards, c):#private Card[] playCards(Player player, int numCards, ComboType c) {
    cardsPlayed = SortedCardCollection()#SortedCardCollection cardsPlayed = new SortedCardCollection();
    while cardsPlayed.size() != numCards:#while (cardsPlayed.size() != numCards) {
      if not cardsPlayed.isSubSet(player) or cardsPlayed.size() > 8:#if (!cardsPlayed.isSubSet(player) || cardsPlayed.size() > 8) {
        cardsPlayed.removeAll()#cardsPlayed.removeAll();
      #}
      self.inputCardsPlayed(cardsPlayed, player)#inputCardsPlayed(cardsPlayed, player);
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
      combo = Combo(player, cardsPlayed)#combo = new Combo(player, cardsPlayed);
      valid = self.validateCardsPlayed(combo, currentTrick, player)#valid = validateCardsPlayed(combo, currentTrick, player);
      if not valid:#if (!valid) {
        self.display("Invalid!")#display("Invalid!");
        cardsPlayed.removeAll()#cardsPlayed.removeAll();
      #}
#
    #}
    currentTrick.add(combo)#currentTrick.add(combo);
    player.removeCards(cardsPlayed)#player.removeCards(cardsPlayed);
  #}
#
  def populateTricks(self):#private void populateTricks() {
    while not TractorGame.players[0].isEmpty():#while (!TractorGame.players[0].isEmpty()) {
      self.tricks.add(self.nextTrick())#tricks.add(nextTrick());
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
    

    while not mainDeck.isEmpty():#while (!mainDeck.isEmpty()) {
      TractorGame.players[self.boss].addCard(self.mainDeck.draw())#TractorGame.players[boss].addCard(mainDeck.draw());
    #}
    self.updateDisplay(TractorGame.players[self.boss])#updateDisplay(TractorGame.players[boss]);
#
    for i in self.playCards(TractorGame.players[self.boss], 8, ComboType.NONE):#for (Card i : playCards(TractorGame.players[boss], 8, ComboType.NONE)) {
      self.mainDeck.addCard(i)#mainDeck.addCard(i);
      TractorGame.players[self.boss].remove(i)#TractorGame.players[boss].remove(i);
    #}
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
#