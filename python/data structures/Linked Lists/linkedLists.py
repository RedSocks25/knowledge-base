
# ? LINKED LISTS
'''
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
The elements in a linked list are linked using pointers.
Each element in a linked list is called a node.

A node consists of two parts:
1. Data (node value)
2. Pointer to the next node

Generally this is how a node is represented with a class

The first node is called the head and the last node is called the tail.

There are two types of linked lists:
1. Singly linked list
2. Doubly linked list

We can also have circular linked lists where the last node points to the first node.

Some of the operations that can be performed on a linked list are:
1. Add an element at the beginning or any position
2. Remove an element from the beginning or any position
3. Look up an element at a specific position
4. Etc
'''


# ? SINGLY LINKED LIST
'''
In a singly linked list, each node points to the next node.
The last node points to NULL.

The node class is defined as follows:
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
'''

class SinglyNode:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return str(self.data)


# * Create a singly linked nodes
head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(4)
c = SinglyNode(7)

# * Link the nodes
head.next = a
a.next = b
b.next = c


# * Traverse (print) the linked nodes - Time complexity: O(n)
current = head
while current:
  print(current)
  current = current.next


# * Display the linked nodes - Time complexity: O(n)
def display(head: SinglyNode):
  current = head
  elements = []
  while current:
    elements.append(current.data)
    current = current.next
  print(' -> '.join(map(str, elements)))

display(head) # 1 -> 3 -> 4 -> 7


# * Search for an element in the linked nodes - Time complexity: O(n)
def search(head: SinglyNode, value):
  current = head
  while current:
    if current.data == value:
      return True
    current = current.next
  return False

print(search(head, 4))  # True (Change the value to check for other elements)


# * Insert an element at the beginning of the linked nodes - Time complexity: O(1)
def insert_at_beginning(head: SinglyNode, value):
  new_node = SinglyNode(value)
  new_node.next = head
  return new_node

head = insert_at_beginning(head, 0)
display(head)  # 0 -> 1 -> 3 -> 4 -> 7


# * Insert an element at the end of the linked nodes - Time complexity: O(n)
def insert_at_end(head: SinglyNode, value):
  new_node = SinglyNode(value)
  current = head
  while current.next:
    current = current.next
  current.next = new_node

insert_at_end(head, 8)
display(head)  # 0 -> 1 -> 3 -> 4 -> 7 -> 8


# * Insert an element at a specific position in the linked nodes - Time complexity: O(n)
def insert_at_position(head: SinglyNode, value, position):
  new_node = SinglyNode(value)
  current = head
  for i in range(position - 1):
    current = current.next
  new_node.next = current.next
  current.next = new_node

insert_at_position(head, 5, 4)
display(head)  # 0 -> 1 -> 3 -> 4 -> 5 -> 7 -> 8



# ? DOUBLY LINKED LIST
'''
In a doubly linked list, each node points to the next node and the previous node.
The first node's previous node points to NULL and the last node's next node points to NULL.

The node class is defined as follows:
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
'''

class DoublyNode:
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev
  
  def __str__(self):
    return str(self.data)


# * Create a doubly linked nodes
