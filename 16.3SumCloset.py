# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
import sys
class Solution:
    def threeSumCloset(self, nums, target) -> int:
        nums, closet = sorted(nums), sys.maxsize
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while left<right:
                sums = nums[index] + nums[left] + nums[right]
                if abs(target - sums) < abs(target - closet):
                    closet = sums 
                if sums < target:
                    left +=1
                else:
                    right -=1
        return closet                

sol = Solution()
noOfElement = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
nums = list(map(int, input(f"Enter Total {noOfElement} Numbers For Nums Array. Seperate Each Input From Single Space: ").strip().split()))[:noOfElement]
target = int(input("Enter The Number As Target To Be Sum Of Three Integer As Closet: "))
print(f"The Sum That Is Closet To The Target is:\t", sol.threeSumCloset(nums, target))