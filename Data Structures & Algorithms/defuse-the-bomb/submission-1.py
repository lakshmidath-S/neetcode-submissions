class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        arr=[0]*n
        if k==0:
            arr
        for i in range(n):
            if k>0:
                for j in range(1,k+1):
                    arr[i]+=code[(i+j)%n]
            else:
                for j in range(1,abs(k)+1):
                    arr[i]+=code[(i-j)%n]
        return arr