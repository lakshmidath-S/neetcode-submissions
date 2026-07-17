class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<1:
            return 0
        maxseq=1
        temp=1
        for i in  range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                temp+=1
            elif nums[i]==nums[i+1]:
                continue
            elif nums[i]+1!=nums[i+1]:
                temp=1
                continue
            maxseq=max(maxseq,temp)
        return maxseq