class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        def isPalindrome(ni,nj):
            while ni<nj:
                if s[ni]!=s[nj]:
                    return False
                ni+=1
                nj-=1
            return True

        def back(idx,curr):
            if idx==n:
                ans.append(curr[:])
                return 
            for j in range(idx,n):
                if isPalindrome(idx,j):
                    curr.append(s[idx:j+1])
                    back(j+1,curr)
                    curr.pop()
        back(0,[])
        return ans
            