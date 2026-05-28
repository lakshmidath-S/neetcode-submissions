class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp=0
        for i in range(len(nums)):
            comp=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==comp:
                    return [i,j]