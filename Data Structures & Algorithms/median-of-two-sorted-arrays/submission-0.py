class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new= nums1+nums2
        l,r= 0, len(new)-1
        mid=(l+r)//2
        return mid   