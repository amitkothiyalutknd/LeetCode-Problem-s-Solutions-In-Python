# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
class Solution:
    # -----------------------------------METHOD 1-----------------------------------
    # def subPalindromic(self, inputString, low, high):
    #     subString = str()
    #     for i in range(low, high + 1):
    #         subString += inputString[i]
    #     return subString

    # def longestPalindrome(self, inputString: str) -> str:
    #     n = len(inputString)
    #     maxLength = 1
    #     start = 0
    #     for i in range(n):
    #         for j in range(i, n):
    #             flag = 1
    #             for k in range(0, ((j - i) // 2) + 1):
    #                 if (inputString[i + k] != inputString[j - k]):
    #                     flag = 0
    #             if (flag != 0 and (j - i + 1) > maxLength):
    #                 start = i
    #                 maxLength = j - i + 1
    #     print(f"The Longes Palindromic Substring In The InputString '{inputString}' Is : '{self.subPalindromic(inputString, start, start + maxLength - 1)}'")
    # -----------------------------------METHOD 2-----------------------------------
    def longestPalindrome(self, s: str) -> str:
        result, resultLen = "", 0
        for i in range(len(s)):
            result, resultLen = self.computePalindrome(i,i, s, result, resultLen)
            # result, resultLen = self.computePalindrome(i,i+1, s, result, resultLen)
        print(f"The Longes Palindromic Substring Of Length {len(result)} In The InputString '{inputString}' Is : '{result}'")
        
    def computePalindrome(self, left, right, string, result, resultLen):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if (right - left + 1) > resultLen:
                result = string[left:right+1]
                resultLen = right - left + 1
            left -= 1
            right += 1
        return [result, resultLen]

sol = Solution()
inputString = input("Enter The String As Input: ")
sol.longestPalindrome(inputString)