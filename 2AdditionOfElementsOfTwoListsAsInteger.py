# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# 2 --> 4 --> 3
# 5 --> 6 --> 4
# -------------
# 7 --> 0 --> 8
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertAtBeginning(self, val):
        newListNode = ListNode(val)
        newListNode.next = self.head
        self.head = newListNode
        return None

    def addTwoNumbers(self, list1, list2):
        result = ([int(e) for e in str(int("".join([str(i) for i in list1])) + int("".join([str(i) for i in list2])))])
        return result[::-1]

l1 = Solution()
l2 = Solution()
l = Solution()
list1 = list(map(int, input("Enter Multiple Elements To Be Insert In List1. Seperate Each Inputs from Single Space.:\t").split(' ')))
for val in reversed(list1):
    l1.insertAtBeginning(val)
list2 = list(map(int, input("Enter Multiple Elements To Be Insert In List2. Seperate Each Inputs from Single Space.:\t").split(' ')))
for val in reversed(list2):
    l2.insertAtBeginning(val)
print(f"The First List: {list1}\t & The Second List: {list2}\nThe Resultant Sum Of Both Lists is: {l.addTwoNumbers(list1, list2)}")