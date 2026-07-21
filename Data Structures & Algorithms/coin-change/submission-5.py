class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=[-1]*(amount+1)
        def ways(target):
            if target==0:
                dp[target]=0
                return dp[target]
            if target in coins:
                dp[target]=1
                return 1
            if target<0:
                return float('inf')
            if dp[target]!=-1:
                return dp[target]
            else:
                dp[target]=1+min(ways(target-i) for i in coins)
                return dp[target]
        ans=ways(amount)
        return -1 if ans==float('inf') else ans
            