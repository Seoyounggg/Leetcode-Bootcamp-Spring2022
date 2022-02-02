"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = -1 * nums[i]

            while left < right:
                if nums[left] + nums[right] == target:
                    res.add((nums[left], nums[right], nums[i]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return map(list, res)