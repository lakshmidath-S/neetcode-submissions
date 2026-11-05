class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves=0
        seats.sort()
        students.sort()
        i=0
        while i<len(seats):
            if seats[i]!=students[i]:
                moves+=abs(seats[i]-students[i])
            i+=1
        return moves
