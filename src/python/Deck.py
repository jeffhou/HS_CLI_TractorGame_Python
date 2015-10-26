#package tractor;

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
