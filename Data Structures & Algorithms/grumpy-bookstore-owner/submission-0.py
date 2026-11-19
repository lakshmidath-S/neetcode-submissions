class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                satisfied+=customers[i]
        max_additional=0
        for i in range(minutes):
            if grumpy[i]:
                max_additional+=customers[i]
        curr_max=max_additional
        for j in range(minutes,len(grumpy)):
            if grumpy[j]:
                curr_max+=customers[j]
            if grumpy[j-minutes]:
                curr_max-=customers[j-minutes]
            max_additional=max(max_additional,curr_max)
        return satisfied+max_additional
