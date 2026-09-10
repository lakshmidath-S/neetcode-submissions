class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        top=0
        bottom=n
        left=0
        right=m
        arr=[]
        while top<bottom and left<right:
            for p in range(left,right):
                arr.append(matrix[top][p])
            for p in range(top+1,bottom):
                arr.append(matrix[p][right-1])
            if top+1<bottom:
                for p in range(right-2,left-1,-1):
                    arr.append(matrix[bottom-1][p])
            if right>left+1:
                for p in range(bottom-2,top,-1):
                    arr.append(matrix[p][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        if top+1==bottom:
            for p in range(left,right):
                arr.append(matrix[top][p])
        elif left+1==right:
            for p in range(top,bottom):
                arr.append(matrix[p][left])
        return arr