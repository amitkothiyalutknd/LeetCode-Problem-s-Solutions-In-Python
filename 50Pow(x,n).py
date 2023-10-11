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
        result = 1
        for i in range(abs(powofNumber)):
            result = result*number
        if powofNumber < 0:
            result = 1/result
        return round(result, 5)

sol = Solution()
number = eval(input("Enter The Number: "))
powofNumber = eval(input("Enter The Power Of Number To Be Calculate: "))
print(f"The Result of Power {powofNumber} of Number {number} is :", sol.numPow(number, powofNumber))