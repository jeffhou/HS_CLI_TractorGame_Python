package tractor;

public class Card implements Comparable<Card> {
	static final String[] NORMAL_VALUES = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
	static final String[] JOKERS = { "J-", "J+" };
	static final char[] SUITS = { '#', '@', '$', '&' };
	static final int[] POINTS = { 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 10, 0 };
	public static final int TRUMP_SUIT = 5;
	public static int trumpSuit;
	public static int trumpValue;

	int cardIndex;

	public Card(int cardIndex) {
		this.cardIndex = cardIndex;
	}

	public Card(String cardName) {
		if (cardName.equals("J-")) {
			cardIndex = 52;
		} else if (cardName.equals("J+")) {
			cardIndex = 53;
		} else {
			char suitChar = cardName.charAt(0);
			String valueChar = cardName.substring(1);

			for (int i = 0; i < SUITS.length; i++) {
				if (suitChar == SUITS[i]) {
					cardIndex = i * 13;
				}
			}
			for (int i = 0; i < NORMAL_VALUES.length; i++) {
				if (NORMAL_VALUES[i].equals(valueChar)) {
					cardIndex += i;
				}
			}
		}
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
