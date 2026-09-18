class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}
        def back(i,curr):
            if (i,curr) in dp:
                return dp[(i,curr)]
            if i==n:
                if curr==target:
                    return 1
                else:
                    return 0
            if (i+1,curr+nums[i]) not in dp:
                dp[(i+1,curr+nums[i])]=back(i+1,curr+nums[i])
            if (i+1,curr-nums[i]) not in dp:
                dp[(i+1,curr-nums[i])]=back(i+1,curr-nums[i])
            return dp[(i+1,curr+nums[i])]+dp[(i+1,curr-nums[i])]
            
        return back(0,0)
