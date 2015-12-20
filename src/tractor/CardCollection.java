package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

public class CardCollection implements Iterable<Card> {
	protected List<Card> cards;

	public CardCollection() {
		cards = new ArrayList<Card>();
	}

	public void addCards(CardCollection cc) {
		for (Card i : cc) {
			cards.add(i);
		}
	}

	public void addCard(Card card) {
		cards.add(card);
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

	public Card get(int i) {
		return cards.get(i);
	}

	public int getCount(Card c) {
		return Collections.frequency(cards, c);
	}

	public int getCardCount() {
		return cards.size();
	}

	public boolean isEmpty() {
		return cards.isEmpty();
	}

	@Override
	public Iterator<Card> iterator() {
		return cards.iterator();
	}

	public boolean remove(Card i) {
		return cards.remove(i);
	}

	public Card remove(int i) {
		return cards.remove(i);
	}

	public void removeAll() {
		cards.removeAll(cards);
	}

	public void removeCards(CardCollection cards) {
		for (Card i : cards) {
			this.cards.remove(i);
		}
	}

	public void shuffle() {
		long seed = TractorGame.TESTING ? 1445123063075L : System.currentTimeMillis();
		Collections.shuffle(cards, new Random(seed));
	}

	public int size() {
		return cards.size();
	}

	public void sort() {
		Collections.sort(cards);
	}
}
