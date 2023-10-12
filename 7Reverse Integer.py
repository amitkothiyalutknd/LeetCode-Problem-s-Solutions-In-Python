# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
class Solution:
# -----------------------------------1st Method-------------------------------------------------
    # def reverse(self, nums):
        # rev, temp = 0, abs(nums)
        # while temp > 0:
        #     rev = (rev * 10) + (temp % 10)
        #     temp = temp//10
        # if nums < 0:
        #     return -abs(rev)
        # else:
        #     return rev
# -----------------------------------2nd Method-------------------------------------------------
    def reverse(self, nums):
        maxInt = 2 ** 31 - 1 # 2,147,483,647
        rev = "0"
        for digit in reversed(str(abs(nums))):
            if int(rev) > maxInt / 10:
                print("The Reversing Of Input Causeing The Value To Go Outiside The Signed 32-bit Integer Range.")
            else:
                rev += digit
        if nums < 0:
            rev = "-" + rev
        return int(rev)

sol = Solution()
integer = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
print(f"The Output Of Given Input: {integer} is:\t", sol.reverse(integer))