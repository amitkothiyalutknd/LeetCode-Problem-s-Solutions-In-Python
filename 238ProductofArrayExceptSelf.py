# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from functools import *
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        preProduct, postProduct, result = 1, 1, [0] * len(nums)
        for index in range(len(nums)):
            result[index] = preProduct
            preProduct *= nums[index]
        for index in range(len(nums)-1, -1, -1):
            result[index] *= postProduct
            postProduct *= nums[index]
        return result
#=============================================2nd Method=============================================
        # output, nums = tuple(), tuple(nums)
        # for index, value in enumerate(nums):
        #     toExlude = (index,)
        #     temp = [value for index, value in enumerate(nums) if index not in toExlude]
        #     output = output + (reduce(lambda a,b: a*b, temp),)
        # return list(output)
sol = Solution()
nums = list(map(int, input(f"Enter The Numbers Of An Array. Seperate Each Input From Single Space: ").strip().split()))[:]
print(f"Product of Array Except Self is:\t", sol.productExceptSelf(nums))