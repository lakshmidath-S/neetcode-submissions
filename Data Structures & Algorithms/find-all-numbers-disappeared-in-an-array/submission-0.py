class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        ans=[]
        while i<len(nums):
            if i+1 not in nums:
                ans.append(i+1)
            i+=1
        return ans
