# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
To improve data integrity and follow object-oriented programming principles, the original `MusicTaste` design was revised to apply visibility modifiers. The general descriptive attributes (`title` and `artist`) remain public for easy access. However, numeric state properties (`songs` and `listeners`) were updated to private attributes (`__songs` and `__listeners`) using Python's double-underscore prefix. This ensures sensitive library data cannot be directly altered or corrupted with negative values from outside the class.

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| `title` | string | Public | Reading or changing a song title does not break any internal safety rules in the program. |
| `artist` | string | Public | It is basic display information that external scripts need to read freely across the program. |
| `songs` | int | Private | To protect internal data; if made public, external code could corrupt the library by setting negative values. |
| `listeners` | int | Private | To enforce encapsulation, preventing unauthorized modifications and forcing updates to pass through validated methods. |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?
I made `__songs` and `__listeners` private to protect the data from being changed incorrectly from outside the class. If they were public, any part of the program could accidentally set negative numbers or negative listeners. Making them private forces all updates to go through safety checks in our methods first.

### Which method changes the state of your object?
The `update_listeners(count)` method changes the state of the object by modifying the private `__listeners` attribute. When passing a new number into this method, it checks if the value is zero or higher. If it is valid, it overwrites the old listener count with the new value.

### How did your two objects demonstrate that instances are independent?
Our test run demonstrated independence because updating `music1` did not affect `music2` at all. When 'update_listeners(100000)` was called on `music1`, its listeners changed from increased. Meanwhile, `music2` kept its original listeners, showing that each object holds its own separate memory space.

### What is the difference between your class diagram and your object diagram?
The class diagram is just the general blueprint showing attribute names, data types, and methods. The object diagram shows the actual state of real instances during runtime. Instead of listing data types, the object diagram shows the exact values stored inside `music1` and `music2` at that specific moment.
