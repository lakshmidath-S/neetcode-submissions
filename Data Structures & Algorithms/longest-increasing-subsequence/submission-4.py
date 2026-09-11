class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for i in nums:
            left=0
            right=len(dp)
            while left<right:
                mid=(left+right)//2
                if dp[mid]<i:
                    left=mid+1
                else:
                    right=mid
            if left==len(dp):
                dp.append(i)
            else :
                dp[left]=i

        return len(dp)

            