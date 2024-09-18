# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
import sys

class Solution:
    def maxSubArray(self, mainArray) -> int:
        # maximum = -sys.maxsize - 1
        # maxSum = 0
        # for index in range(len(mainArray)):
        #     maxSum = maxSum + mainArray[index]
        #     maximum = max(maxSum, maximum)
        #     if (maxSum < 0):
        #         maxSum = 0
        # return maximum

# --------------------------------------------------2nd Approach------------------------------------
        maximum = -sys.maxsize - 1
        maxSum = 0
        for value in mainArray:
            maxSum = max(value, maxSum + value)
            maximum = max(maxSum, maximum)
        return maximum

sol = Solution()
mainArray = list(map(int, input("Enter The Values Inside A list. Separate Each Inputs from Single Space.: ").split(' ')))
print(f"The Sum Of Final Maximum SubArray: {sol.maxSubArray(mainArray)}")