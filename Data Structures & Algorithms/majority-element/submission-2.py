from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=0
        count=0
        for i in nums:
            if count==0:
                candidate=i
            if i==candidate:
                count+=1
            else:
                count-=1
        return candidate
        