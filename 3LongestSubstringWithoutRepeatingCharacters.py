# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, inputString: str) -> int:
        subString = str()
        stringList = []
        for char in inputString:
            if char not in subString:
                subString += char
            else:
                if char == subString[0]:
                    subString = subString[1::]
                    subString += char
                else:
                    for i in range(len(subString)):
                        if subString[i] == char:
                            if subString[i] != subString[-1]:
                                subString = subString[i+1:]
                                subString += char
                                break
                            else:
                                subString = char
                        else:
                            continue
            stringList.append(subString)
        stringList = set(stringList)
        subString = max(stringList, key = len, default = 0)
        if subString == 0:
            print(f"User Doesn't Give Any String As Input.")
            return 0
        else:
            print(f"The Length of Longest Substring:'{subString}' From The InputString:'{inputString}' Is -> {len(str(subString))}")
            return len(str(subString))

sol = Solution()
inputString = str(input("Enter The String As Input: "))
sol.lengthOfLongestSubstring(inputString)