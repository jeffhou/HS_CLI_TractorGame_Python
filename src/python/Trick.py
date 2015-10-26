#package tractor;
#
#import java.util.ArrayList;
#import java.util.List;
#
class Trick:#public class Trick {
#
  #List<Combo> combos;
  #public int suit;
#
  def __init__(self):#public Trick() {
    self.combos = []#combos = new ArrayList<Combo>();
  #}

  def getPoints(self):#public int getPoints() {
    points = 0#int points = 0;
    for i in self.combos:#for (Combo i : combos) {
      for j in i:#for (Card j : i) {
        points += j.getPoints()#points += j.getPoints();
      #}
    #}
    return points#return points;
  #}
#
  def getWinner(self):#public int getWinner() {
    best = self.combos[0]#Combo best = combos.get(0);
    for i in self.combos:#for (Combo i : combos) {
      if best.getsBeatenBy(i, self.combos.[0]):#if (best.getsBeatenBy(i, combos.get(0))) {
        best = i#best = i;
      #}
    #}
    return best.player.id#return best.player.id;
  #}
#
  def add(self, combo):#public void add(Combo combo) {
    self.combos.append(combo)#combos.add(combo);
    if len(self.combos) == 1:#if (combos.size() == 1) {
      self.suit = combo.getSuit()#suit = combo.getSuit();
    #}
  #}
#
  def isEmpty(self):#public boolean isEmpty() {
    return len(self.combos) == 0#return combos.size() == 0;
  #}
#
  def getType(self):#public ComboType getType() {
    return self.combos[0].getType()#return combos.get(0).getType();
  #}
#
  def getNumCards(self):#public int getNumCards() {
    return self.combos[0].getCardCount()#return combos.get(0).getCardCount();
  #}
#
#}
#