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
def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hands):
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    deck = [(value, suit) for value in range(1, 14) for suit in suits]

    hands_and_their_indexes = {}

    for hand in hands:
        hands_and_their_indexes[hand] = deck.index(hand)

    sorted_hands = sorted(hands_and_their_indexes,
                          key=hands_and_their_indexes.get)

    return sorted_hands


def test():
    '''
     test cases from class
    '''
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    return "tests pass"


print(test)
