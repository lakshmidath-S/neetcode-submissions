class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(i,j,target):
            if i>j :
                return -1
            mid=int((i+j)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return binary(i,mid-1,target)
            else:
                return binary(mid+1,j,target)
        return binary(0,len(nums)-1,target)