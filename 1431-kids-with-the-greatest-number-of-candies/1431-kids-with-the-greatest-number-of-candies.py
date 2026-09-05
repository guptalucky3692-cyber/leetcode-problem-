class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s = []
        for i in candies:
            if i+extraCandies >= max(candies):
                s.append(True)
            else:
                s.append(False)
        return s
            
        