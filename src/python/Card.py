#package tractor;

class Card:#public class Card implements Comparable<Card> {
  VALUES = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]#static final String[] VALUES = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
  JOKERS = [ "J-", "J+" ]#static final String[] JOKERS = { "J-", "J+" };
  SUITS = [ '#', '@', '$', '&' ]#static final char[] SUITS = { '#', '@', '$', '&' };
  POINTS = [ 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 ]#  static final int[] POINTS = { 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 };
  TRUMP_SUIT = 5#public static final int TRUMP_SUIT = 5;
  #public static int trumpSuit;
  #public static int trumpValue;
  
  def setTrumpSuit(self, trumpSuit):#public static void setTrumpSuit(int trumpSuit) {
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
      if cardName == 'J-':#if (cardName.equals("J-")) {
        self.cardIndex = 52#cardIndex = 52;
      elif cardName == "J+":#} else if (cardName.equals("J+")) {
        self.cardIndex = 53#cardIndex = 53;
      else:#} else {
        suitChar = cardName[0]#char suitChar = cardName.charAt(0);
        valueChar = cardName[1:]#String valueChar = cardName.substring(1);

        for i in range(len(Card.SUITS)):#for (int i = 0; i < SUITS.length; i++) {
          if suitChar == SUITS[i]:#if (suitChar == SUITS[i]) {
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
  #}

  #@Override
  def equals(self, o):#public boolean equals(Object o) {
    return o.cardIndex == self.cardIndex#return ((Card) o).cardIndex == cardIndex;
  #}

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
    return self.getRawSuit#return cardIndex / 13;
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
      return Card.SUITS[self.getRawSuit] + Card.VALUES[self.getValue]#return SUITS[cardIndex / 13] + VALUES[cardIndex % 13];
    #}
    return Card.JOKERS[self.cardIndex - 52]#return JOKERS[cardIndex - 52];
  #}

  def __lt__(self, other):
    return this.compareTo(other) < 0;
    
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
