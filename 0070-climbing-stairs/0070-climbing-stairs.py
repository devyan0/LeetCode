class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(maxsize=1000)
        def dp(k):
            if k <= 0: return 1
            if k == 1: return 1
            
            return dp(k-1) + dp(k-2)
        
        return dp(n)