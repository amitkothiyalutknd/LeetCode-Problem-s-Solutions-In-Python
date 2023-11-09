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
from collections import defaultdict
import bisect
class Solution:
    def fourSum(self, nums, target):
        nums, hmap, quadruplets = sorted(nums), defaultdict(int), []
        for index1 in range(len(nums) - 3):
            if index1 > 0 and nums[index1] == nums[index1 - 1]:
                continue
            for index2 in range(index1 + 1, len(nums) - 2):
                for index3 in range(index2 + 1, len(nums) - 1):
                    sums = target - (nums[index1] + nums[index2] + nums[index3])
                    idx = bisect.bisect_left(nums[index3 + 1:len(nums)], sums)
                    if index3 + idx + 1 < len(nums) and nums[index3 + idx + 1] == sums:
                        lis = [nums[index1], nums[index2], nums[index3], nums[index3+idx+1]]
                        temp = ''.join(map(str, lis))
                        if hmap[temp] == 0:
                            quadruplets.append(lis)
                            hmap[temp] = 1
        return quadruplets

sol = Solution()
nums = []
NoOfelements = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
for index in range(NoOfelements):
    element = int(input(f"Enter The {index+1} Elements To Be Insert In A List: "))
    nums.append(element)
target = int(input("Enter The Number As A Target For Sum of Any Four Elements Of The List: "))
print(f"The List Of Quadruplets Which Values Sum Are Same As Target: {target} From Given Input: {nums} is:\t", sol.fourSum(nums, target))