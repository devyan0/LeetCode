class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        slow = fast = 0
        for i in range(2, len(cost)+1):
            slow, fast = fast, min(slow+cost[i-2], fast+cost[i-1])
        
        return fast
            