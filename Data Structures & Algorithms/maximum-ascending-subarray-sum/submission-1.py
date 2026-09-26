class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum=0
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr+=nums[i]
            else:
                sum=max(sum,curr)
                curr=nums[i]
            sum=max(sum,curr)
        return sum
