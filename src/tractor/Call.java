package tractor;

public class Call {
	Card card;
	int count;
	public Call (Card card, int count) {
		this.card = card;
		this.count = count;
	}
	public Call (String cardString, int count) {
		this.card = new Card(cardString);
		this.count = count;
	}
	public int getCallLevel() {
		int callLevel = card.getRawSuit() + (count - 1) * 6;
		if (card.toString().equals("J+")) {
			callLevel++;
		}
		if (callLevel == 4 || callLevel == 5) {
			callLevel = -1;
		}
		return callLevel;
	}
	public int getSuit() {
		return card.getRawSuit();
	}
}
