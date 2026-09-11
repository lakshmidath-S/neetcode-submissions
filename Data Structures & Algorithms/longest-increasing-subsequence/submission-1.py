class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n-1:
            if nums[i]<nums[i+1]:
                i+=1
            else:
                break
        if i==n-1:
            return n
        dp=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[i],1+dp[j])
        return max(dp)