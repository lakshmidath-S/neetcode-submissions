class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j=1
        maxx=nums[0]
        curr=nums[0]
        while j<len(nums):
            curr = max(nums[j], curr + nums[j])
            maxx=max(maxx,curr)
            j+=1
        return maxx