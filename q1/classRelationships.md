# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: MusicTaste
Description:  This class encapsulates an individual's musical interests, tracking details about their favorite song, artist, music library, and artist popularity.
## New Related Class
Class: PlayList
Description: This class organizes lists of audio, songs, or digital media files that play back in a specific order or on a loop
## Association
Relationship: A-PlayList
Explanation: MusicTaste is managed by PlayList in order for varying genre of songs to be organized in an effective class.
## Multiplicity

Multiplicity: 1:*
Explanation: 1 PlayList can store and manage many MusicTaste instances, whereas each MusicTaste can exist on its own or be assigned to a playlist.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The association is that PlayList contains and manages MusicTaste items. The PlayList groups individual music tastes, favorite songs, or artist profiles together to organize music by. In this setup, PlayList holds references to one or more MusicTaste objects so it can track and control playback order effectively.
### What multiplicity did you choose and why?
I chose a 1 to many (1 : *) multiplicity because a single PlayList can store and organize multiple MusicTaste examples, while each individual MusicTaste entry can belong to a playlist. This design reflects how real-life music applications allpws a user  creates a specific playlist that contains many different songs and artist profiles. Choosing * provides the flexibility to add, remove, or loop through as many music taste entries as needed.
### How did you implement the relationship in Python?
I implemented the relationship by passing MusicTaste entires into the PlayList class and storing them inside an internal list attribute such as self.tracks = []. The PlayList class provides methods like add_music_taste to append object references directly into this list. This allows PlayList methods to add through the stored list and access each MusicTaste object's properties, like play_songs().
### Why did you store an object reference instead of copying its data?
Storing an object reference ensures data consistency and preserves updates across the system. If the data were duplicated inside the playlist, any updates made to the original object such as updating an artist's monthly listener count through update_listeners(), would not be reflected inside the playlist. Referencing the actual object guarantees that both the playlist and the original instance always interact with the  same updated state.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because it is an organized data structure that supports duplicate entries, add elements, and iteration. Since playlists rely on playback order, a list maintains the exact sequence in which MusicTaste items are added. Furthermore, Python lists are suitable for managing multiplicities as it resize as tracks are added or removed.