# Classes

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)


# Constructors

class SecondPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = SecondPoint(10, 20)
print(point.x)


# Challenge

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! I am {self.name}")


john = Person("John Smith")
print(john.name)
john.talk()

bob = Person("Bob Smith")
print(bob.name)
bob.talk()


# Inheritance: Use code again with repeating by inheriting parent class
# In this case, the class Mammal is the parent class

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()
