class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count=numBottles
        if numExchange>numBottles:
            return count
        elif numExchange==numBottles:
            return count+1
        while numBottles>=numExchange:
            numBottles-=numExchange
            numBottles+=1
            count+=1
        return count