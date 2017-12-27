def set_trump(in_boss_ID):
	print('Player ' + str(in_boss_ID+1) + ', what would you like to be trump?')
	print('1) Hearts')
	print('2) Spades')
	print('3) Clubs')
	print('4) Diamonds')
	return int(input('Trump Suit: '))-1
def get_trump(in_trump_suit,in_trump_value):
	trump=[]
	for j in range(13):
		if j != in_trump_value:
			trump.append([in_trump_suit,j])
	for j in range(4):
		if j != in_trump_suit:
			trump.append([j,in_trump_value])
	trump.append([in_trump_suit,in_trump_value])
	for j in range(2):
			trump.append([4,j+13])
	return trump
def trump_power(in_trump,in_card):
	return in_trump.index(in_card)
def is_trump(in_trump,in_card):
	return bool(in_trump.count(in_card)):
def contains_trump(in_trump,in_cards):
	for i in in_cards:
		if is_trump(in_trump,i):
			return True
	return False