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
  return render_template('index.html')

@app.route('/hello')
def hello():
  return render_template('hello.html', data=123456)

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

  if round.drawCard():
    options = round.generateAllPossibleCalls(Player.players[round.currentPlayer])
    print("Current Player: " + str(round.currentPlayer))
    return render_template('play_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), options=options, current_player=round.currentPlayer)
  else:
    if Card.trumpSuit == -1:
      round.autoAssignTrumpSuit()
    while not round.mainDeck.isEmpty():
      Player.players[round.boss].addCard(round.mainDeck.draw())
    return render_template('bury_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.boss)

@app.route('/make_call', methods=['POST'])
def make_call():
  global round
  if request.method == 'POST':
    call = Call.deserialize(request.form['call'])
    print(call)
    round.callTrump(round.currentPlayer, call)
  
  if round.drawCard():
    print("Current Player: " + str(round.currentPlayer))
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
    if round.buryCards(cards):
      round.currentPlayer = round.boss
      round.currentTrick = Trick()
      return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.currentPlayer, acrossPlayer=Player.players[(round.currentPlayer + 2)%4], leftPlayer=Player.players[(round.currentPlayer + 3)%4], rightPlayer=Player.players[(round.currentPlayer + 1)%4], trick=round.currentTrick)
    else:
      if Card.trumpSuit == -1:
        round.autoAssignTrumpSuit()
      while not round.mainDeck.isEmpty():
        Player.players[round.boss].addCard(round.mainDeck.draw())
      return render_template('bury_page.html', values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.boss)
@app.route('/play_cards', methods=['POST'])
def play_cards():
  global round
  if request.method == 'POST':
    cards = request.form.getlist('card')
    for i in range(len(cards)):
      cards[i] = Card(int(cards[i]))
    if round.playCardsForTrick(Player.players[round.currentPlayer], cards, round.currentTrick):
      if round.currentTrick.isComplete():
        round.updatePoints(round.currentTrick.getWinner(), round.currentTrick.getPoints())
        if Player.players[0].isEmpty():
          round.checkBottom()
          round.levelByPoints()
          round = Round(Player.players[round.getWinner()])
          return render_template('stats_page.html', players=Player.players, values=Card.VALUES)
        round.currentPlayer = round.currentTrick.getWinner()
        round.tricks.append(round.currentTrick)
        round.currentTrick = Trick()
        #show who the winner is
        return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.currentPlayer, acrossPlayer=Player.players[(round.currentPlayer + 2)%4], leftPlayer=Player.players[(round.currentPlayer + 3)%4], rightPlayer=Player.players[(round.currentPlayer + 1)%4], trick=round.currentTrick)
      else:
        round.currentPlayer = (round.currentPlayer + 1) % 4
        return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.currentPlayer, acrossPlayer=Player.players[(round.currentPlayer + 2)%4], leftPlayer=Player.players[(round.currentPlayer + 3)%4], rightPlayer=Player.players[(round.currentPlayer + 1)%4], trick=round.currentTrick)

    else:
      return render_template('main_page.html', points=round.playerPoints, values=Card.VALUES, players=Player.players, boss=round.boss, trump_string=getTrumpString(), current_player=round.currentPlayer, acrossPlayer=Player.players[(round.currentPlayer + 2)%4], leftPlayer=Player.players[(round.currentPlayer + 3)%4], rightPlayer=Player.players[(round.currentPlayer + 1)%4], trick=round.currentTrick)
if __name__ == '__main__':
  app.debug = True
  app.run()