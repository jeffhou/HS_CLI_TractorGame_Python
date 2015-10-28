from CardCollection import CardCollection
from Card import Card
class Deck (CardCollection):  

  DECK_SIZE = 54
  
  def __init__(self, numDecks):
    super().__init__()
    self.addDecks(numDecks)
    self.shuffle()

  def addDeck(self):
    for i in range(self.DECK_SIZE): 
      self.addCard(Card(i))

  def addDecks(self, numDecks):
    for i in range(numDecks):
      self.addDeck()

  def draw(self): 
    return self.remove(0)
