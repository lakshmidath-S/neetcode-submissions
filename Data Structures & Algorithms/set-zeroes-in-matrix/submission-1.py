class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        a=set()
        def setz():
            for i,j in a:
                for k in range(n):
                    matrix[k][j]=0
                for k in range(m):
                    matrix[i][k]=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    a.add((i,j))
        setz()
        

