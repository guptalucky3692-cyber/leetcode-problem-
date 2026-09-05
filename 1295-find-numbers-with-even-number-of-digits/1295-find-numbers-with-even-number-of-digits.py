class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            n = len(str(nums[i]))
            if n%2==0:
                s+=1
        return s



        