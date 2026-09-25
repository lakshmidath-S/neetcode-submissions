class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        ans=[]
        stack=[]
        for i in nums2:
            if not stack or stack[-1]>i:
                stack.append(i)
            else:
                while len(stack)!=0 and stack[-1]<i:
                    a=stack.pop()
                    freq[a]=i
                stack.append(i)


        for i in nums1:
            if i in freq:
                ans.append(freq[i])
                continue
            ans.append(-1)
        return ans

                