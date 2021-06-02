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

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

deck = [(value, suit) for value in range(1, 14) for suit in suits]

print(deck)
'''
[(1, 'Hearts'), (1, 'Diamonds'), (1, 'Spades'), 
(1, 'Clubs'), (2, 'Hearts'), (2, 'Diamonds'), 
(2, 'Spades'), (2, 'Clubs'), (3, 'Hearts'), 
(3, 'Diamonds'), (3, 'Spades'), (3, 'Clubs'), 
(4, 'Hearts'), (4, 'Diamonds'), (4, 'Spades'), 
(4, 'Clubs'), (5, 'Hearts'), (5, 'Diamonds'), 
(5, 'Spades'), (5, 'Clubs'), (6, 'Hearts'), 
(6, 'Diamonds'), (6, 'Spades'), (6, 'Clubs'), 
(7, 'Hearts'), (7, 'Diamonds'), (7, 'Spades'), 
(7, 'Clubs'), (8, 'Hearts'), (8, 'Diamonds'), 
(8, 'Spades'), (8, 'Clubs'), (9, 'Hearts'), 
(9, 'Diamonds'), (9, 'Spades'), (9, 'Clubs'), 
(10, 'Hearts'), (10, 'Diamonds'), (10, 'Spades'), 
(10, 'Clubs'), (11, 'Hearts'), (11, 'Diamonds'), 
(11, 'Spades'), (11, 'Clubs'), (12, 'Hearts'), 
(12, 'Diamonds'), (12, 'Spades'), (12, 'Clubs'), 
(13, 'Hearts'), (13, 'Diamonds'), (13, 'Spades'), 
(13, 'Clubs')]
'''

# def poker(hands):
#     "Return the best hand: poker([hand,...]) => hand"
#     return max(hands, key=hand_rank)


############------------ DRIVER CODE ------------############
# if __name__ == "__main__":
# poker([(5, 'S'), (6, 'S'), (7, 'S')])
