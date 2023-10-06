# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#           '.' Matches any single character.​​​​
#           '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
class Solution:
    def regExpressionMatch(self, inputString: str, patternString: str):
        if len(inputString) == 0 and len(patternString) == 0:
            return True
        if (len(inputString) != 0 and len(patternString) == 0) or (len(inputString) == 0 and len(patternString) != 0):
            return False
        
        regExpMatch = [[False for col in range(len(patternString) + 1)] for row in range(len(inputString) + 1)]
        regExpMatch[0][0] = True

        for row in range(2, len(patternString) + 1):
            if patternString[row - 1] == '*':
                regExpMatch[0][row] = regExpMatch[0][row - 2]

        for row in range(1, len(inputString) + 1):
            for col in range(1, len(patternString) + 1):
                if inputString[row - 1] == patternString[col - 1] or patternString[col - 1] == ".":
                    regExpMatch[row][col] = regExpMatch[row - 1][col - 1]
                elif col > 1 and patternString[col - 1 ]  == "*":
                    regExpMatch[row][col] = regExpMatch[row][col - 2]
                    if patternString[col - 2]  == "." or patternString[col - 2] == inputString[row - 1]:
                        regExpMatch[row][col] = regExpMatch[row][col] or regExpMatch[row - 1][col]
        return regExpMatch[len(inputString)][len(patternString)]

sol = Solution()
inputString = (input("Enter The First String As Input: "))
patternString = (input("Enter The Second String For Pattern: "))
if sol.regExpressionMatch(inputString, patternString) is True:
    print(f"Both Strings '{inputString}' & '{patternString}' Are Matched.")
else:
    print(f"Both Strings '{inputString}' & '{patternString}' Are Not Matched.")