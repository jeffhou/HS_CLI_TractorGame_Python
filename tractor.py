import sys, random
sys.path.append('C:\\Users\\Jeff Hou\\TRACTOR')
import cards,auction,trumplib,gameplay
player_levels=[0,0,0,0]
hands_and_bury = cards.deck_deal(cards.shuffle(cards.deck_setup()))
for i in range(len(hands_and_bury)):
	cards.hand_sort(hands_and_bury[i])
(boss_ID,point_marker)=auction.start(random.randint(0,3),hands_and_bury[:4])
trump_suit=trumplib.set_trump(boss_ID)
trumplib.get_trump(trump_suit, player_levels[boss_ID])


