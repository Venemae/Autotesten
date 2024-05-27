############### create_deck.py file

import random

card_symbols = ["hearts", "clubs", "spades", "diamonds"]

card_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]

color_config = {
    "hearts": "red",
    "diamonds": "red",
    "clubs": "black",
    "spades": "black"
}

suit_config = {
    "11": "jack",
    "12": "queen",
    "13": "king",
    "14": "ace"
}

sides = ["up", "down"]


card_deck = []

for card_symbol in card_symbols:
    
    print(f"generating: {card_symbol}")
    
    for card_value in card_values:
        
        card_color = color_config[card_symbol]
        
        card_side = sides[0]#[random.randint(0,0)]
                
        print(f"adding: {card_symbol} {card_value} with color: {card_color} cardside: {card_side}")
        
        card_template = {
            
            "color": card_color,
            "value": card_value,
            "side": card_side,
            "symbol": card_symbol
            
        }
        
        card_deck.append(card_template)
        
        print(f"Current card count is: {len(card_deck)} cards")