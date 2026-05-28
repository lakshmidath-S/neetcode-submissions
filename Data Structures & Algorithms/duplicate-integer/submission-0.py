class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
                flag=True
            else:
                freq[x]=1
        return flag