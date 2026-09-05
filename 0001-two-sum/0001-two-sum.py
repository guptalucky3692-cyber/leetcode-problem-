class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        df ={}
        for i in range(0,n):
            remaing = target - nums[i]
            if remaing in df:
                return [df[remaing],i]
            df[nums[i]] = i
            
        