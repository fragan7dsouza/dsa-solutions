class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new= nums1+nums2
        s= sorted(new)
        l,r= 0, len(s)-1
        mid=(l+r)//2
        return s[mid]