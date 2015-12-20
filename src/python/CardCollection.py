import random
from TestingSuite import TESTING

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
    return sum(c == card for card in self.cards)

  def getCardCount(self):
    return len(self.cards)

  def isEmpty(self):
    return len(self.cards) == 0

  def remove(self, i):
    if type(i) != int:
      return self.cards.remove(i)
    else:
      return self.cards.pop(i)

  def removeAll(self):
    self.cards.clear()

  def removeCards(self, cards):
    for i in cards.cards:
      self.cards.remove(i)
      
  def shuffle(self):
    if TESTING:
      random.seed(0)
    else:
      random.seed()
    random.shuffle(self.cards)

  def size(self):
    return len(self.cards)
    
  def sort(self): 
    self.cards.sort()