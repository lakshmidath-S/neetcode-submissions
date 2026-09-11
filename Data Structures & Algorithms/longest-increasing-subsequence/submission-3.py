class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for i in nums:
            pos=0
            while pos<len(dp) and dp[pos]<i:
                pos+=1
            if pos==len(dp):
                dp.append(i)
            else :
                dp[pos]=i

        return len(dp)

            