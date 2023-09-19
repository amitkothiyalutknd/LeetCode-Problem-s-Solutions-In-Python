# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
import math
class Solution:
    def findMedianSortedArrays(self, array1: list[int], array2: list[int]) -> float:
        mergedArray = (array1 + array2)
        mergedArray.sort()
        if len(mergedArray) % 2 == 0:
            midElement1 = int((len(mergedArray) / 2) - 1)
            midElement2 = midElement1 + 1
            print(f"The Median Of Two Merged Sorted Array Is: {(mergedArray[midElement1] + mergedArray[midElement2]) / 2}.")
        else:
            midElement = int((math.ceil(len(mergedArray) / 2) - 1))
            print(f"The Median Of Two Merged Sorted Array Is: {mergedArray[midElement]}.")

sol = Solution()
array1 = list(map(int, input("Enter Multiple Elements To Be Insert In First Arrays. Seperate Each Inputs from Single Space.:\t").split(' ')))
array2 = list(map(int, input("Enter Multiple Elements To Be Insert In First Arrays. Seperate Each Inputs from Single Space.:\t").split(' ')))
sol.findMedianSortedArrays(array1, array2)