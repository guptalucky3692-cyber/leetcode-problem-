class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        s = len(arr)
        t = 0
        for i in range(s):
            for j in range(i+1,s):
                for k in range(j+1,s):
                    if abs(arr[i]-arr[j])<=a and abs(arr[i]-arr[k])  <=c and abs(arr[j]-arr[k])<=b:
                        t+=1
        return t
        