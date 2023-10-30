# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, stringList) -> str:
        if not stringList:
            return None
        result = ""
        # print(smallestString)
        for i in range(len(min(stringList, key=len))):
            char = stringList[0][i]
            for string in stringList:
                if string[i] != char:
                    return result
            result += char
        return result

sol = Solution()
noOfStrings = int(input("Enter The Number Of Strings As Input: "))
stringList = list(map(str, input(f"Enter Total {noOfStrings} Strings For List. Seperate Each Input From Single Space: ").strip().split()))[:noOfStrings]
print(f"The Longest Common Prefix Among The {stringList} Is: ", sol.longestCommonPrefix(stringList))
