class Animal:
  def __init__(self, name):
    self.name = name
    
  def eat(self):
    print(f"{self.name} is eating.")
    
  def make_sound(self):
    print(f"{self.name} makes a sound.")

class Lion (Animal):
  def eat(self):
    print(f"{self.name} eats fresh meat.")

  def make_sound(self):
    print(f"{self.name} roars loudly!")

class Elephant(Animal):
  def eat(self):
    print(f"{self.name} eats grass and fruits.")

  def make_sound(self):
    print(f"{self.name} trumpets!)

class Monkey(Animal):
  def eat(self):
    print(f"{self.name} eats bananas.")

  def make_sound(self):
    print(f"{self.name} chatters!")


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")
