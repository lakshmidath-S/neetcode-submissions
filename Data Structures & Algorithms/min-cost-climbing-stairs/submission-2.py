class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost=0
        target=len(cost)
        dp=[float('inf')]*(target+1)
        def climber(value,i):
            if i>=value:
                return 0
            else:
                if dp[i]!=float('inf'):
                    return dp[i]
                else:
                    dp[i]=cost[i]+min(climber(value,i+1),climber(value,i+2))
                    return dp[i]
        return min(climber(target,0),climber(target,1))
