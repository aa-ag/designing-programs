############------------ IMPORTS ------------############

# ---> TO DO: READ > https://stackoverflow.com/questions/41970795/what-is-the-best-way-to-create-a-deck-of-cards

############------------ FUNCTIONS ------------############
# -----------
# User Instructions
#
# Modify the poker() function to return the best hand
# according to the hand_rank() function. Since we have
# not yet written hand_rank(), clicking RUN won't do
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right.
#
# def poker(hands):
#     "Return the best hand: poker([hand,...]) => hand"
#     return max(hands, key=hand_rank)


def hand_rank(hands):
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    deck = [(value, suit) for value in range(1, 14) for suit in suits]

    return [deck.index(i) for i in hands]


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print(hand_rank([(6, 'Spades'), (5, 'Spades'), (7, 'Spades')]))
