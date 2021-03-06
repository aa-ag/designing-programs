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


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif ...


# def hand_rank(hands):
#     suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

#     deck = [(value, suit) for value in range(1, 14) for suit in suits]

#     hands_and_their_indexes = {}

#     for hand in hands:
#         hands_and_their_indexes[hand] = deck.index(hand)

#     sorted_hands = sorted(hands_and_their_indexes,
#                           key=hands_and_their_indexes.get)

#     return sorted_hands


def test():
    '''
     test cases from class
    '''
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 8, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (8, 10, 7)
    return "tests pass"


print(test)
