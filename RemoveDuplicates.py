class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating a sorted linked list with duplicates: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

# Print original list
print("Original List:")
print_list(head)

# Remove duplicates
solution = Solution()
head = solution.deleteDuplicates(head)

# Print modified list
print("List after removing duplicates:")
print_list(head)