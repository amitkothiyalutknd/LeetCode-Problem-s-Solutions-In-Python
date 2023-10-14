# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
class Solution:
    def numPow(self, number: float, powofNumber: int) -> float:
        try:
            result = number**(abs(powofNumber))
            if powofNumber < 0:
                result = 1/result
            return result
        except OverflowError as e:
            return 0

sol = Solution()
number = eval(input("Enter The Number: "))
powofNumber = eval(input("Enter The Power Of Number To Be Calculate: "))
if sol.numPow(number, powofNumber) == 0:
    print("Result Getting To Much Large Or Out Of Integer Range. Getting Arithmetic Error.")
else:
    print(f"The Result of Power: {powofNumber} of Number: {number} is :", sol.numPow(number, powofNumber))