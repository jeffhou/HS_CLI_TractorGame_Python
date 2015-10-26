#package tractor;

class Call:#public class Call {
  #Card card;
  #int count;
  def __init__(self, card, count):#public Call (Card card, int count) {
    if type(card) == Card:
      this.card = card#this.card = card;
    else:
      this.card = Card(card)
    this.count = count#this.count = count;
  #}

  def getCallLevel(self):#public int getCallLevel() {
    callLevel = self.card.getRawSuit() + (count - 1) * 6#int callLevel = card.getRawSuit() + (count - 1) * 6;
    if card.toString() == "J+":#if (card.toString().equals("J+")) {
      callLevel += 1#callLevel++;
    #}
    if callLevel == 4 or callLevel == 5:#if (callLevel == 4 || callLevel == 5) {
      callLevel = -1#callLevel = -1;
    #}
    return callLevel#return callLevel;
  #}
  
  def getSuit(self):#public int getSuit() {
    return card.getRawSuit()#return card.getRawSuit();
  #}
#}
