package tractor;

import java.util.ArrayList;
import java.util.List;

public class Trick {
	
	List<Combo> combosPlayed;
	public int suit;
	public Trick() {
		combosPlayed = new ArrayList<Combo>();
	}
	public int getPoints() {
		int points = 0;
		for (Combo i: combosPlayed){
			for (Card j: i.cards) {
				points += j.getPoints();
			}
		}
		return points;
	}
	public int getWinner() {
		Combo winningCombo = combosPlayed.get(0);
		for (Combo i: combosPlayed) {
			if(winningCombo.getsBeatenBy(i, combosPlayed.get(0))){
				winningCombo = i;
			}
		}
		return winningCombo.player.id;
	}
	public void add(Combo combo) {
		combosPlayed.add(combo);
		if (combosPlayed.size() == 1) {
			suit = combo.getSuit();
		}
	}
	public boolean isEmpty() {
		return combosPlayed.size() == 0;
	}
	public ComboType getType() {
		return combosPlayed.get(0).getType();
	}
	public int getNumCards() {
		return combosPlayed.get(0).getNumCards();
	}

}
