class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums))
        def value(i):
            if i >= len(nums):
                return 0
            elif dp[i]==-1:
               dp[i]=max(nums[i]+value(i+2),value(i+1))
            return dp[i]
        return value(0)