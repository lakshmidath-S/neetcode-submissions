class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        summ=prices[0]+prices[1]
        if summ>money:
            return money
        else:
            return money-summ