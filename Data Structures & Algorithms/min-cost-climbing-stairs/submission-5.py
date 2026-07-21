class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target=len(cost)
        dp1=cost[0]
        dp2=cost[1]
        for i in range(2,target):
            dp3=cost[i]+min(dp2,dp1)
            dp1=dp2
            dp2=dp3
        return min(dp1,dp2)
