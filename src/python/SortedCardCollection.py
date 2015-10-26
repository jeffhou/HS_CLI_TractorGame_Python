#package tractor;

#import java.util.ArrayList;
#import java.util.List;

class SortedCardCollection(CardCollection):#public class SortedCardCollection extends CardCollection {

  def __init__(self):
    super().__init__()
  
  def addCard(self, card):#public void addCard(Card card) {
    super().addCard(card)#super.addCard(card);
    self.sort()#sort();
  #}
#
  def addCards(cc):#public void addCards(CardCollection cc) {
    super().addCards(cc)#super.addCards(cc);
    self.sort()#sort();
  #}

  def copyCardsList(self, cardsList):
    cards = []
    for i in cardsList:
      cards.append(Card(i.toString()))
    return cards
    
  def isSubSet(self, o):#public boolean isSubSet(SortedCardCollection o) {
    sortedSubList = this.copyCardsList(cards)#List<Card> sortedSubList = new ArrayList<Card>(cards);
    sortedSuperList = this.copyCardsList(o.cards)#List<Card> sortedSuperList = new ArrayList<Card>(o.cards);
#
    j = 0#int j = 0;
    for i in range(len(sortedSubList)):#for (int i = 0; i < sortedSubList.size(); i++) {
      notSubset = False#boolean notSubset = false;
      while True:#while (true) {
#
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
        return False#return false;
      #}
    #}
    return True#return true;
  #}
#}
