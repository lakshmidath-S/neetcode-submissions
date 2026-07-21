class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target=len(cost)
        dp1=0
        dp2=0
        for i in range(target-1,-1,-1):
            dp3=cost[i]+min(dp2,dp1)
            dp1=dp2
            dp2=dp3
        return min(dp1,dp2)