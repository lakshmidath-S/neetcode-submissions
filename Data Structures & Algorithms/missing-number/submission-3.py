class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)