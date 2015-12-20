package tractor;

import java.util.ArrayList;
import java.util.List;

public class Trick {

	List<Combo> combos;
	public int suit;

	public Trick() {
		combos = new ArrayList<Combo>();
	}

	public int getPoints() {
		int points = 0;
		for (Combo i : combos) {
			for (Card j : i) {
				points += j.getPoints();
			}
		}
		return points;
	}

	public int getWinner() {
		Combo best = combos.get(0);
		for (Combo i : combos) {
			if (best.getsBeatenBy(i, combos.get(0))) {
				best = i;
			}
		}
		return best.player.id;
	}

	public void add(Combo combo) {
		combos.add(combo);
		if (combos.size() == 1) {
			suit = combo.getSuit();
		}
	}

	public boolean isEmpty() {
		return combos.size() == 0;
	}

	public ComboType getType() {
		return combos.get(0).getType();
	}

	public int getNumCards() {
		return combos.get(0).getCardCount();
	}

}
