class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        if len(nums)==1:
            return nums[0]
        def value(i):
            if dp[i]==0:
                if i<=len(nums)-3:
                    dp[i]=max(nums[i]+value(i+2),value(i+1))
                elif i==len(nums)-2:
                    dp[i]=max(nums[i],value(i+1))
                elif i==len(nums)-1:
                    dp[i]=nums[i]
            return dp[i]
        return (value(0))