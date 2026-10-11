from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        ans=[]
        for i in freq:
            if freq[i]==i:
                ans.append(i)
        return max(ans)if ans else -1