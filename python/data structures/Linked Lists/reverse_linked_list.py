'''
Exercise: Write a function that takes the head of a singly linked list as input and returns the head of the linked list reversed.
'''

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return str(self.data)
  

def display(head: Node):
  current = head
  elements = []
  while current:
    elements.append(current.data)
    current = current.next
  print(' -> '.join(map(str, elements)))


def reverse_linked_list(head: Node) -> Node:
  prev = None
  current = head

  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

  return prev


# Create three nodes
head = Node(1)
a = Node(2)
b = Node(3)

# Link the nodes
head.next = a
a.next = b

display(head) # 1 -> 2 -> 3

# Reverse the linked list
reversed_head = reverse_linked_list(head)
display(reversed_head) # 3 -> 2 -> 1