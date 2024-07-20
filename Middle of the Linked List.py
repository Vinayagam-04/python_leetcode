def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

input_str = input("Enter linked list elements: ")
head = list_to_linkedlist(list(map(int, input_str.split())))

middle = find_middle(head)
print("Middle element of the linked list:", middle.val if middle else "List is empty")
