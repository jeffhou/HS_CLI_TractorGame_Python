package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Deck {
	private static final int DECK_SIZE = 54;
	List<Card> cards;
	public Deck(int numDecks) {
		cards = new ArrayList<Card>();
		for (int i = 0; i < numDecks; i++) {
			addDeck();
		}
		shuffle();
	}

	private void shuffle() {
		long seed = TractorGame.TESTING ? 1445123063075L : System.currentTimeMillis();
		System.out.println("SEED: " + seed);
		Collections.shuffle(cards, new Random(seed));
	}

	private void addDeck() {
		for (int i = 0; i < DECK_SIZE; i++) {
			cards.add(new Card(i));
		}
	}

	public int size() {
		return cards.size();
	}

	public Card pop() {
		return cards.remove(0);
	}

	public void addCard(Card i) {
		cards.add(i);
	}

}
