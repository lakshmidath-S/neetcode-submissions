class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2==1:
            return False
        target=total//2
        n=len(nums)
        memo={}
        def back(i,curr):
            if curr==target:
                return True
            if i==n or curr>target:
                return False
            if (i,curr) in memo:
                return memo[(i,curr)]
            result=back(i+1,curr+nums[i]) or back(i+1,curr)
            memo[(i,curr)]=result
            return result
        return back(0,0)
