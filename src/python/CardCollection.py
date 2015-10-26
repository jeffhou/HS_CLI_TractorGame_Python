#package tractor;

#import java.util.ArrayList;
#import java.util.Collections;
#import java.util.Iterator;
#import java.util.List;
#import java.util.Random;

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
    for i in self.cards:#for (Card i : cards) {
      self.cards.remove(i)#this.cards.remove(i);
    #}
  #}

  def shuffle(self):#public void shuffle() {
    seed = 0 if Tractor.TESTING else random.seed()#long seed = TractorGame.TESTING ? 1445123063075L : System.currentTimeMillis();
    random.shuffle(self.cards)#Collections.shuffle(cards, new Random(seed));
  #}

  def size(self):#public int size() {
    return len(self.cards)#return cards.size();
  #}
    
  def sort(self): #public void sort() {
    self.cards.sort()#Collections.sort(cards);
  #}
#}
