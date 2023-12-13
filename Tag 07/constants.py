import types

HAND_TYPE_FIVEOF    = 0
HAND_TYPE_FOUROF    = 1
HAND_TYPE_FULLHOUSE = 2
HAND_TYPE_THREEOF   = 3
HAND_TYPE_TWOPAIR   = 4
HAND_TYPE_ONEPAIR   = 5
HAND_TYPE_HIGHCARD  = 6

Cards = types.SimpleNamespace()
Cards.JOKER   = 1
Cards.TWO     = 2
Cards.THREE   = 3
Cards.FOUR    = 4
Cards.FIVE    = 5
Cards.SIX     = 6
Cards.SEVEN   = 7
Cards.EIGHT   = 8
Cards.NINE    = 9
Cards.TEN     = 10
Cards.QUEEN   = 11
Cards.KING    = 12
Cards.ACE     = 13
Cards.INVALID = -1