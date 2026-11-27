class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=start^goal
        return bin(x).count('1')
