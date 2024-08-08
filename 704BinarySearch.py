# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

import math

class Solution:
    def search(self, listValues, target: int) -> int:
        listValues.sort()
        start, end = 0, len(listValues) - 1
        mid = math.ceil((start+end)/2)
        while(start<=end):
            if listValues[mid] == target:
                return mid
            elif listValues[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            mid = math.ceil((start+end)/2)
        return -1
        
sol = Solution()
listValues = list(map(int, input("Enter Multiple Elements To Be Insert In List. Separate Inputs from Single Space.:\t").split(' ')))
target = int(input("Enter The Target Number To Be Search: "))
print(sol.search(listValues, target))