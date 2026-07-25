class Solution:
    def reverseBits(self, n: int) -> int:
        a=0
        for _ in range(32):
            last_bit=n&1
            n=n>>1
            a=a<<1
            a=a|last_bit
        return int(a)
        