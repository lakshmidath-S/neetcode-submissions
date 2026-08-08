class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def robber(nums):
            a=0
            b=0
            for i in nums:
                curr=max(a,b+i)
                b=a
                a=curr
            return a
        return max(robber(nums[1:]),robber(nums[:-1]))
            