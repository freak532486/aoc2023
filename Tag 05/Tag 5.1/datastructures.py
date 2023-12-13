from utils import *

class Interval:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi

    def contains(self, x: int):
        return x >= self.lo and x <= self.hi

    def __repr__(self):
        return f"[{self.lo}, {self.hi}]"
    

class Mapping:
    def __init__(self, src, dst, range):
        self.src   = src
        self.dst   = dst
        self.range = range

    def map(self, x: int):
        if x < self.src or x >= self.src + self.range:
            return None
        
        return self.dst + (x - self.src)
    
    def src_ival(self):
        return Interval(self.src, self.src + self.range - 1)
    
    def offset(self):
        return self.dst - self.src
    
    def __repr__(self):
        return f"[{self.src}..{self.src+self.range} -> {self.dst}..{self.dst + self.range} ]"
    