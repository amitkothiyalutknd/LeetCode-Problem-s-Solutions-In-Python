# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for number in nums:
            if nums.count(number) == 1:
                return number

sol = Solution()
noOfElement = int(input("Enter The Total Number Of Elements To Be Insert In An Array: "))
nums = list(map(int, input(f"Enter The Total {noOfElement} Numbers For An Array. Seperate Each Input From Single Space: ").strip().split()))[:noOfElement]
print(f"List Of Distinct Numbers In An Array {nums} is:\t", sol.singleNumber(nums))