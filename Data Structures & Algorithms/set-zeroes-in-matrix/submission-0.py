class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        a=set()
        def setz():
            for i,j in a:
                for k in range(i,n):
                    matrix[k][j]=0
                for k in range(i,-1,-1):
                    matrix[k][j]=0
                for k in range(j,m):
                    matrix[i][k]=0
                for k in range(j,-1,-1):
                    matrix[i][k]=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    a.add((i,j))
        setz()
        

