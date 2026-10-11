from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        return max((i for i in freq if freq[i]==i),default=-1)