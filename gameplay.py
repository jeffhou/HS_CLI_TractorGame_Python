import sys
sys.path.append('C:\\Users\\Jeff Hou\\TRACTOR')
import trumplib
def eval_winner_single(in_first_ID,in_cards_played,in_trump):
	if trumplib.contains_trump(in_trump, in_cards_played):
		power_list=[0,0,0,0]
		counter=in_first_ID
		for i in range(4):
			if trumplib.is_trump(in_trump,in_cards_played[counter]):
				power_list[counter]=trumplib.trump_power(in_trump,in_cards_played[counter])
			counter=(counter+1)%4
		
		power_list_sorted=power_list
		power_list_sorted.sort()
		counter=in_first_ID
		for i in range(4):
			if power_list[counter]==power_list_sorted[-1]:
				return counter
			counter=(counter+1)%4
	else:
		first_suit=in_cards_played[in_first_ID][0]
		right_suit=[False,False,False,False]
		numbers=[]
		for i in range(4):
			right_suit[i]=in_cards_played[i][0]==first_suit
			if right_suit[i]:
				numbers.append(in_cards_played[i][1])
			else:
				numbers.append(-1)
		numbers_sorted=numbers
		numbers_sorted.sort()
		counter=in_first_ID
		for i in range(4):
			if numbers[counter]==numbers_sorted[-1]:
				return counter
			counter=(counter+1)%4	
def is_pair(in_cards):
	if len(in_cards)==2 and in_cards.count(in_cards[0])==2:
		return True
	else:
		return False
def is_tractor(in_cards):
	in_cards.sort()
	if len(in_cards)%2==0:
		for i in in_cards:
			if not in_cards.count(i)==2:
				return False
		
	else:
		return False
			