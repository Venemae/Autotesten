############### randomize_deck.py file

import create_deck
import random
import copy
 
card_deck = create_deck.card_deck
sides = create_deck.sides
sorted_deck = copy.deepcopy(card_deck)
 
random.shuffle(sorted_deck)
 
shuffled_deck = sorted_deck
for x in range(len(shuffled_deck)):
    shuffled_deck[x]["side"] = sides[random.randint(0,1)]
 
print(f"shuffled_deck length: {len(shuffled_deck)} and card_deck length: {len(card_deck)}")
 
for i in range(len(card_deck)):
   
    print("\n", 50*"#")
    print(f"shuf_deck: {(shuffled_deck[i])}")
    print(f"card_deck: {(card_deck[i])}")
    print(50*"#", "\n")
	