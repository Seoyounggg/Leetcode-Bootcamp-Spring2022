"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for idx in range(len(nums)):
            comp = target - nums[idx]

            if comp in prev:
                return [prev[comp],idx]
            else:
                prev[nums[idx]] = idx