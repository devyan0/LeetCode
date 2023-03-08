class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        
        def can_eat_in(abil):
            t = 0
            for n in piles:
                t += ceil(n/abil)
            return t
        
        l, r = 1, max(piles)+1
        while l < r:
            m = (l+r)//2
            if can_eat_in(m) <= h:
                r = m
            else:
                l = m + 1
                
        return l if l <= max(piles) else max(piles)