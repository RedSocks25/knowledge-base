'''
Write a function that takes the heads of two sorted linked lists and merges them into a single sorted linked list.
The new linked list should be made by splicing together the nodes of the first two lists.
'''

class ListNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return str(self.data)


def display(head: ListNode):
  current = head
  elements = []
  while current:
    elements.append(current.data)
    current = current.next
  print(' -> '.join(map(str, elements)))


def merge_two_sorted_lists(l1: ListNode, l2: ListNode):
  dummy = ListNode(0)
  current = dummy

  while l1 and l2:
    if l1.data < l2.data:
      current.next = l1
      l1 = l1.next
    else:
      current.next = l2
      l2 = l2.next
    current = current.next
  
  if l1:
    current.next = l1
  elif l2:
    current.next = l2
  
  return dummy.next


# Create two linked lists
head1 = ListNode(1)
a1 = ListNode(3)
b1 = ListNode(5)

head2 = ListNode(2)
a2 = ListNode(4)
b2 = ListNode(6)

# Link the nodes
head1.next = a1
a1.next = b1

head2.next = a2
a2.next = b2

display(head1) # 1 -> 3 -> 5
display(head2) # 2 -> 4 -> 6

merged_head = merge_two_sorted_lists(head1, head2)
display(merged_head) # 1 -> 2 -> 3 -> 4 -> 5 -> 6