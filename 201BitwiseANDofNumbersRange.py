# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

# Example 1:
# Input: left = 5, right = 7
# Output: 4

# Example 2:
# Input: left = 0, right = 0
# Output: 0

# Example 3:
# Input: left = 1, right = 2147483647
# Output: 0

class Solution:
    def andFun(self, num1, num2):
        bnum1, bnum2 = int(bin(num1)[2:]), int(bin(num2)[2:])
        result = bnum1 & bnum2
        print(bin(result), type(result))
        return result

sol = Solution()
num1 = int(input("Enter The First Integer Number: "))
num2 = int(input("Enter The Second Integer Number: "))
print(f"The Bitwise AND Of All Numbers In The Range [{num1}, {num2}] is: {sol.andFun(num1, num2)}")