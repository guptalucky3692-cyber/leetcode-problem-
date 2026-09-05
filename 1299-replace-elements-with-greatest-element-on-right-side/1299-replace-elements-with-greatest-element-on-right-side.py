class Solution(object):
    def replaceElements(self, arr):
        curr = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i],curr = curr,max(arr[i],curr)
        return arr

        """
        :type arr: List[int]
        :rtype: List[int]
        """

        