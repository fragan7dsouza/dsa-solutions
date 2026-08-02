class Solution:
    def rob(self, nums: List[int]) -> int:
        s= sorted(nums)
        ans= max(s)
        return ans