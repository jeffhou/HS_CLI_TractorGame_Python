from flask import Flask, render_template, request
from TractorGame import TractorGame
from Player import Player
from Card import Card
from Call import Call
from Trick import Trick
from Round import Round
app = Flask(__name__)

@app.route('/')
def index():
  global game, round
  try:
    print(game)
  except:
    game = TractorGame()
    round = game.nextRound()
  return render_template('stats_page.html', players=Player.players, values=Card.VALUES)

@app.route('/start_game')
def start_game():
  global game, round
  game = TractorGame()
  round = game.nextRound()
  return render_template('stats_page.html', players=Player.players, values=Card.VALUES)

def getTrumpString():
  global round
  if Card.trumpSuit == -1:
    trump_string = Card.VALUES[Player.players[round.boss].level]
  elif Card.trumpSuit < 4:
    trump_string = Card.VALUES[Player.players[round.boss].level] + " of " + Card.SUIT_NAMES[Card.trumpSuit]
  else:
    trump_string = Card.VALUES[Player.players[round.boss].level] + " (No Trump)"
  return trump_string

@app.route('/start_round')
def start_round():
  global round
  if round.drawCard(): #drawing works
    options = round.generateAllPossibleCalls(Player.players[round.currentPlayer])
    return render_template('play_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), options=options, current_player=round.currentPlayer)
  else: #done drawing
    if Card.trumpSuit == -1:
      round.autoAssignTrumpSuit()
    round.giveBottom(round.boss)
    round.currentPlayer = round.boss
    return render_template('bury_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.boss)

@app.route('/make_call', methods=['POST'])
def make_call():
  global round
  if request.method == 'POST':
    call = Call.deserialize(request.form['call'])
    round.callTrump(round.currentPlayer, call)
  if round.drawCard():
    options = round.generateAllPossibleCalls(Player.players[round.currentPlayer])
    return render_template('play_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.currentPlayer)
  else:
    if Card.trumpSuit == -1:
      round.autoAssignTrumpSuit()
    while not round.mainDeck.isEmpty():
      Player.players[round.boss].addCard(round.mainDeck.draw())
    return render_template('bury_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.boss)

@app.route('/bury_cards', methods=['POST'])
def bury_cards():
  global round
  if request.method == 'POST':
    cards = request.form.getlist('card')
    for i in range(len(cards)):
      cards[i] = Card(int(cards[i]))

    if round.buryCards(cards): # bury successful
      round.currentPlayer = round.boss
      round.currentTrick = Trick()
      return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), trick=round.currentTrick, circle=round.getPlayerCircle())
    else: # retry
      return render_template('bury_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.boss)

@app.route('/play_cards', methods=['POST'])
def play_cards():
  global round
  if request.method == 'POST':
    cards = request.form.getlist('card')
    for i in range(len(cards)):
      cards[i] = Card(int(cards[i]))

    if round.playCardsForTrick(Player.players[round.currentPlayer], cards, round.currentTrick): #the combo the current player played is valid
      if round.currentTrick.isComplete():
        round.updatePoints(round.currentTrick.getWinner(), round.currentTrick.getPoints())
        if round.isComplete():
          round.checkBottom()
          round.levelByPoints()
          round = round.nextRound()
          return render_template('stats_page.html', players=Player.players, values=Card.VALUES)
        else:
          round.prepNextTrick()
          return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), trick=round.currentTrick, circle=round.getPlayerCircle())
      else:
        round.incrementCurrentPlayer()
        return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), trick=round.currentTrick, circle=round.getPlayerCircle())
    else:
      return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), trick=round.currentTrick, circle=round.getPlayerCircle())
if __name__ == '__main__':
  app.debug = True
  app.run()