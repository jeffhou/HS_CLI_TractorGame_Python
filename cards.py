import random
def deck_setup():
	deck=[]
	for i in range(2):
		for j in range(4):
			for k in range(13):
				deck.append([j,k])
		for j in range(2):
			deck.append([4,j+13])
	return deck
def shuffle(in_deck):
	random.shuffle(in_deck)
	return in_deck
def deck_deal(in_deck):
	hands=[]
	for i in range(4):
		hands.append([])
		for j in range(25):
			hands[i].append(in_deck.pop(0))
	hands.append([])
	while len(in_deck)>0:
		hands[4].append(in_deck.pop(0))
	return hands
def hand_sort(in_hand):
	in_hand.sort()
	return in_hand
def display_cards(in_cards):
	suits=['Hearts','Spades','Clubs','Diamonds','Trump']
	cards=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace','Big Joker','Small Joker']
	for i in range(5):
		print(suits[i])
		for j in in_cards:
			if j[0]==i:
				print(cards[j[1]],end=' ')
		print()
