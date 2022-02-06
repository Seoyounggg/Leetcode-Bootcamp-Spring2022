"""
https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
"""

# Using binary search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] - mid -1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k


# Using set
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = [i for i in range(1,arr[-1]+1+k)]
        ans = sorted(list(set(nums) - set(arr)))
        return ans[k-1]