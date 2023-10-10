# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
 
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
class Solution:
    def fourSum(self, nums, target):
        index1, output, listing = 0, [0] * 4, []
        nums.sort()
        while index1 < (len(nums) - 3):
            index2 = index1 + 1
            while index2 < (len(nums)):
                index3 = index2 + 1
                while index3 < (len(nums)):
                    index4 = index3 + 1
                    while index4 < (len(nums)):
                        if (nums[index1] + nums[index2] + nums[index3] + nums[index4] == target) and (index1 != index2 and index3 and index4) and (index2 != index3 and index4) and (index3 != index4):
                            output[0], output[1], output[2], output[3] = nums[index1], nums[index2], nums[index3], nums[index4]
                            if output not in listing:
                                listing.append(output[:])
                        index4 = index4 + 1
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
target = int(input("Enter The Number As A Target For Sum of Any Four Elements Of The List: "))
print(f"The List Of Numbers Which Values Sum Are Same As Target: {target} From Given Input: {nums} is:\t", sol.fourSum(nums, target))