class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec=0
        inc=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                dec=1
            else:
                dec=0
                break
        for i in range(len(nums)-1,1,-1):
            if nums[i]>=nums[i-1]:
                inc=1
            else:
                inc=0
                break

        return dec==1 or inc==1
