"""
https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You
must also not convert the inputs to integers directly.

"""

# Using hashmap
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_res, num2_res = 0, 0
        num_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        for num in num1:
            num1_res = num1_res * 10 + num_dict[num]
        for num in num2:
            num2_res = num2_res * 10 + num_dict[num]
        return str(num1_res + num2_res)

# Using ord
