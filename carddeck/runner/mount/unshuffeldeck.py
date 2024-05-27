import random

card_symbols = ["hearts", "clubs", "spades", "diamonds"]
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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

carddeck = []

# Generate the original deck with all cards facing up
for card_symbol in card_symbols:
    for card_value in card_values:
        card_color = color_config[card_symbol]
        card_side = "up"  # Set the side to "up" for original deck
        card_template = {
            "color": card_color,
            "value": card_value,
            "side": card_side,
            "symbol": card_symbol
        }
        carddeck.append(card_template)

# Shuffle the original deck
shuffled_deck = carddeck.copy()
random.shuffle(shuffled_deck)

# Set random orientation for shuffled cards
for card in shuffled_deck:
    card["side"] = random.choice(["up", "down"])

# Print the shuffled cards
print("Shuffled Cards:")
for shuffled_card in shuffled_deck:
    print(shuffled_card)

# Print the original cards
print("\nOriginal Cards:")
for original_card in carddeck:
    print(original_card)
