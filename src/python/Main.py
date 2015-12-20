from Player import Player
from Round import Round


class TractorGame:

  NUM_PLAYERS = 4
  NUM_DECKS = 2
  
  def __init__(self):
    self.startGame()
    
  def startGame(self):

    currentRound = None
    Player.players = []

    for i in range(TractorGame.NUM_PLAYERS): 
      Player.players.append(Player(i))

    while True: 
      if currentRound == None: 
        currentRound = Round(Player.players[0])
      else: 
        currentRound = Round(Player.players[currentRound.getWinner()])
      currentRound.start()

TractorGame()