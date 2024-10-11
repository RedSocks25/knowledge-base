'''
Exercise Prompt: Playlist Manager

Objective: Create a console application that manages a playlist of songs using a linked list. The application should allow users to perform the following operations:
- Add a Song: Add a new song to the playlist.
- Remove a Song: Remove a specific song from the playlist.
- Reorder Songs: Move a song to a different position in the playlist.

Requirements:
1. Song Representation: Define a Song class with at least the following attributes:
  - title: The title of the song (string)
  - artist: The artist of the song (string)
  - next: A pointer/reference to the next song in the playlist (for the linked list).

2. Linked List Implementation: Implement a Playlist class that supports the following methods:
 - add_song(title: str, artist: str): Adds a song to the end of the playlist.
  - remove_song(title: str): Removes the first song with the given title from the playlist.
  - reorder_song(title: str, new_position: int): Moves the specified song to a new position in the playlist (0-indexed).

3. User Interface: Create a simple console menu that allows users to:
  - Add a song
  - Remove a song
  - Reorder a song
  - Display the current playlist
  - Exit the application

4. Input Validation: Ensure that the application handles invalid inputs gracefully (e.g., trying to remove a song that doesn’t exist, or moving a song to an invalid position).
'''



class Song:
  '''
  Song class with title, artist, and next attributes

  Attributes:
    title (str): The title of the song
    artist (str): The artist of the song
    next (Song): A pointer/reference to the next song in the playlist
  
  Methods:
    __init__: Initializes the Song object with the given title and artist
    __str__: Returns a string representation of the
  '''
  def __init__(self, title, artist):
    self.title = title
    self.artist = artist
    self.next = None
  
  def __str__(self):
    return f'{self.title} by {self.artist}'


class Playlist:
  '''
  Playlist class that manages a playlist of songs using a linked list

  Attributes:
    head (Song): The first song in the playlist
  
  Methods:
    add_song: Adds a new song to the end of the playlist
    remove_song: Removes a specific song from the playlist
    reorder_song: Moves a song to a different position in the playlist
    display: Displays the current playlist
  '''
  def __init__(self):
    self.head = None
  
  def add_song(self, title, artist):
    new_song = Song(title, artist)
    if not self.head:
      self.head = new_song
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_song
  
  def remove_song(self, title):
    if not self.head:
      print('Playlist is empty')
      return
    if self.head.title == title:
      self.head = self.head.next
      return
    current = self.head
    while current.next:
      if current.next.title == title:
        current.next = current.next.next
        return
      current = current.next
    print('Song not found')
  
  def reorder_song(self, title, new_position):
    if not self.head:
      print('Playlist is empty')
      return
    if self.head.title == title:
      print('Cannot move the first song')
      return
    current = self.head
    prev = None
    index = 0
    while current:
      if current.title == title:
        break
      prev = current
      current = current.next
      index += 1
    if not current:
      print('Song not found')
      return
    if new_position < 0 or new_position >= index:
      print('Invalid position')
      return
    prev.next = current.next
    current.next = None
    if new_position == 0:
      current.next = self.head
      self.head = current
    else:
      temp = self.head
      for _ in range(new_position - 1):
        temp = temp.next
      current.next = temp.next
      temp.next = current
  
  def display(self):
    current = self.head
    while current:
      print(current)
      current = current.next

def main():
  playlist = Playlist()
  
  while True:
    print('\n\nPlaylist Manager')
    print('1. Add a song')
    print('2. Remove a song')
    print('3. Reorder a song')
    print('4. Display the playlist')
    print('5. Exit', end='\n')

    choice = input('\nEnter your choice: ')
    
    if choice == '1':
      title = input('\nEnter the title of the song: ')
      artist = input('Enter the artist of the song: ')
      playlist.add_song(title, artist)
    elif choice == '2':
      title = input('\nEnter the title of the song to remove: ')
      playlist.remove_song(title)
    elif choice == '3':
      title = input('\nEnter the title of the song to reorder: ')
      new_position = int(input('Enter the new position (0-indexed): '))
      playlist.reorder_song(title, new_position)
    elif choice == '4':
      playlist.display()
    elif choice == '5':
      break
    else:
      print('\nInvalid choice. Please try again.')

if __name__ == '__main__':
  main()