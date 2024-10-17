class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minm = len(nums) + 1
        left = 0
        tot = 0
        
        for i in range(len(nums)):
            tot += nums[i]
            while tot >= target:
                minm = min(minm, i - left + 1)
                tot -= nums[left]
                left += 1
        
        if minm > len(nums):
            return 0
        return minm