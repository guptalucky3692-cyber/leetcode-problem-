class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 +nums2
        arr.sort()
        total = len(arr)
        if total%2==1:
            return float(arr[total//2])
        else:
            arr1 = arr[total//2-1]
            arr2 = arr[total//2]
        return (float(arr1)+float(arr2))/2

        