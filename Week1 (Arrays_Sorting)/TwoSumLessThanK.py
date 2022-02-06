"""
https://leetcode.com/problems/two-sum-less-than-k/

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] +
nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

"""

# Using two pointers approach
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = -1
        for p in range(len(nums)):
            left, right = p, len(nums)-1
            while left < right:
                if nums[left] + nums[right] >= k:
                    right -= 1
                else:
                    res = max(res,nums[left]+nums[right])
                    left += 1
        return res