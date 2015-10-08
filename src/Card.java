
public class Card {
	
	static final String[] NORMAL_VALUES = {"Two", "Three", "Four", "Five","Six",
			"Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"};
	static final String[] JOKERS = {"Small Joker", "Big Joker"};
	static final String[] SUIT_NAMES = {"Spades", "Hearts", "Clubs", "Diamonds"};
	
	int valueIndex, suitIndex;
	
	public Card (int cardID) {
		suitIndex = cardID / 13;
		valueIndex = cardID % 13;
	}
	
	public String toString() {
		if (suitIndex == 4) {
			return JOKERS[valueIndex];
		} else {
			return NORMAL_VALUES[valueIndex] + " of " + SUIT_NAMES[suitIndex];
		}
	}
}
