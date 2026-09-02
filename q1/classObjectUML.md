# SG4 - Understanding Classes and Objects

## Class Name
`MusicTaste`

## Class Description
The “MusicTaste” class encapsulates an individual's musical interests, tracking details about their favorite song, artist, music library, and artist popularity.

## Properties
| Property | Data Type | Description |
|---|---|---|
| title | string | Title of favorite song. |
| artist | string | Name of the artist. |
| songs | int | Number of saved songs in the user's library. |
| listeners | int | Monthly listeners count of the selected artist. |

## Methods
| Method | Description |
|---|---|
| PlaySongs() | Simulates playing the selected song to provide leisure and entertainment. |
| UpdateListeners(count: int) | Updates the artist's monthly listener count with a new value. |
| PinInterests() | Prints a summary of the user's music interests and favorite artist. |

## Class Diagram
![Class Diagram](images/classDiagram.png)
## Design Explanation
### Why did you choose this class? 
I chose MusicTaste because music is a big part of my daily life, and I was genuinely curious about how my favorite songs and listening habits could be turned into code. It felt like a fun way to connect something I enjoy with object-oriented programming.
### Which property is the most important? Why?
The title is the most important property as it provides the main identification for songs, making it essential for distinguishing individual entries in a user's library.
### Which method is the most useful? Why?
The UpdateListeners(count: int) method is the most useful because listener numbers change all the time. Using count: int as a parameter allows the system to easily update the data whenever an artist gets new listeners.

