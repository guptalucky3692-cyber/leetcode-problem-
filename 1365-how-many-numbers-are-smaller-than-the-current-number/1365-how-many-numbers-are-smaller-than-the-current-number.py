class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t =[]
        for i in nums:
            count=0
            for j in nums:
                if i>j:
                    count+=1
            t.append(count)
        return t


        