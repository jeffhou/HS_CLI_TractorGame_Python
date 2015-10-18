package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Combo {
	Player player;
	List<Card> cards;

	public Combo(Player player, List<Card> cardsPlayed) {
		this.player = player;
		this.cards = new ArrayList<Card>(cardsPlayed);
	}

	public int getSuit() {
		int suit = -1;
		for (Card i : cards) {
			if (suit == -1) {
				suit = i.getSuit();
			}
			if (suit != i.getSuit()) {
				return -1;
			}
		}
		if (Card.trumpSuit == suit) {
			return Card.TRUMP_SUIT;
		}
		return suit;
	}

	public boolean getsBeatenBy(Combo challenger, Combo first) {
		return getPower(first) < challenger.getPower(first);
	}

	public int getPower(Combo first) {
		/*
		 * assumption: 1. cards are already sorted correctly (sequential cards
		 * are next to each other) 2. cards have the same length as first.cards
		 * 3. cards are already valid and playable
		 */
		/*
		 * returns 0 if it's not going to beat the first combo
		 */
		if (getType() == ComboType.NONE) {
			//not a combo
			return 0;
		}
		// check all are the same suit
		if (getSuit() == -1) {
			return 0;
		}

		// check if suit is same suit as first or trump
		if (getSuit() != first.getSuit() && getSuit() != Card.TRUMP_SUIT) {
			return 0;
		}

		// check to see if combination is a valid type (single, double, tractor)
		if (isType(first.getType())) {
			int power = cards.get(0).getPowerIndex();
			if (getSuit() == Card.TRUMP_SUIT) {
				power += 100;
			}
			return power;
		}

		return 0;
	}

	private boolean isType(ComboType type) {
		return getType() == type;
	}

	public ComboType getType() {
		// assumes size > 0
		// assumes 2 decks
		// TODO implement for +2 decks
		if (getSuit() == -1) {
			return ComboType.NONE;
		} else if (cards.size() == 1) {
			return ComboType.SINGLE;
		} else if (cards.size() == 2) {
			if (cards.get(0).equals(cards.get(1))) {
				return ComboType.PAIR;
			}
		} else if (cards.size() % 2 == 0) {
			for (int i = 0; i < cards.size(); i += 2) {
				if (!cards.get(i).equals(cards.get(i + 1))) {
					return ComboType.NONE;
				}
				try {
					if (cards.get(i).getPowerIndex() != cards.get(i + 2).getPowerIndex() - 1) {
						return ComboType.NONE;
					}
				} catch (IndexOutOfBoundsException e) {

				}
			}
			return ComboType.TRACTOR;
		}
		return ComboType.NONE;
	}
public List<Integer> consecutivePairCounts(Combo firstCombo){
		
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
	public int countSuit(int suit) {
		int count = 0;
		for (Card i: cards) {
			if (i.getSuit() == suit) {
				count++;
			}
		}
		return count;
	}

	public int getNumCards() {
		return cards.size();
	}

}
