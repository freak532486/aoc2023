from constants import *

def cardToChar(card: int) -> chr:
    match card:
        case Cards.JOKER: return 'J'
        case Cards.TWO:   return '2'
        case Cards.THREE: return '3'
        case Cards.FOUR:  return '4'
        case Cards.FIVE:  return '5'
        case Cards.SIX:   return '6'
        case Cards.SEVEN: return '7'
        case Cards.EIGHT: return '8'
        case Cards.NINE:  return '9'
        case Cards.TEN:   return 'T'
        case Cards.QUEEN: return 'Q'
        case Cards.KING:  return 'K'
        case Cards.ACE:   return 'A'

    print(f"Matched invalid card {card}!")
    return '?'

def charToCard(c: chr):
    match c:
        case 'J': return Cards.JOKER
        case '2': return Cards.TWO
        case '3': return Cards.THREE
        case '4': return Cards.FOUR
        case '5': return Cards.FIVE
        case '6': return Cards.SIX
        case '7': return Cards.SEVEN
        case '8': return Cards.EIGHT
        case '9': return Cards.NINE
        case 'T': return Cards.TEN
        case 'Q': return Cards.QUEEN
        case 'K': return Cards.KING
        case 'A': return Cards.ACE
    
    print(f"Matched invalid card {c}!")
    return Cards.INVALID


def strToHand(input: str) -> list:
    ret = []
    for c in input:
        ret.append(charToCard(c))
    return ret

def handToStr(hand: list) -> str:
    ret = ""
    for card in hand:
        ret += cardToChar(card)
    return ret

def getHandType(hand: list) -> int:
    numJokers = 0

    # Convert to dict
    card_dict = {}
    for card in hand:
        if card == Cards.JOKER:
            numJokers += 1
            continue

        if card not in card_dict:
            card_dict[card] = 0

        card_dict[card] += 1

    # Get sorted list of card occurences e.g. [4, 1], [5], [3, 2], [3, 1, 1], [1, 1, 1, 1, 1]...
    values = sorted(list(card_dict.values()), reverse=True)
    if len(values) == 0:
        values.append(0)

    values[0] += numJokers
    
    # Check for types
    if len(values) == 1:
        return HAND_TYPE_FIVEOF
    
    if len(values) == 2 and values[0] == 4:
        return HAND_TYPE_FOUROF
    
    if len(values) == 2 and values[0] == 3 and values[1] == 2:
        return HAND_TYPE_FULLHOUSE
    
    if len(values) == 3 and values[0] == 3:
        return HAND_TYPE_THREEOF
    
    if len(values) == 3 and values[0] == 2 and values[1] == 2:
        return HAND_TYPE_TWOPAIR
    
    if len(values) == 4:
        return HAND_TYPE_ONEPAIR
    
    return HAND_TYPE_HIGHCARD

def compareHands(hand1: list, hand2: list) -> bool:
    handType1 = getHandType(hand1)
    handType2 = getHandType(hand2)

    if handType1 < handType2: return 1
    elif handType1 > handType2: return -1

    for i in range(5):
        card1 = hand1[i]
        card2 = hand2[i]

        if card1 > card2: return 1
        elif card1 < card2: return -1

    return 0