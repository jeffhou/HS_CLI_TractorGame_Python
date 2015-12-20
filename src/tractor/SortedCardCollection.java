package tractor;

import java.util.ArrayList;
import java.util.List;

public class SortedCardCollection extends CardCollection {
	public void addCard(Card card) {
		super.addCard(card);
		sort();
	}

	public void addCards(CardCollection cc) {
		super.addCards(cc);
		sort();
	}

	public boolean isSubSet(SortedCardCollection o) {
		List<Card> sortedSubList = new ArrayList<Card>(cards);
		List<Card> sortedSuperList = new ArrayList<Card>(o.cards);

		int j = 0;
		for (int i = 0; i < sortedSubList.size(); i++) {
			boolean notSubset = false;
			while (true) {

				if (sortedSubList.get(i).equals(sortedSuperList.get(j))) {
					j++;
					break;
				}
				j++;
				if (j >= sortedSuperList.size()) {
					notSubset = true;
					break;
				}
			}
			if (notSubset || j == sortedSuperList.size()) {
				return false;
			}
		}
		return true;
	}
}
