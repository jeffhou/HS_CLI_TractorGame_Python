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

  def getPower(first):#public int getPower(Combo first) {
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
