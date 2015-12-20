package tractor;

public class Deck extends CardCollection {

	private static final int DECK_SIZE = 54;

	public Deck(int numDecks) {
		super();
		addDecks(numDecks);
		shuffle();
	}

	/**
	 * Adds a complete deck of playing cards into the main deck.
	 */
	private void addDeck() {
		for (int i = 0; i < DECK_SIZE; i++) {
			addCard(new Card(i));
		}
	}

	/**
	 * adds multiple decks into main deck
	 */
	private void addDecks(int numDecks) {
		for (int i = 0; i < numDecks; i++) {
			addDeck();
		}
	}

	public Card draw() {
		return remove(0);
	}
}
