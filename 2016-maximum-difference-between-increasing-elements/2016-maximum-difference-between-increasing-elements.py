class Solution(object):
    def maximumDifference(self, nums):
        if nums[::-1]==sorted(nums):
            return -1
        else:
            a = []
            l = len(nums)
            for i in range(l):
                for j in range(i,l):
                    a.append(nums[j]-nums[i])
            return max(a)

        """
        :type nums: List[int]
        :rtype: int
        """
        