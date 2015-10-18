package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

public class CardCollection implements Iterable<Card>{
	private List<Card> cards;
	private boolean sorted;
	public CardCollection() {
		cards = new ArrayList<Card>();
		sorted = true;
	}
	public CardCollection(boolean sorted) {
		cards = new ArrayList<Card>();
		this.sorted = sorted;
	}

	public CardCollection(CardCollection cc) {
		this(cc.cards);
	}

	public CardCollection(List<Card> list) {
		cards = new ArrayList<Card>(list);
		sorted = true;
		Collections.sort(cards);
	}
	public void addCard(Card card) {
		cards.add(card);
		if (sorted) {
			Collections.sort(cards);
		}
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

	public int getCardCount() {
		return cards.size();
	}

	public boolean isEmpty() {
		return cards.isEmpty();
	}

	public boolean isSubSet(CardCollection o) {
		List<Card> sortedSubList = new ArrayList<Card>(cards);
		List<Card> sortedSuperList = new ArrayList<Card>(o.cards);
		
		int j = 0;
		for (int i = 0; i < sortedSubList.size(); i++){
			boolean notSubset = false;
			while(true) {
				//System.out.println("Comparing " + sortedSubList.get(i) + " (i="+i+") with " + sortedSuperList.get(j) + "(j="+j+") ");
				if(sortedSubList.get(i).equals(sortedSuperList.get(j))){
					j++;
					//System.out.println("EQUAL");
					break;
				}
				//System.out.println("UNEQUAL");
				j++;
				if(j >= sortedSuperList.size()){
					notSubset = true;
					break;
				}
			}
			if (notSubset || j == sortedSuperList.size()) {
				//System.out.println("RETURNING FALSE");
				return false;
			}
			
		}
		System.out.println("RETURNING TRUE");
		return true;
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
		System.out.println("SEED: " + seed);
		Collections.shuffle(cards, new Random(seed));
	}
	public int size() {
		return cards.size();
	}
	public void sort() {
		Collections.sort(cards);
	}
}
