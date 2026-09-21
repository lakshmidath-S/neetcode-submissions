class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=nums[:]
        for i in nums:
            a.append(i)
        return a