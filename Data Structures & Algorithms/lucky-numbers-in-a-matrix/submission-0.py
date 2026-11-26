class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        def isrow(num,i):
            for j in range(m):
                if num>matrix[i][j]:
                    return False
            return True
        def iscol(num,i):
            for j in range(n):
                if num<matrix[j][i]:
                    return False
            return True
        ans=[]
        for i in range(n):
            for j in range(m):
                if  isrow(matrix[i][j],i) and iscol(matrix[i][j],j):
                    ans.append(matrix[i][j])
        return ans
