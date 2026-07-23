class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=(m*n-1)
        while i<=j:
            mid=(i+j)//2
            row=mid//n
            col=mid%n
            midval=matrix[row][col]
            if midval==target:
                return True
            elif midval>target:
                j=mid-1
            elif midval<target:
                i=mid+1
        return False


