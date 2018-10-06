""" Notes
Cards will be repreented in binary for fast runtime.
Details are explained in the README
"""

from random import shuffle, randrange, sample
# import random

# Constants
GAMES = 1
suit_num_to_letter = {0: 'C', 1: 'D', 2: 'H', 3: 'S'}
value_num_to_letter = {1: 'A',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5',
                    6: '6',
                    7: '7',
                    8: '8',
                    9: '9',
                    10: 'T',
                    11: 'J',
                    12: 'Q',
                    13: 'K'}
suit_letter_to_num = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
value_letter_to_num = {'A': 1,
                       '2': 2,
                       '3': 3,
                       '4': 4,
                       '5': 5,
                       '6': 6,
                       '7': 7,
                       '8': 8,
                       '9': 9,
                       'T': 10,
                       'J': 11,
                       'Q': 12,
                       'K': 13}

def simulate_hand(player1):
    ## Outline

    # Start with two players
    # Player one gets pocket aces
    # Player two gets pocket tens
    # The river is drawn randomly
    # The winner is computed
    # The winner's win_count is incremented
    # The process is repeated until statistical significance is achieved

    # Create Deck
    deck = []
    for suit in range(4):
        bit_suit = '{0:02b}'.format(suit)
        for value in range(13):
            bit_value = '{0:04b}'.format(value+1)
            bit_card = bit_value + bit_suit
            deck.append(bit_card)
    # print(deck)
    shuffle(deck)
    # print(deck)
    deck.remove(player1[0])
    deck.remove(player1[1])
    # print(deck)

    player2 = []
    player2.append(deck.pop())
    player2.append(deck.pop())

    river = []
    for i in range(5):
        river.append(deck.pop())

    print("Player 1:")
    print_hand(player1)

    print("Player 2:")
    print_hand(player2)

    print("River: ")
    print_hand(river)

    decide_winner(player1, player2, river)

def decide_winner(player1, player2, river):
    print()

def print_hand(cards):
    for card in cards:
        print_bin_as_string(card)

def print_bin_as_string(card):
    suit = suit_num_to_letter[int(card, base=2) % 4]
    value = value_num_to_letter[int(card, base=2) // 4]
    print(value, suit)

def choose_hand(input):
    value1 = value_letter_to_num[input[0]]
    value2 = value_letter_to_num[input[1]]

    # If suited
    if len(input) == 3:
        # Choose 1 suit
        card1_bit_suit = '{0:02b}'.format(randrange(4))
        card2_bit_suit = card1_bit_suit
        # Choose distinct values
        card1_bit_value = '{0:04b}'.format(value1)
        card2_bit_value = '{0:04b}'.format(value2)

    # Else, if not suited
    else:
        # Choose 2 suits
        suits = sample([0, 1, 2, 3], 2)
        card1_bit_suit = '{0:02b}'.format(suits[0])
        card2_bit_suit = '{0:02b}'.format(suits[1])
        # Choose values
        card1_bit_value = '{0:04b}'.format(value1)
        card2_bit_value = '{0:04b}'.format(value2)

    card1_bit = card1_bit_value + card1_bit_suit
    card2_bit = card2_bit_value + card2_bit_suit

    return [card1_bit, card2_bit]

def main():

    player1 = choose_hand('ATs')

    for i in range(GAMES):
        simulate_hand(player1)

if __name__ == "__main__":
    main()
