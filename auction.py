import cards

def start(in_bidder_ID,in_cards):
	player_bidder=[True,True,True,True]
	high_bid = 0
	while player_bidder.count(True)>1:
		if player_bidder[in_bidder_ID]:
			print('===Player',in_bidder_ID+1,'===')
			cards.display_cards(in_cards[in_bidder_ID])
			print('===============')
			new_bid=int(input('Bid(Min = '+str(high_bid)+'): '))
			if new_bid > high_bid:
				high_bid=new_bid
			else:
				player_bidder[in_bidder_ID]=False
		in_bidder_ID=(in_bidder_ID+1)%4
	print('Player ' +str(player_bidder.index(True)+1) + ' won the auction!')
	return (player_bidder.index(True),high_bid)
		