
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list (optional for debugging)
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)))

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Example input lists (Python lists)
    list1_values = [1, 3, 5, 7]
    list2_values = [2, 4, 6, 8]

    # Convert Python lists to linked lists using the helper function
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    # Call the mergeTwoLists method
    merged_list = solution.mergeTwoLists(list1, list2)

    # Print the merged linked list
    print("Merged Linked List:")
    print_linked_list(merged_list)

# Call the main function
if __name__ == "__main__":
    main()





# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         merged_list = []
#         i = j = 0
        
#         while i < len (list1) and j < len(list2):
#             if list1[i] < list2[j]:
#                 merged_list.append(list1[i])
#                 i += 1
#             else:
#                 merged_list.append(list2[j])
#                 j += 1
        
#         while i < len(list1):
#             merged_list.append(list1[i])
#             i += 1
        
#         while j < len (list2):
#             merged_list.append(list2[j])
#             j += 1

#         return merged_list


# def main():
#     # Create an instance of the Solution class
#     solution = Solution()

#     # Example input lists
#     list1 = [1, 3, 5, 7]
#     list2 = [1, 2, 4, 6, 8]

#     # Call the mergeTwoLists method
#     merged_list = solution.mergeTwoLists(list1, list2)

#     # Print the result
#     print("Merged List:", merged_list)
