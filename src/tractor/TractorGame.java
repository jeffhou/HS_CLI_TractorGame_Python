package tractor;

public class TractorGame {

	static final int NUM_PLAYERS = 4;
	static final int NUM_DECKS = 2;
	public static final boolean TESTING = true;
	static Player[] players;

	public static void startGame() {

		Round currentRound = null;
		players = new Player[NUM_PLAYERS];

		for (int i = 0; i < players.length; i++) {
			players[i] = new Player(i);
		}

		while (true) {
			if (currentRound == null) {
				currentRound = new Round(players[0]);
			} else {
				currentRound = new Round(players[currentRound.getWinner()]);
			}
			currentRound.start();
		}
	}

	public static void main(String[] args) {
		startGame();
	}
}
