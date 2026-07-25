class Solution:
    def reverseBits(self, n: int) -> int:
        bits=format(n,"032b")
        bits=bits[::-1]
        return int(bits,2)