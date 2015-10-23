package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Player extends SortedCardCollection {
	int id, level;

	public Player(int i) {
		super();
		id = i;
		level = 0;
	}

	public void levelUp(int level) {
		this.level += level;
	}

	public boolean hasComboToPlay(Combo firstCombo) {
		// TODO: refactor
		// has to be pair or tractor
		// the hard part is that tractors have multiple
		// easiest is to find biggest number of consecutive pairs in the suit
		// TODO make sure everything works with SHUAI
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
			}
		}
		if (maxCount * 2 >= firstCombo.size()) {
			return true;
		}
		return false;
	}

	public boolean playedRequired(Combo firstCombo, Combo attemptedCombo) {
		// TODO: refactor
		List<Integer> handConsecPairCounts = consecutivePairCounts(firstCombo);
		List<Integer> comboConsecPairCounts = attemptedCombo.consecutivePairCounts(firstCombo);
		int numberOfCardsNeeded = firstCombo.size();
		int i = 0;
		while (numberOfCardsNeeded != 0 && i < handConsecPairCounts.size()) {
			if (i >= comboConsecPairCounts.size()) {
				return false;
			}
			if (handConsecPairCounts.get(i) * 2 <= numberOfCardsNeeded) {
				if (comboConsecPairCounts.get(i) != handConsecPairCounts.get(i)) {
					return false;
				}
				numberOfCardsNeeded -= handConsecPairCounts.get(i);
			} else {
				if (comboConsecPairCounts.get(i) != numberOfCardsNeeded) {
					return false;
				} else {
					return true;
				}
			}
			i++;
		}
		return true;
	}

	public List<Integer> consecutivePairCounts(Combo firstCombo) {
		// TODO: refactor
		List<Integer> consecPairCounts = new ArrayList<Integer>();
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
					consecPairCounts.add(currentCount);
				}
				currentCount = 0;
			}

		}
		if (currentCount > 0) {
			consecPairCounts.add(currentCount);
		}
		Collections.sort(consecPairCounts);
		Collections.reverse(consecPairCounts);
		return consecPairCounts;
	}

	public boolean canOverride(Player player, int newCallLevel) {
		// TODO: refactor
		int numCards = newCallLevel / 6 + 1;
		int suit = newCallLevel % 6;
		Card toCheck = null;
		if (suit == 5) {
			toCheck = new Card("J+");
			if (numCards == 1) {
				return false;
			}
		} else if (suit == 4) {
			toCheck = new Card("J-");
			System.out.println("blah!");
			if (numCards == 1) {
				return false;
			}
		} else {
			toCheck = new Card(Card.SUITS[suit] + Card.VALUES[Card.trumpValue]);
		}
		for (Card i : this) {
			if (i.equals(toCheck)) {
				numCards--;
			}
		}
		return numCards <= 0;
	}

	public boolean has(Card card, int numCards) {
		return getCount(card) >= numCards;
	}

}
