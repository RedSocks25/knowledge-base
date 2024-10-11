
# ? DYNAMIC ARRAYS
'''
These are arrays that can grow and shrink in size.
Also the items in the array are stored in a contiguous block of memory, same as static arrays.
Each item can be mutated.
'''

a = [1, 2, 3, 4, 5]


# * Adding an element - Time complexity: O(1)
a.append(6)
print(a)  # [10, 2, 3, 4, 5, 6]


# * Removing an element at the end - Time complexity: O(1)
a.pop()
print(a)  # [10, 2, 3, 4, 5]


# * Inserting an element at the beginning - Time complexity: O(n)
a.insert(0, 0)
print(a)  # [0, 10, 2, 3, 4, 5]


# * Modify an element at a specific index - Time complexity: O(1)
a[0] = 1
print(a)  # [1, 10, 2, 3, 4, 5]


# * Accessing an element with index - Time complexity: O(1)
print(a[0])  # 1


# * Say if an element is present in the array - Time complexity: O(n)
print(1 in a)  # True (Change the value to check for other elements)


# * Find the index of an element - Time complexity: O(n)
print(a.index(1))  # 0 (Change the value to check for other elements)


# * Find the length of the array - Time complexity: O(1)
print(len(a))  # 6



# ? STRING ARRAYS
'''
Strings are arrays of characters.
The way strings are stored in memory is similar to arrays but behaves differently.
'''

s = 'hello'


# * Append a character to the string - Time complexity: O(n)
b = s + ' world'
print(b)  # hello world


# * Check if a character is present in the string - Time complexity: O(n)
print('h' in s)  # True (Change the value to check for other characters)


# * Accessing a character with index - Time complexity: O(1)
print(s[0])  # h


# * Find the length of the string - Time complexity: O(1)
print(len(s))  # 5


# * Find the index of a character - Time complexity: O(n)
print(s.index('h'))  # 0 (Change the value to check for other characters)


# * Modify a character at a specific index - Time complexity: O(n)
s = s[:0] + 'H' + s[1:]
print(s)  # Hello