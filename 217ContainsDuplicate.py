# 217. ContainsDuplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containDuplicates(self, array) -> bool:
        arraySet = set(array)
        if len(arraySet) == len(array):
            return False
        else:
            return True

sol = Solution()
noOfElement = int(input("Enter The Total Number Of Elements To Be Insert In A List: "))
array = list(map(int, input(f"Enter The Total {noOfElement} Numbers For An Array. Seperate Each Input From Single Space: ").strip().split()))[:noOfElement]
print(f"Duplicates Exist In Array {array} is:\t", sol.containDuplicates(array))




