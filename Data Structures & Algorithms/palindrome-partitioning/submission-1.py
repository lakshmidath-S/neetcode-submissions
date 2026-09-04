class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])


        def back(idx,curr):
            if idx==n:
                ans.append(curr[:])
                return 
            for j in range(idx,n):
                if dp[idx][j]:
                    curr.append(s[idx:j+1])
                    back(j+1,curr)
                    curr.pop()
        back(0,[])
        return ans
            
        