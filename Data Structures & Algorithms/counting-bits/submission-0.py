class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(n+1):
            arr.append(i)
        for i in range(n+1):
            count=0
            while arr[i]:
                arr[i]&=(arr[i]-1)
                count+=1
            arr[i]=count
        return arr