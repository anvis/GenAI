
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()


##############################

class Dog(Animal):
    pass

# This means: "Dog inherits everything from Animal, and I'm not adding or changing anything — no new __init__, no new methods, nothing extra." 
# The class body is intentionally empty because Dog is happy just using whatever Animal already gives it.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    pass

d = Dog("Rex")
d.speak()  # Rex makes a sound (inherited as-is)

###########################################################

## Usning Super()

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal.__init__
        self.breed = breed
        print(f"Dog breed: {self.breed}")

d = Dog("Rex", "Labrador")
# Animal 'Rex' created
# Dog breed: Labrador

######################################

print("\n\n\n Method Overridding")

#Method Overridding

class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):  # overrides parent's method
        print("Woof!")

Animal().speak()  # Some generic animal sound
Dog().speak()     # Woof!

################################################

print("\n\n\n Multiple Inheritance")

# Multiple Inheritance

class Flyable:
    def fly(self):
        print("I can fly")

class Swimmable:
    def swim(self):
        print("I can swim")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()   # I can fly
d.swim()  # I can swim

###########################################

print("\n\n\n Multiple Inheritance — Method Overridden in Both Parent Classes")

# Multiple Inheritance — Method Overridden in Both Parent Classes

class Flyable:
    def move(self):
        print("Flying through the air")

class Swimmable:
    def move(self):
        print("Swimming through water")

class Duck(Flyable, Swimmable):
    def move(self):
        print("Duck moving:")
        Flyable.move(self)     # explicitly call one parent
        Swimmable.move(self)   # explicitly call the other

d = Duck()
d.move()
# Duck moving:
# Flying through the air
# Swimming through water

########################################################

print("\n\n\n Multiple Inheritance — All Classes Define the Same Method (MRO in action)")
# Multiple Inheritance — All Classes Define the Same Method (MRO in action)

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass  # no override here

class E(B,C):
    def greet(self):
        print("Hello from E")
        super().greet()  # calls B's greet due to MRO

d = D()
d.greet()  # Hello from B  <- follows Method Resolution Order (MRO)
print(D.__mro__)
# (D, B, C, A, object) — Python resolves left to right, depth-first (C3 linearization)

#output: Hello from B

e = E()
e.greet()  # Hello from E
# Hello from B  <- super() in E calls B's greet due to MRO
print(E.mro())
# OUTPUT : Hello from B

########################################################

print("\n\n\n Multiple Inheritance with super()")

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()   # follows MRO, not just "parent class A"

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class E(A):
    def greet(self):
        print("Hello from E")
        super().greet()

class D(B, C, E):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()
# Hello from D
# Hello from B
# Hello from C
# Hello from A

print(D.__mro__)
# (D, B, C, A, object)
