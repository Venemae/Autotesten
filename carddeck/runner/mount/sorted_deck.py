############### sort_deck.py file

import create_deck
import randomize_deck
import copy

card_deck = randomize_deck.shuffled_deck
sides = create_deck.sides
card_values = create_deck.card_values
card_symbols = create_deck.card_symbols
 
sorted_deck = card_deck.copy()
sorted_deck.sort(key=lambda x:card_symbols.index(x['symbol']) * 14 + x['value'])
for x in sorted_deck:
        x["side"] = sides[0]
for x in sorted_deck:
        print(f"{x}")