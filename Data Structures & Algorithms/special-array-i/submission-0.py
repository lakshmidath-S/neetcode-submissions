class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def isodd(num):
            if num%2==1:
                return True
            return False
        for i in range(len(nums)-1):
            if isodd(nums[i]) and isodd(nums[i+1]):
                return False
            elif not isodd(nums[i]) and not isodd(nums[i+1]):
                return  False
        return True