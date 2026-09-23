class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat=[[]for _ in range(numRows)]
        for i in range(numRows):
            value=1
            for j in range(i+1):
                mat[i].append(value)
                value=value*(i-j)//(j+1)
        return mat
            