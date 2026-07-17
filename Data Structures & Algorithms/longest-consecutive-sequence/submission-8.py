class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq={}
        maxseq=1
        temp=1
        if len(nums)<2:
            return len(nums)
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        i=0
        while(i<len(nums)):
            if nums[i]+1 in freq and nums[i]-1 not in freq:
                temp=1
                while nums[i]+temp in freq:
                    temp+=1
                maxseq=max(maxseq,temp)
            i+=1        
        return maxseq
