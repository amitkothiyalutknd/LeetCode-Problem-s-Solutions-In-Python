# Remove Nth Node From End of List

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def createLinkedList(lst):
    if not lst:
        return None

    head  = Node(lst[0])
    current = head

    for val in lst[1:]:
        current.next = Node(val)
        current = current.next

    return head

def removeNthFromTheEnd(head, n):
    dummy = Node(0)
    dummy.next = head
    slow, fast = dummy, dummy

    for _ in range(n + 1):
        fast = fast.next
    
    while fast is not None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    
    return dummy.next

myList = [1, 2, 3, 4, 5]
head = createLinkedList(myList)
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next

n = 4

head = removeNthFromTheEnd(head, n)
print(f"\nAfter {n} position element deletion from the last")
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next