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
        nums, listing = sorted(nums), []
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while left<right:
                sums = nums[index] + nums[left] + nums[right]
                if (nums[index] + nums[left] + nums[right] == 0) and (index != left) and (index != right) and (left != right):
                    if [nums[index], nums[left], nums[right]] not in listing:
                        listing.append([nums[index], nums[left], nums[right]])
                if sums < 0:
                    left +=1
                else:
                    right -=1
        return listing

sol = Solution()
NoOfelements = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
nums = []
for index in range(NoOfelements):
    element = int(input(f"Enter The {index+1} Elements To Be Insert In A List: "))
    nums.append(element)
print(f"The List Of Quadruplets Which Values Sum Is 0 From Given Input: {nums} is:\t", sol.threeSum(nums))