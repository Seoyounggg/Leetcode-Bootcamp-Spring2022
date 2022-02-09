"""
https://leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.

"""

# Using list
class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        i = 0
        ans = []

        while num > 0:
            n = num % 10
            if 1 <= n <= 3:
                ans.append(ones[i] * n)
            elif n == 4:
                ans.append(ones[i] + fives[i])
            elif 5 <= n <= 8:
                ans.append(fives[i] + ones[i] * (n - 5))
            elif n == 9:
                ans.append(ones[i] + ones[i + 1])
            i += 1
            num //= 10

        return ''.join(i for i in ans[::-1])


# Using list of tuples
class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
                  ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
                  ('IV', 4), ('I', 1)]
        res = []

        for symbol, value in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            res.append(symbol * count)
        return "".join(res)

