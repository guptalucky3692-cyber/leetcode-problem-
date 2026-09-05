class Solution:
    def maxProduct(self, n: int) -> int:
        x = sorted([int(d) for d in str(n)],reverse=True)
        return x[0]*x[1]

        