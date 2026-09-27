 # Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: MusicTaste
Child: PremiumMusicTaste
Explanation: PremiumMusicTaste is simply an exclusive version of a standard MusicTaste profile and explicitly points out the use of super().__init__().
## Inheritance UML
![Inheritance](https://github.com/kctsandejo/9magnesiumcs3/blob/main/PictureFolder/inheritanceDiagram.jpg?raw=true)
## Composition/Aggregation
Relationship: Composition (Strong HAS-A)
Explanation: It provides a strong ownership bond where the PlaylistInfo cannot exist without the PlayList, which follows the composition relationship.
## Advanced UML Diagram
![Advanced UML](https://github.com/kctsandejo/9magnesiumcs3/blob/main/PictureFolder/advancedClassDiagram.jpg?raw=true)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](https://github.com/kctsandejo/9magnesiumcs3/blob/main/PictureFolder/advancedTestRun.jpg?raw=true)
## Object Diagram
![Objects](https://github.com/kctsandejo/9magnesiumcs3/blob/main/PictureFolder/advancedObjectDiagram.jpg?raw=true)
## Reflection

### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
I chose PremiumMusicTaste as a child class of MusicTaste because a premium profile is a specific type of music taste profile (IS-A relationship). It shares all basic features like favorite songs and artists. It simply extends the parent class with a listening_mode attribute.

### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance allowed PremiumMusicTaste to reuse parent variables using super().__init__(). I did not need to repeat code for listener_name, favorite_song, favorite_artist, or artist_popularity. It also inherited the update_popularity() method automatically.

### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
​My HAS-A relationship is Composition because PlayListInfo is created directly inside PlayList.__init__(). The details belong exclusively to that playlist. Therefore, if the PlayList object is deleted, its PlayListInfo object is deleted along with it, showing a compoition relationship.

### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
In Part III's Association, MusicTaste objects were created outside PlayList and passed in as references. In Part IV's Composition, PlayListInfo is created internally by PlayList. This creates strong ownership and lifecycle dependence.

### 5. How does your design follow the DRY principle?
The design follows the DRY principle by storing shared attributes in the parent class MusicTaste. This avoids writing repeated setup code in child classes. Additionally, it separates playlist details into PlayListInfo, keeping the code organized and modified in a single place.
