# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
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
        rev = ""
        for digit in reversed(str(abs(nums))):
            rev += digit
        if nums < 0:
            rev = "-" + rev
        if int(rev).bit_length() <= 32:
            return int(rev)
        else:
            print("The Reversing Of Input Causeing The Value To Go Outiside The Signed 32-bit Integer Range.")

sol = Solution()
integer = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
print(f"The Output Of Given Input: {integer} is:\t", sol.reverse(integer))