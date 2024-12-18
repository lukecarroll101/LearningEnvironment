class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None  
    current = head 

    while current:
        next_node = current.next  
        current.next = prev  
        prev = current 
        current = next_node 

    return prev  


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original Linked List:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)
