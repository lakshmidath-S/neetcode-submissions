class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)+1
        for i in nums:
            sum+=i
        return int((n*(n-1))/2)-sum

