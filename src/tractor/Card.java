package tractor;

public class Card implements Comparable<Card> {
	static final String[] NORMAL_VALUES = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
	static final String[] JOKERS = { "J-", "J+" };
//	static final String[] SUITS = { "¶", "®", "§", "Ø" };
	static final String[] SUITS = { "#", "@", "$", "&" };
	static final int[] POINTS = { 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 };
	public static final int TRUMP_SUIT = 5;
	public static int trumpSuit;
	public static int trumpValue;
	int cardIndex;

	public Card(int cardIndex) {
		this.cardIndex = cardIndex;
	}

	public Card(String cardName) {
		// System.out.println("Card Name: "+cardName);
		String tempString;
		for (int i = 0; i < 54; i++) {
			if (i < 52) {
				tempString = SUITS[i / 13] + NORMAL_VALUES[i % 13];
			} else {
				tempString = JOKERS[i - 52];
			}
			if (cardName.equals(tempString)) {
				cardIndex = i;
				break;
			}
		}
		// System.out.println("Card Index: "+cardIndex);
	}

	@Override
	public boolean equals(Object o) {
		return ((Card) o).cardIndex == cardIndex;
	}

	public int getPoints() {
		return POINTS[cardIndex % 13];
	}

	public int getSuit() {
		if (cardIndex >= 52 || cardIndex / 13 == trumpSuit || cardIndex % 13 == trumpValue) {
			return TRUMP_SUIT;
		}
		return cardIndex / 13;
	}

	public int getPowerIndex() {
		if (cardIndex == 53) {
			return 29;
		} else if (cardIndex == 52) {
			return 28;
		} else if ((cardIndex / 13 == trumpSuit || trumpSuit == 4) && cardIndex % 13 == trumpValue) {
			return 27;
		} else if (cardIndex % 13 == trumpValue) {
			return 26;
		} else if (cardIndex / 13 == trumpSuit) {
			return cardIndex % 13 + 13;
		} else {
			return cardIndex % 13;
		}
	}

	public String toString() {
		if (cardIndex < 52) {
			return SUITS[cardIndex / 13] + NORMAL_VALUES[cardIndex % 13];
		}
		return JOKERS[cardIndex - 52];
	}

	@Override
	public int compareTo(Card o) {
		if (getSuit() != o.getSuit()) {
			return getSuit() - o.getSuit();
		}
		if (getPowerIndex() - o.getPowerIndex() == 0) {
			return cardIndex - o.cardIndex;
		}
		return getPowerIndex() - o.getPowerIndex();
	}
}
