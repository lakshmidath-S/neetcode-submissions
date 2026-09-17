class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2==1:
            return False
        target=total//2
        n=len(nums)
        def back(i,curr):
            if curr==target:
                return True
            if i==n or curr>target:
                return False
            if back(i+1,curr+nums[i]):
                return True
            return back(i+1,curr)
        return back(0,0)
