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
 
class Solution:
    def twoSum(self, inputList, targetNumber):
        outputList = []
        for i in range(len(inputList)):
            start = i + 1
            if start < len(inputList):
                for j in range(start, len(inputList)):
                    if inputList[i] + inputList[j] == targetNumber:
                        outputList.append(i)
                        outputList.append(j)
                        print(f"The Index of Eligible Elements for Desired Output is: {outputList}.")
                        break
        
sol = Solution()  
inputList = list(map(int, input(f"Enter Multiple Numbers To Be Insert In List. Seperate Each Inputs From Single Space.: ").split(' ')))
targetNumber = int(input("Enter The Target Number As A Result Of Sum Of Two Numbers In A list: "))
sol.twoSum(inputList, targetNumber)