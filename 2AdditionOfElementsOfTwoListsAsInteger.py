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

# Definition for singly-linked list.
class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, digit):
        newNode = Node(digit)
        newNode.next = self.head
        self.head = newNode

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while(first is not None or second is not None):

            fdigit = 0 if first is None else first.digit
            sdigit = 0 if second is None else second.digit
            Sum = carry + fdigit + sdigit

            carry = 1 if Sum >= 10 else 0

            Sum = Sum if Sum < 10 else Sum % 10

            temp = Node(Sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if carry > 0:
                temp.next = Node(carry)

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.digit, end=' ')
            temp = temp.next

first = LinkedList()
second = LinkedList()
integer1, integer2 = input("Enter Two Integers. Seperate Both Inputs From Single Sapce: ").split()
print(f"Simple Addition Of Both Integer Without Using Linked List is: {int(integer1) + int(integer2)}")
for digit in integer1:
    first.push(int(digit))
for digit in integer2:
    second.push(int(digit))
print(f"\nThe Linked List Representation of First Number After Insertion In Linked List: {integer1} is: ", end="")
first.printList()
print(f"\nThe Linked List Representation of Second Number After Insertion In Linked List: {integer2} is: ", end="")
second.printList()
result = LinkedList()
result.addTwoLists(first.head, second.head)
print(f"\nThe Resultant Sum of Both Linked List is: ", end="")
result.printList()