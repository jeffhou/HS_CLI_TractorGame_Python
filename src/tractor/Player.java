package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Player {
	List<Card> cards;
	int id;
	int level;

	public Player(int i) {
		cards = new ArrayList<Card>();
		id = i;
		level = 0;
	}

	public void addCard(Card card) {
		cards.add(card);
		Collections.sort(cards);
	}

	public boolean hasCards() {
		return cards.size() > 0;
	}

	public void removeCards(List<Card> cardsPlayed) {
		for (Card i : cardsPlayed) {
			cards.remove(i);
		}
	}

	public void levelUp(int level) {
		this.level += level;
	}

	public int countSuit(int suit) {
		int count = 0;
		for (Card i : cards) {
			if (i.getSuit() == suit) {
				count++;
			}
		}
		return count;
	}

	public boolean hasComboToPlay(Combo firstCombo) {
		// has to be pair or tractor
		// the hard part is that tractors have multiple
		// easiest is to find biggest number of consecutive pairs in the suit
		// TODO make sure everything works with SHUAI
		int currentCount = 0;
		int maxCount = 0;
		int startOfSuit = 0;
		// find start of suit
		for (int i = 0; i < cards.size(); i++) {
			if (cards.get(i).getSuit() == firstCombo.getSuit()) {
				startOfSuit = i;
				break;
			}
		}
		int i = startOfSuit;
		int lastPair = -1;
		while (i < cards.size() - 1 && cards.get(i).getSuit() == firstCombo.getSuit()) {
			if (cards.get(i).equals(cards.get(i + 1))) {// is a pair
				if (lastPair == cards.get(i).getPowerIndex()) {
					i += 2;
					continue;
				} else if (lastPair == -1 || cards.get(i).getPowerIndex() != lastPair + 1) {
					// start of new pair list
					currentCount = 1;

				} else { // continuing list of consecutive
					currentCount++;
				}
				if (currentCount > maxCount) {
					maxCount = currentCount;
				}
				lastPair = cards.get(i).getPowerIndex();
				i += 2;
			} else { // not a pair
				i++;
			}
		}
		if (maxCount * 2 >= firstCombo.cards.size()) {
			return true;
		}
		return false;
	}

	public boolean playedRequired(Combo firstCombo, Combo attemptedCombo) {
		List<Integer> handConsecutivePairCounts = consecutivePairCounts(firstCombo);
		List<Integer> comboConsecutivePairCounts = attemptedCombo.consecutivePairCounts(firstCombo);
		int numberOfCardsNeeded = firstCombo.cards.size();
		int i = 0;
		while (numberOfCardsNeeded != 0 && i < handConsecutivePairCounts.size()) {
			if (i >= comboConsecutivePairCounts.size()) {
				return false;
			}
			if (handConsecutivePairCounts.get(i) * 2 <= numberOfCardsNeeded) {
				if (comboConsecutivePairCounts.get(i) != handConsecutivePairCounts.get(i)) {
					return false;
				}
				numberOfCardsNeeded -= handConsecutivePairCounts.get(i);
			} else {
				if (comboConsecutivePairCounts.get(i) != numberOfCardsNeeded) {
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

		List<Integer> consecutivePairCounts = new ArrayList<Integer>();
		int currentCount = 0;
		int maxCount = 0;
		int startOfSuit = 0;
		// find start of suit
		for (int i = 0; i < cards.size(); i++) {
			if (cards.get(i).getSuit() == firstCombo.getSuit()) {
				startOfSuit = i;
				break;
			}
		}
		int i = startOfSuit;
		int lastPair = -1;
		while (i < cards.size() - 1 && cards.get(i).getSuit() == firstCombo.getSuit()) {
			if (cards.get(i).equals(cards.get(i + 1))) {// is a pair
				if (lastPair == cards.get(i).getPowerIndex()) {
					i += 2;
					continue;
				} else if (lastPair == -1 || cards.get(i).getPowerIndex() != lastPair + 1) {
					// start of new pair list
					currentCount = 1;

				} else { // continuing list of consecutive
					currentCount++;
				}
				if (currentCount > maxCount) {
					maxCount = currentCount;
				}
				lastPair = cards.get(i).getPowerIndex();
				i += 2;
			} else { // not a pair
				i++;
				if (currentCount > 0) {
					consecutivePairCounts.add(currentCount);
				}
				currentCount = 0;
			}

		}
		if (currentCount > 0) {
			consecutivePairCounts.add(currentCount);
		}
		Collections.sort(consecutivePairCounts);
		Collections.reverse(consecutivePairCounts);
		return consecutivePairCounts;
	}

	public boolean canOverride(Player player, int newCallLevel) {
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
			if (numCards == 1) {
				return false;
			}
		} else {
			toCheck = new Card(Card.SUITS[suit] + Card.NORMAL_VALUES[Card.trumpValue]);
		}
		for (Card i : cards) {
			if (i.equals(toCheck)) {
				numCards--;
			}
		}
		return numCards <= 0;
	}

}
