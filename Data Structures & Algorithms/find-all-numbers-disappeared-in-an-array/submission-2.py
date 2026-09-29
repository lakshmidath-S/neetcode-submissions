class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=set(nums)
        ans=[]
        for i in range(len(nums)):
            if i+1 not in a:
                ans.append(i+1)
        return ans

