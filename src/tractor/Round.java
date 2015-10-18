package tractor;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Round {
	static final int NUM_PLAYERS = 4;
	static final int NUM_DECKS = 2;
	static final int NUM_LEFTOVER = 8;
	static int roundCount = 0;
	Deck mainDeck;
	int boss;
	int firstPlayer;
	Player[] players;
	ArrayList<Trick> tricks;
	boolean[] winners;
	// int trumpSuit;
	int[] playerTeams = { 0, 1, 0, 1 };
	int[] playerPoints = { 0, 0, 0, 0 };
	private int callLevel;

	public Round(Player[] players, int winner) {
		roundCount++;
		mainDeck = new Deck(NUM_DECKS);
		boss = winner;
		Card.trumpValue = players[boss].level;
		if (winner == -1) {
			firstPlayer = 0;
		} else {
			firstPlayer = winner;
		}
		tricks = new ArrayList<Trick>();
		Card.trumpSuit = -1;
		this.players = players;
		callLevel = -1;
	}

	public int getWinner() { // used for creation of subsequent round
		for (int i = 0; i < NUM_PLAYERS; i++) {
			if (winners[(i + boss + 1) % NUM_PLAYERS]) {
				return (i + boss + 1) % NUM_PLAYERS;
			}
		}
		return -1; // should never happen
	}

	public void start() {
		dealAndCall();
		replaceBottom();
		for (Player i : players) {
			Collections.sort(i.cards);
		}
		populateTricks();
		checkBottom();
		levelByPoints();
	}

	private void checkBottom() {
		int points = 0;
		for (Card i : mainDeck.cards) {
			points += i.getPoints();
		}
		int multiplier = 2;
		Trick lastTrick = tricks.get(tricks.size() - 1);
		switch (lastTrick.getType()) {
		case SINGLE:
			multiplier = 2;
			break;
		case PAIR:
			multiplier = 4;
			break;
		case TRACTOR:
			multiplier = lastTrick.getNumCards() * 2;
		default:
			break;
		}
		playerPoints[tricks.get(tricks.size()).getWinner()] += points * multiplier;
	}

	private void replaceBottom() {
		if (Card.trumpSuit == -1) {
			autoAssignTrumpSuit();
		}
		if (Card.trumpSuit == 4) {
			System.out.println("\n=== REPLACE BOTTOM (!)===");
		} else {
			System.out.println("\n=== REPLACE BOTTOM (" + Card.SUITS[Card.trumpSuit] + ")===");
		}

		while (mainDeck.size() > 0) {
			players[boss].addCard(mainDeck.pop());
		}
		updateDisplay(players[boss]);

		for (Card i : playCards(players[boss], 8, ComboType.NONE)) {
			mainDeck.addCard(i);
			players[boss].cards.remove(i);
		}
		updateDisplay(players[boss]);
	}

	private void autoAssignTrumpSuit() {
		System.out.print("Bottom 8: ");
		for (Card i : mainDeck.cards) {
			System.out.print(i.toString() + " ");
		}

		for (Card i : mainDeck.cards) {
			if (i.cardIndex % 13 == Card.trumpValue) {
				Card.trumpSuit = i.getSuit();
				return;
			}
		}

		Card selector = null;
		for (Card i : mainDeck.cards) {
			if (selector == null || selector.cardIndex % 13 < i.cardIndex % 13) {
				selector = i;
			}
		}
		Card.trumpSuit = selector.getSuit();
	}

	private Card[] playCards(Player player, int numCards, ComboType c) {
		List<Card> cardsPlayed = new ArrayList<Card>();
		while (cardsPlayed.size() != numCards) {
			if (!Util.isSubSet(cardsPlayed, player.cards) || cardsPlayed.size() > 8) {
				cardsPlayed.removeAll(cardsPlayed);
			}
			inputCardsPlayed(cardsPlayed, player);
		}
		Card[] cards = new Card[numCards];
		for (int i = 0; i < numCards; i++) {
			cards[i] = cardsPlayed.get(i);
		}
		return cards;
	}

	private void updateDisplay(Player player) {
		System.out.print("Player " + player.id + ": ");
		for (Card i : player.cards) {
			System.out.print(i.toString() + " ");
		}
		System.out.println();
	}

	private void levelByPoints() {
		if (getPointsForChallengers() < 80) {
			incumbentsWin();
			if (getPointsForChallengers() == 0) {
				levelUpWinners(3);
			} else if (getPointsForChallengers() < 40) {
				levelUpWinners(2);
			} else if (getPointsForChallengers() < 80) {
				levelUpWinners(1);
			}
		} else {
			challengersWin();
			levelUpWinners(getPointsForChallengers() / 40 - 2);
		}
	}

	private void determineWinners(boolean challengersWin) {
		int challengerTeam = playerTeams[boss];
		for (int i = 0; i < players.length; i++) {
			if ((playerTeams[i] == challengerTeam) == challengersWin) {
				winners[i] = true;
			}
		}
	}

	private void challengersWin() {
		determineWinners(true);
	}

	private void levelUpWinners(int level) {
		for (int i = 0; i < NUM_PLAYERS; i++) {
			players[i].levelUp(level);
		}
	}

	private void incumbentsWin() {
		determineWinners(false);
	}

	private int getPointsForChallengers() {
		int points = 0;
		for (int i = 0; i < NUM_PLAYERS; i++) {
			if (playerTeams[i] != playerTeams[boss]) {
				points += playerPoints[i];
			}
		}
		return points;
	}

	private void populateTricks() {
		while (players[0].hasCards()) {
			tricks.add(nextTrick());
		}
	}

	private Trick nextTrick() {
		Trick currentTrick = new Trick();
		if (Card.trumpSuit == 4) {
			System.out.println("=== NEW TRICK (!" + Card.NORMAL_VALUES[players[boss].level] + ")===");
		} else {
			System.out.println(
					"=== NEW TRICK (" + Card.SUITS[Card.trumpSuit] + Card.NORMAL_VALUES[players[boss].level] + ")===");
		}

		for (Player i : players) {
			System.out.println("Player " + i.id + ": " + playerPoints[i.id] + " points");
		}

		for (int i = 0; i < NUM_PLAYERS; i++) {
			int playerID = (i + firstPlayer) % NUM_PLAYERS;
			updateDisplay(players[playerID]);
			playCards(players[playerID], currentTrick);
		}
		updatePoints(currentTrick.getWinner(), currentTrick.getPoints());
		firstPlayer = currentTrick.getWinner();
		System.out.println("Player " + currentTrick.getWinner() + " wins trick and earns " + currentTrick.getPoints()
				+ " points!");
		return currentTrick;
	}

	private void playCards(Player player, Trick currentTrick) {
		List<Card> cardsPlayed = new ArrayList<Card>();
		boolean valid = false;
		Combo combo = null;
		while (!valid) {
			inputCardsPlayed(cardsPlayed, player);
			combo = new Combo(player, cardsPlayed);
			valid = validateCardsPlayed(combo, currentTrick, player);
			if (!valid) {
				display("Invalid!");
				cardsPlayed.removeAll(cardsPlayed);
			}

		}
		currentTrick.add(combo);
		player.removeCards(cardsPlayed);
	}

	private boolean validateCardsPlayed(Combo combo, Trick currentTrick, Player player) {

		if (currentTrick.isEmpty()) {
			// first combo played, as long as same suit and valid type, is valid
			System.out.println("First combo played: " + combo.getType());
			return combo.getType() != ComboType.NONE;
		}
		Combo first = currentTrick.combosPlayed.get(0);
		if (combo.cards.size() == first.cards.size()) {
			// number of cards is right
			if (combo.getSuit() != first.getSuit()) {
				// suits aren't the same
				if (player.countSuit(first.getSuit()) == combo.countSuit(first.getSuit())) {
					return true;
				} else {
					return false;
				}
			} else {
				// suits are the same
				if (combo.getType() == first.getType()) {
					// comboTypes are the same
					return true;
				} else {
					// comboTypes aren't the same
					System.out.println("combos aren't the same");
					if (player.hasComboToPlay(first)) {
						return false;
					} else if (player.playedRequired(first, combo)) {
						System.out.println("doesn't have that combo");
						return true;
					}
				}
			}
		}
		return false;
		/*
		 * if (combo.cards.size() == 1) { if (currentTrick.isEmpty() ||
		 * combo.cards.get(0).getSuit() == currentTrick.suit) { return true; }
		 * else { for (Card i : cards) { if (i.getSuit() == currentTrick.suit) {
		 * return false; } } return true; } } return false;
		 */
	}

	private String getUserInput(String prompt) {
		System.out.print(prompt);
		@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);
		String inputString = scanner.nextLine();
		// scanner.close();
		return inputString;
	}

	private void inputCardsPlayed(List<Card> cardsPlayed, Player player) {
		List<Card> cards = cardsPlayed;
		System.out.print("Cards (" + cards.size() + "): ");
		for (Card i : cards) {
			System.out.print(i + " ");
		}
		String inputString = getUserInput("");
		if (inputString.equals(""))
			return;
		String[] cardStrings = inputString.split(" ");
		for (String i : cardStrings) {
			cards.add(new Card(i));
		}
		Collections.sort(cards);
	}

	private void display(String string) {
		System.out.println(string);
	}

	private void updatePoints(int winner, int points) {
		playerPoints[winner] += points;
	}

	private void dealAndCall() {
		while (mainDeck.size() > NUM_LEFTOVER) {
			for (int i = 0; i < NUM_PLAYERS; i++) {
				Card newCard = mainDeck.pop();
				players[i].addCard(newCard);
				if (Card.trumpSuit == 4) {
					System.out.println("\n=== HAND (!" + Card.NORMAL_VALUES[players[boss].level] + ")===");
				} else if (Card.trumpSuit != -1) {
					System.out.println("\n=== HAND (" + Card.SUITS[Card.trumpSuit] + ""
							+ Card.NORMAL_VALUES[players[boss].level] + ")===");
				} else {
					System.out.println("\n=== HAND (~" + Card.NORMAL_VALUES[players[boss].level] + ")===");
				}

				updateDisplay(players[i]);
				if (true) {
					callTrumpInput(players[i]);
				}

			}
		}
	}

	private void callTrumpInput(Player player) {
		String trumpInput = getUserInput("Call: ");
		if (!trumpInput.equals("")) {
			int numCards = Integer.parseInt("" + trumpInput.charAt(0));
			String suitString = trumpInput.substring(1);
			int trumpSuit = -1;
			int newCallLevel = 0;
			for (int i = 0; i < Card.SUITS.length; i++) {
				if (Card.SUITS[i].equals(suitString)) {
					trumpSuit = i;
					newCallLevel = i;
				}
			}
			if (trumpSuit == -1) {
				if (suitString.equals("J-")) {
					trumpSuit = 4;
					newCallLevel = 4;
				} else if (suitString.equals("J+")) {
					trumpSuit = 4;
					newCallLevel = 5;
				}
			}

			newCallLevel += (numCards - 1) * 6;
			System.out.println("newCallLevel: " + newCallLevel);

			if (newCallLevel > callLevel) {
				System.out.println("Checking override conditions...");
				if (player.canOverride(player, newCallLevel)) {
					Card.trumpSuit = trumpSuit;
					callLevel = newCallLevel;
					if (trumpSuit == 4) {
						System.out.println("Trump Suit is now nothing!");
					} else {
						System.out.println("Trump Suit is now " + Card.SUITS[trumpSuit]);
					}
					if (roundCount == 1) {
						boss = player.id;
						firstPlayer = player.id;
					}
					return;
				}
			}
			System.out.println("Invalid call!");
		}
	}

}
