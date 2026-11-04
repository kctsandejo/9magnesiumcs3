class Animal:
  def __init__(self, name):
    self.name = name
    
  def eat(self):
    print(self.name,"is eating.")
    
  def make_sound(self):
    print(self.name, "makes a sound")

class Lion (Animal):
  def eat(self):
    print(f"{self.name} roars loudly!")
    print(f"{self.name} eats fresh meat.")
    print("-----")

class Monkey (Animal):
   def eat(self):
    print(f"{self.name} trumpets!")
    print(f"{self.name} eats grass and fruits.")
    print("-----")

class Monkey (Animal):
   def eat(self):
    print(f"{self.name} trumpets!")
    print(f"{self.name} eats grass and fruits.")
    print("-----")



