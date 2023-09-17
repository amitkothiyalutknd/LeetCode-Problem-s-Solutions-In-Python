# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
from itertools import chain
class solution:
    def __init__(self):
        self.inputList = list(map(int, input(f"Enter Multiple Numbers To Be Insert In List. Seperate Each Inputs From Single Space.: ").split(' ')))
           
    def twoSum(self, inputList, targetNumber):
        print(f"\nThe InputList is: {self.inputList} & Target Sum of Two Elements is: {targetNumber}.")
        print(f"The Index of Eligible Elements for Desired Output is: {str(list(chain.from_iterable([list((i, i + 1)) for i in range(len(self.inputList) - 1) if self.inputList[i] + self.inputList[i + 1] == targetNumber])))}")
        
inputList = solution()  
targetNumber = int(input("Enter The Target Number As A Result Of Sum Of Two Numbers In A list: "))
inputList.twoSum(inputList, targetNumber)