#package tractor;
#
#import java.util.ArrayList;
#import java.util.Collections;
#import java.util.List;
class Player(SortedCardCollection):#public class Player extends SortedCardCollection {
  #int id, level;
  def __init__(self, i):#public Player(int i) {
    super()#super();
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
#