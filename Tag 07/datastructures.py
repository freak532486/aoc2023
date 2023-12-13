from utils import *

class HandBidPair:
    def __init__(self, hand: list, bid: int):
        self.hand = hand
        self.bid  = bid

    def __repr__(self):
        return f"Hand {handToStr(self.hand)} with bid {self.bid}"