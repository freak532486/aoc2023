class Interval:
    def __init__(self, lo: int, hi: int):
        self.lo = lo
        self.hi = hi

    def __repr__(self):
        return f"[{self.lo}, {self.hi}]"
    
class IntervalPair:
    def __init(self, src: Interval, dst: Interval):
        self.src = src
        self.dst = dst