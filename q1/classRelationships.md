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

Multiplicity: *
Explanation:
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
    Both classes 
### What multiplicity did you choose and why?

### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
