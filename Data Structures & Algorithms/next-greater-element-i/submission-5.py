class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        ans=[]
        for i in range(len(nums2)):
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    if nums2[i] not in freq:
                        freq[nums2[i]]=[nums2[j]]
                        break
        for i in nums1:
            if i in freq:
                ans.append(freq[i][0])
                continue
            ans.append(-1)
        return ans

                