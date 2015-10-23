package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Combo extends SortedCardCollection {
	Player player;

	public Combo(Player player, CardCollection cardsPlayed) {
		super();
		addCards(cardsPlayed);
		this.player = player;
	}

	public boolean isSameSuit() {
		int suit = -1;
		for (Card i : this) {
			if (suit == -1) {
				suit = i.getSuit();
			}
			if (suit != i.getSuit()) {
				return false;
			}
		}
		return true;
	}

	public int getSuit() {
		if (isSameSuit()) {
			return cards.get(0).getSuit();
		}
		return -1;
	}

	public boolean getsBeatenBy(Combo challenger, Combo first) {
		return getPower(first) < challenger.getPower(first);
	}

	public int getPower(Combo first) {
		if (getType() == ComboType.NONE || getType() != first.getType()) {
			return 0;
		}
		if (getSuit() != first.getSuit() && getSuit() != Card.TRUMP_SUIT) {
			return 0;
		}

		int power = get(0).getPowerIndex();
		return power;
	}

	public ComboType getType() {
		if (isMixedSuit()) {
			return ComboType.NONE;
		} else if (isSingle()) {
			return ComboType.SINGLE;
		} else if (isPair()) {
			return ComboType.PAIR;
		} else if (isTractor()) {
			return ComboType.TRACTOR;
		}
		return ComboType.NONE;
	}

	private boolean isTractor() {
		int numCopies = getCount(get(0));
		for (int i = 0; i < size() - numCopies; i += numCopies) {
			if (get(i).getPowerIndex() != get(i + numCopies).getPowerIndex()) {
				return false;
			}
			if (getCount(get(i)) == numCopies) {
				return false;
			}
		}
		return true;
	}

	private boolean isPair() {
		return size() == 2 && get(0).equals(get(1));
	}

	private boolean isSingle() {
		return size() == 1;
	}

	private boolean isMixedSuit() {
		return getSuit() == -1;
	}

	public List<Integer> consecutivePairCounts(Combo firstCombo) {
		// TODO: refactor
		List<Integer> consPairCounts = new ArrayList<Integer>();
		int currentCount = 0;
		int maxCount = 0;
		int startOfSuit = 0;
		// find start of suit
		for (int i = 0; i < size(); i++) {
			if (get(i).getSuit() == firstCombo.getSuit()) {
				startOfSuit = i;
				break;
			}
		}
		int i = startOfSuit;
		int lastPair = -1;
		while (i < size() - 1 && get(i).getSuit() == firstCombo.getSuit()) {
			if (get(i).equals(get(i + 1))) {// is a pair
				if (lastPair == get(i).getPowerIndex()) {
					i += 2;
					continue;
				} else if (lastPair == -1 || get(i).getPowerIndex() != lastPair + 1) {
					// start of new pair list
					currentCount = 1;

				} else { // continuing list of consecutive
					currentCount++;
				}
				if (currentCount > maxCount) {
					maxCount = currentCount;
				}
				lastPair = get(i).getPowerIndex();
				i += 2;
			} else { // not a pair
				i++;
				if (currentCount > 0) {
					consPairCounts.add(currentCount);
				}
				currentCount = 0;
			}

		}
		if (currentCount > 0) {
			consPairCounts.add(currentCount);
		}
		Collections.sort(consPairCounts);
		Collections.reverse(consPairCounts);
		return consPairCounts;
	}
}
