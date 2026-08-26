class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end=0
        furthest=0
        jump=0
        for i in range(len(nums)-1):
            furthest=max(furthest,i+nums[i])
            if i==cur_end:
                jump+=1
                cur_end=furthest
        return jump