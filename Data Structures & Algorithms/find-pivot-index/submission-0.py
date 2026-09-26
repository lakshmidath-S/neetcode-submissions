class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=sum(nums)
        left=0
        for i in range(len(nums)):
            right=a-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1
