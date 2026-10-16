class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a=set()
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.add(i)
        return len(a)==0