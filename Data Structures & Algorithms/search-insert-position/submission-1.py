class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)
        while i<=j:
            middle=(i+j)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                if middle<len(nums)-1:
                    if nums[middle+1]>target:
                        return middle+1
                else:
                    return len(nums)

                i=middle+1
            else:
                j=middle-1
        return i
