# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
class Solution:
    def convert(self, inputString, numRows):
        if len(inputString) < 1:
            return 0
        if len(inputString) < 3 or numRows >= len(inputString):
            return inputString
        else:
            variable, linenumber, pointer, Flag, result = globals(), 0, 0, True, str()
            for row in range(numRows):
                variable["string%s" % (row+1)] = str()
                # listA.append("string{0}".format(row))
        
            for index1 in range(len(inputString)):
                linenumber += 1
                variable["string%s" % (linenumber)] += inputString[pointer]
                pointer +=1
                if pointer == len(inputString):
                    break
                if linenumber == numRows:
                    for index2 in range(numRows-1, 1,-1):
                        variable["string%s" % (index2)] += inputString[pointer]
                        pointer +=1
                        if pointer == len(inputString):
                            Flag  = False
                            break
                    linenumber = 0
                if Flag == False:
                    break
            for row in range(numRows):
                result += variable["string%s" % (row+1)]
            return result

sol = Solution()
inputString = input("Enter The String As Input: ")
numRows = int(input("Enter The Number Of Rows For ZigZag Pattern: "))
print(f"The ZigZag Pattern Of Given String '{inputString}' is:\t", sol.convert(inputString, numRows))