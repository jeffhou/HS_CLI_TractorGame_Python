class TractorGame:

  NUM_PLAYERS = 4 #static final int NUM_PLAYERS = 4;
  NUM_DECKS = 2   #static final int NUM_DECKS = 2;
  TESTING = True  #public static final boolean TESTING = true;
  #static Player[] players;
  
  def __init__(self):
    self.startGame()
    
  def startGame(self):#public static void startGame() {

    currentRound = None#Round currentRound = null;
    players = []#players = new Player[NUM_PLAYERS];

    for i in range(TractorGame.NUM_PLAYERS): #for (int i = 0; i < players.length; i++) {
      players.append(Player(i))#players[i] = new Player(i);
    #}

    while True: #while (True) {
      if currentRound == None: #if (currentRound == null) {
        currentRound = Round(players[0])#currentRound = new Round(players[0]);
      else: #} else {
        currentRound = Round(players[currentRound.getWinner()])#currentRound = new Round(players[currentRound.getWinner()]);
      #}
      currentRound.start()#currentRound.start();
    #}
  #}

  #public static void main(String[] args) {
  #  startGame();
  #}
#}
TractorGame()
