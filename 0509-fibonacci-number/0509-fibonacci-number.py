class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return [0, 1][n]
        
        slow, fast = 0, 1
        for _ in range(n-1):
            fast, slow = fast + slow, fast
            
        return fast
            