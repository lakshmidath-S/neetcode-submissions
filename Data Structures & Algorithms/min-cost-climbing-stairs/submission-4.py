class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost=0
        target=len(cost)
        dp=[float('inf')]*(target)
        def climber(i):
            if i>=target:
                return 0
            else:
                if dp[i]!=float('inf'):
                    return dp[i]
                else:
                    dp[i]=cost[i]+min(climber(i+1),climber(i+2))
                    return dp[i]
        return min(climber(0),climber(1))
