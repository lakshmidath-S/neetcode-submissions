class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        a=set()
        while(i<len(nums)):
            if nums[i] in a:
                return True
            a.add(nums[i])
            if len(a)>k:
                a.remove(nums[i-k])
            i+=1
        return False