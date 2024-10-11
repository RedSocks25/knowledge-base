# Playlist Manager

## Objective
Create a console application that manages a playlist of songs using a linked list. The application should allow users to perform the following operations:
- Add a Song: Add a new song to the playlist.
- Remove a Song: Remove a specific song from the playlist.
- Reorder Songs: Move a song to a different position in the playlist.

## Requirements

### 1. Song Representation
Define a `Song` class with at least the following attributes:
- `title`: The title of the song (string)
- `artist`: The artist of the song (string)
- `next`: A pointer/reference to the next song in the playlist (for the linked list).

### 2. Linked List Implementation
Implement a `Playlist` class that supports the following methods:
- `add_song(title: str, artist: str)`: Adds a song to the end of the playlist.
- `remove_song(title: str)`: Removes the first song with the given title from the playlist.
- `reorder_song(title: str, new_position: int)`: Moves the specified song to a new position in the playlist (0-indexed).

### 3. User Interface
Create a simple console menu that allows users to:
- Add a song
- Remove a song
- Reorder a song
- Display the current playlist
- Exit the application

### 4. Input Validation
Ensure that the application handles invalid inputs gracefully (e.g., trying to remove a song that doesn’t exist, or moving a song to an invalid position).

## How to Run
1. Clone the repository.
2. Navigate to the directory containing the `playlist_manager.py` file.
3. Run the script using Python:
   ```sh
   python playlist_manager.py