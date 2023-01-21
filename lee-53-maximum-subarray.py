class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            mx = max(mx, nums[i])
        return mx
