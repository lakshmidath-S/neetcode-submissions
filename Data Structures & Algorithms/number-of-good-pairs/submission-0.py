import math
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        freq=Counter(nums)
        for i,j in freq.items():
            if j>1:
                count+=math.comb(j,2)
        return count
