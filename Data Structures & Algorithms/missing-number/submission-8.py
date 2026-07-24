class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=0
        n=len(nums)+1
        for i in nums:
            total+=i
        return int((n*(n-1))/2)-total

