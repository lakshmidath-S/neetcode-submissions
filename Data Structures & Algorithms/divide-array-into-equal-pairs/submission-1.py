from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for i,j in freq.items():
            if j%2!=0:
                return False
        return True