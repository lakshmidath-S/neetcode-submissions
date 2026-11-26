class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        colmax={}
        rowmin={}
        for i in range(n):
            for j in range(m):
                a=matrix[i][j]
                if j in colmax:
                    if colmax[j]<a:
                        colmax[j]=a
                else:
                    colmax[j]=a
                if i in rowmin:
                    if rowmin[i]>a:
                        rowmin[i]=a
                else:
                    rowmin[i]=a
        def isrow(num,i):
            return num==rowmin[i]
        def iscol(num,i):
            return num==colmax[i]
        ans=[]
        for i in range(n):
            for j in range(m):
                if  isrow(matrix[i][j],i) and iscol(matrix[i][j],j):
                    ans.append(matrix[i][j])
        return ans
