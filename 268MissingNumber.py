# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
class Solution():
    def missingNumber(self, nums) -> int:
        for i in range(len(nums)+1):
            print(i)
            if i not in nums:
                return i
            else:
                continue

sol = Solution()
noOfElement = int(input("Enter The Total Number Of Elements To Be Insert In An Array: "))
nums = list(map(int, input(f"Enter The Total {noOfElement} Numbers For An Array. Seperate Each Input From Single Space: ").strip().split()))[:noOfElement]
print(f"Missing Number In Array {nums} is:\t", sol.missingNumber(nums))