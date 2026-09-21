class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        malen=0
        curr=0
        for i in nums:
            if i==1:
                curr+=1
            else:
                malen=max(curr,malen)
                curr=0
        return max(curr,malen)
