class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            middle=(i+j)//2
            if nums[middle]<target:
                i=middle+1
            else:
                j=middle-1
        return i
