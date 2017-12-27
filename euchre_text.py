import random
random.seed(0)
def setup_deck():
	card_values=['a','k','q','j','10','9']
	card_suits=['s','h','c','d']
	deck=[]
	for i in card_suits:
		for j in card_values:
			deck.append(i+j)
	return deck
def deal_deck(deck):
	hands=[[],[],[],[]]
	for i in range(len(hands)):
		for j in range(5):
			hands[i].append(deck.pop(0))
	return hands
def call_trump():
        display_hands()
        display_kitty()
        display_first_card()
        first_card=cards["Kitty"][0]
        return _call_trump()
def _call_trump():
        global dealer
        for i in range(4):
                current_player=(i+dealer+1)%4
                if input("Player "+str(current_player)+": Pick it up?").strip()=="y":
                        return current_player
        return -1
def _call_suit():
        global dealer,cards
        card_suits=['s','h','c','d']
        card_suits.pop(card_suits.index(cards["Kitty"][0][0]))
        for i in range(4):
                current_player=(i+dealer+1)%4
                if i==3 or input("Player "+str(i)+": Call Trump Suit?").strip()=="y":
                        trump_suit=""
                        while trump_suit not in card_suits:
                                trump_suit=input("Trump Suit")
                        return (trump_suit,current_player)
def display_hands():
        for i in range(len(cards["Hands"])):
                print("Player "+str(i)+"'s HAND: ",cards["Hands"][i])
def display_hand(hand_id):
        print("Player "+str(hand_id)+"'s HAND: ",cards["Hands"][hand_id])
def display_kitty():
        print("KITTY: " , cards["Kitty"])
def display_first_card():
        print("FIRST CARD: ",cards["Kitty"][0])
def setup_suits_with_trump():
        global trump_suit
        color_neighbor={'s':'c','c':'s','h':'d','d':'h'}
        card_suits=['s','h','c','d']
        card_values=['a','k','q','j','10','9']
        cards={}        
        cards[trump_suit]=[]
        cards[trump_suit].append(trump_suit+'j')
        cards[trump_suit].append(color_neighbor[trump_suit]+'j')
        for i in ['a','k','q','10','9']:
                cards[trump_suit].append(trump_suit+i)
        cards[color_neighbor[trump_suit]]=[]
        for j in ['a','k','q','10','9']:
                cards[color_neighbor[trump_suit]].append(color_neighbor[trump_suit]+j)
        card_suits.pop(card_suits.index(trump_suit))
        card_suits.pop(card_suits.index(color_neighbor[trump_suit]))
        for j in card_suits:
                cards[j]=[]
                for k in ['a','k','q','j','10','9']:
                        cards[j].append(j+k)
        return(cards)
def sort_hands():
        global trump_suit, cards, deck_order
        color_neighbor={'s':'c','c':'s','h':'d','d':'h'}
        
        for i in cards["Hands"]:
                card_suits=['s','h','c','d']
                temp_hand=[]
                for j in deck_order[trump_suit]:
                        if j in i:
                                temp_hand.append(i.pop(i.index(j)))
                print(card_suits)
                card_suits.pop(card_suits.index(trump_suit))
                for j in deck_order[color_neighbor[trump_suit]]:
                        if j in i:
                                temp_hand.append(i.pop(i.index(j)))
                card_suits.pop(card_suits.index(color_neighbor[trump_suit]))
                for j in card_suits:
                        for k in deck_order[j]:
                                if k in i:
                                       temp_hand.append(i.pop(i.index(k)))
                for j in temp_hand:
                        i.append(j)
        #print(cards["Hands"])
def hand_contains_suit(player_id,suit):
        for i in cards["Hands"][player_id]:
                if get_suit(i)==suit:
                        return True
        return False
def is_trump(card):
        global trump_suit,deck_order
        return card in deck_order[trump_suit]
def new_card_wins(winning_card,new_card):
        first_suit=get_suit(winning_card)
        global trump_suit,deck_order
        if get_suit(new_card)==trump_suit:
                print(1)
                if first_suit!=trump_suit:
                        return True
        if get_suit(new_card)==first_suit:
                print(2)
                print(deck_order)
                return deck_order[first_suit].index(winning_card) > deck_order[first_suit].index(new_card)
        print(3)
        return False
def get_suit(card):
        global deck_order
        for i in deck_order:
                if card in deck_order[i]:
                       return i     
def new_round():
        global first_player,deck_order
        first_suit=""
        cards_played={}
        for i in range(4):
                current_player=(first_player+i)%4
                display_hand(current_player)
                card_played=""
                while card_played not in cards["Hands"][current_player]:
                        card_played=input("Play: ")
                        print(card_played)
                        if i==0:
                                first_suit=get_suit(card_played)
                        else:
                                if hand_contains_suit(current_player,first_suit) and get_suit(card_played)!=first_suit:
                                        card_played=""
                cards_played[current_player]=card_played
                if i==0:
                        winning_player=current_player
                        winning_card=card_played
                else:
                        if new_card_wins(winning_card,card_played):
                                print(card_played+" is better than "+winning_card)
                                winning_player=current_player
                                winning_card=card_played
                cards["Hands"][current_player].pop(cards["Hands"][current_player].index(card_played))
        first_player=winning_player
        return winning_player
team_points=[0,0]
while team_points[0]<10 or team_points[1]<10:
        dealer=0
        deck_to_be_dealt = setup_deck()
        random.shuffle(deck_to_be_dealt)
        cards={"Hands":deal_deck(deck_to_be_dealt),"Kitty":deck_to_be_dealt}
        player_who_called=call_trump()

        if player_who_called==-1:
                print("No one said pick it up.")
                (trump_suit,player_who_called)=_call_suit()
        else:
                if player_who_called%2==0:
                        print("Player "+str(player_who_called)+" of Team Even called it.")
                else:
                        print("Player "+str(player_who_called)+" of Team Odd called it.")
                print("Trump suit: " + cards["Kitty"][0][0])
        cards["Hands"][dealer].append(cards["Kitty"][0])
        print(cards["Hands"][dealer])
        card_discard=input("Discard: ").strip()
        cards["Kitty"].append(cards["Hands"][dealer].pop(cards["Hands"][dealer].index(card_discard)))
        for i in range(len(cards["Hands"])):
                print("Player "+str(i)+"'s HAND: ",cards["Hands"][i])
        trump_suit=(cards["Kitty"][0][0])
        deck_order=setup_suits_with_trump()
        sort_hands()
        display_hands()
        first_player=dealer+1
        team_score=[0,0]
        for i in range(5):
                team_score[new_round()%2]+=1
        print(team_score)
        winning_team=team_score.index(max(team_score))
        if team_score[winning_team]!=5:
                points_awarded=1
        else:
                points_awarded=2
        if winning_team!=player_who_called%2:
                points_awarded+=1
        team_points[winning_team]+=points_awarded
        print(team_points)
input("DONE...")
