# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    def validParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if (char == "(") or (char == "[") or (char == "{"):
                stack.append(char)
            else:
                if not stack or ((char == ")") and stack[-1] != "(") or ((char == "]") and stack[-1] != "[") or ((char == "}") and stack[-1] != "{"):
                    return False
                stack.pop()
        return not stack
        
sol = Solution()
inputString = input("Enter The String As Input: ")
print(sol.validParentheses(inputString))