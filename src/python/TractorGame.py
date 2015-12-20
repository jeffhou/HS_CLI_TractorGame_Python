from Player import Player
from Round import Round

class TractorGame:

  NUM_PLAYERS = 4
  NUM_DECKS = 2
  
  def __init__(self):
    self.startGame()
    
  def startGame(self):
    self.currentRound = None
    Player.players = []

    for i in range(TractorGame.NUM_PLAYERS): 
      Player.players.append(Player(i))
  
  def nextRound(self):
      if self.currentRound == None: 
        self.currentRound = Round(Player.players[0])
      else: 
        self.currentRound = Round(Player.players[self.currentRound.getWinner()])
      return self.currentRound