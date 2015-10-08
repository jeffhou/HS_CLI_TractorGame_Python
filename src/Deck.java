import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Deck {

	static final int CARDS_PER_DECK = 54;

	ArrayList<Card> deck;
	int numberOfDecks;

	public Deck(int numberOfDecks) {
		DebugUtils.notice("Instantiating a Deck with " + numberOfDecks + ".", 1);
		this.numberOfDecks = numberOfDecks;
		reset();
	}

	public void reset() {
		DebugUtils.notice("Remaking deck...", 1);
		deck = new ArrayList<Card>();
		for (int i = 0; i < 54; i++) {
			for (int j = 0; j < numberOfDecks; j++) {
				deck.add(new Card(i));
				DebugUtils.notice("Added " + deck.get(deck.size() - 1).toString() + " to Deck.", 1);
			}
		}
		DebugUtils.notice(toString(), 1);
		shuffle();
	}

	public void shuffle() {
		DebugUtils.notice("Shuffling...", 1);
		long seed = System.nanoTime();
		Collections.shuffle(deck, new Random(seed));
		DebugUtils.notice(toString(), 1);
	}
	
	public Card draw() {
		return deck.remove(0);
	}
	
	public String toString() {
		StringBuilder string = new StringBuilder();
		for (Card i : deck) {
			string.append(i.toString() + "\n");
		}
		return string.toString();
	}
}
