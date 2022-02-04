"""
https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
closest to target.

Return the sum of the three integers.

"""

# Using two pointers approach
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums = sorted(nums)
        for p in range(len(nums)):
            left, right = p + 1, len(nums) - 1
            while left < right:
                t_sum = nums[p] + nums[left] + nums[right]
                if abs(t_sum - target) < abs(res - target):
                    res = t_sum
                if t_sum > target:
                    right -= 1
                if t_sum < target:
                    left += 1
                if t_sum == target:
                    return target
        return res