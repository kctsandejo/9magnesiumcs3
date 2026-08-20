# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation groups the name, price, and quantity properties together into a single object while also restricting direct access to these variables. Controlled methods within the object can handle tasks like modifying the stock or getting item details. This protects store data from accidental edits, ensuring accurate quantities across operations.

### 2. Abstraction
Abstraction hides the background logic of array manipulation and exposes only simple functions like adding, removing, and displaying items. The operator can then perform essential actions without managing complex data structures,  simplifying the program design and its daily usage.

### 3. Inheritance
Inheritance allows specialized product categories to inherit basic properties such as name, price, and quantity from a parent object. Specific items can then add unique details, such as expiration tracking for perishable goods. This eliminates repeated code and keeps the inventory structure organized.

### 4. Polymorphism
Polymorphism allows different item types to execute their own version of a shared function, such as displayItems(). Regular items can print basic information, while specialized items print additional detailed attributes. This ensures that a single call to display inventory automatically handles diverse product behaviors cleanly.

## Reflection
Among the four pillars, Encapsulation is the most useful for improving the sari-sari store inventory system as it directly solves the problem of using 15 separate variables by grouping each item's name, price, and quantity into one single object. By restricting direct modification and directing updates through methods, it keeps quantity counts accurate and secure. This provides an organized structure  for adding, removing, and displaying items efficiently. 