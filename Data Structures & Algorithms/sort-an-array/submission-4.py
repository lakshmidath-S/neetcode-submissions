class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n,i):
            largest=i
            left=i*2+1
            right=i*2+2
            if left<n and nums[left]>nums[largest]:
                largest=left
            if right<n and nums[right]>nums[largest]:
                largest=right
            if i!=largest:
                nums[i],nums[largest]=nums[largest],nums[i]
                heapify(n,largest)
        n=len(nums)
        for i in range(n//2-1,-1,-1):
            heapify(n,i)
        for i in range(n-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            heapify(i,0)
        return nums
