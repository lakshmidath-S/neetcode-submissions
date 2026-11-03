class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sum=0
        i=0
        while i<n:
            sum+=mat[i][i]
            i+=1
        j=i-1
        i=0
        while j>-1: 
            if i!=j:
                sum+=mat[i][j]
            i+=1
            j-=1
        return sum