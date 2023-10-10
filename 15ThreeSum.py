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
    def threeSum(self, nums):
        index1, output, listing = 0, [0] * 3, []
        nums.sort()
        while index1 < (len(nums) - 2):
            index2 = index1 + 1
            while index2 < (len(nums)):
                index3 = index2 + 1
                while index3 < (len(nums)):
                    if (nums[index1] + nums[index2] + nums[index3] == 0) and (index1 != index2) and (index1 != index2) and (index2 != index3):
                        output[0], output[1], output[2] = nums[index1], nums[index2], nums[index3]
                        if output not in listing:
                            listing.append(output[:])
                    index3 = index3 + 1
                index2 = index2 + 1
            index1 = index1 + 1
        return listing

sol = Solution()
nums = []
NoOfelements = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
for index in range(NoOfelements):
    element = int(input(f"Enter The {index+1} Elements To Be Insert In A List: "))
    nums.append(element)
print(f"The Output Of Given Input: {nums} is:\t", sol.threeSum(nums))