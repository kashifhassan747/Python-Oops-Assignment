
# Python OOPs Assignment - Theory & Practical Solutions

## Theory Questions (with Answers)

1. **What is Object-Oriented Programming (OOP)?**
   - OOP is a paradigm where code is organized into objects containing attributes and methods.

2. **What is a class in OOP?**
   - A class is a blueprint for creating objects.

3. **What is an object in OOP?**
   - An object is an instance of a class.

4. **Difference between abstraction and encapsulation?**
   - Abstraction hides implementation details, encapsulation binds data and methods together.

5. **What are dunder methods?**
   - Special methods with double underscores, like `__init__`, `__str__`, etc.

6. **Explain inheritance in OOP.**
   - Mechanism for a class to inherit attributes/methods from another.

7. **What is polymorphism in OOP?**
   - Same interface, different implementations.

8. **How is encapsulation achieved in Python?**
   - By private variables (`__var`) and getters/setters.

9. **What is a constructor in Python?**
   - The `__init__` method initializes attributes.

10. **Class vs static methods?**
    - `@classmethod`: works with class.
    - `@staticmethod`: independent utility.

11. **Method overloading?**
    - Simulated using default args or `*args`.

12. **Method overriding?**
    - Child class replaces parent implementation.

13. **Property decorator?**
    - `@property` defines getter methods.

14. **Why polymorphism?**
    - Promotes flexibility and reusability.

15. **Abstract class?**
    - Class with abstract methods (using `ABC`).

16. **Advantages of OOP?**
    - Modularity, abstraction, reuse, extensibility.

17. **Class vs instance variables?**
    - Class: shared, Instance: unique to each object.

18. **Multiple inheritance?**
    - A class inheriting from multiple classes.

19. **__str__ vs __repr__?**
    - str: readable, repr: debug representation.

20. **super()?**
    - Calls parent method.

21. **__del__?**
    - Destructor (called on object deletion).

22. **@staticmethod vs @classmethod?**
    - Static: no access to class/instance.
    - Class: works with class (`cls`).

23. **Polymorphism with inheritance?**
    - Method overriding in subclasses.

24. **Method chaining?**
    - Returning `self` to chain methods.

25. **__call__?**
    - Makes object callable like a function.

---

## Practical Questions (with Code)

### 1. Animal & Dog
```python
class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

d = Dog()
d.speak()
```

### 2. Abstract class Shape
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

print(Circle(5).area())
print(Rectangle(4, 6).area())
```

### 3. Multi-level inheritance
```python
class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type, brand):
        super().__init__(type)
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, type, brand, battery):
        super().__init__(type, brand)
        self.battery = battery

tesla = ElectricCar("Car", "Tesla", "100kWh")
print(tesla.type, tesla.brand, tesla.battery)
```

### 4. Bird polymorphism
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

birds = [Sparrow(), Penguin()]
for b in birds:
    b.fly()
```

### 5. BankAccount encapsulation
```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(100)
acc.withdraw(30)
print(acc.get_balance())
```

### 6. Instrument polymorphism
```python
class Instrument:
    def play(self):
        print("Playing instrument")

class Guitar(Instrument):
    def play(self):
        print("Strumming guitar")

class Piano(Instrument):
    def play(self):
        print("Playing piano")

for inst in [Guitar(), Piano()]:
    inst.play()
```

### 7. MathOperations
```python
class MathOperations:
    @classmethod
    def add_numbers(cls, a, b):
        return a + b

    @staticmethod
    def subtract_numbers(a, b):
        return a - b

print(MathOperations.add_numbers(5, 3))
print(MathOperations.subtract_numbers(10, 4))
```

### 8. Person counter
```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def total_persons(cls):
        return cls.count

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.total_persons())
```

### 9. Fraction
```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

f = Fraction(3, 4)
print(f)
```

### 10. Vector overloading
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
```

### 11. Person greet
```python
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person2("John", 25)
p.greet()
```

### 12. Student grades
```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

s = Student("Sara", [80, 90, 85])
print(s.average_grade())
```

### 13. Rectangle area
```python
class Rectangle2:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle2()
r.set_dimensions(4, 5)
print(r.area())
```

### 14. Employee/Manager salary
```python
class Employee:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

class Manager(Employee):
    def __init__(self, hours, rate, bonus):
        super().__init__(hours, rate)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

m = Manager(40, 50, 500)
print(m.calculate_salary())
```

### 15. Product
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

p = Product("Laptop", 60000, 2)
print(p.total_price())
```

### 16. Animal abstract
```python
class Animal2(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cow(Animal2):
    def sound(self):
        return "Moo"

class Sheep(Animal2):
    def sound(self):
        return "Baa"

print(Cow().sound())
print(Sheep().sound())
```

### 17. Book
```python
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_book_info(self):
        return f"{self.title} by {self.author}, published in {self.year_published}"

b = Book("1984", "George Orwell", 1949)
print(b.get_book_info())
```

### 18. House & Mansion
```python
class House:
    def __init__(self, address, price):
        self.address = address
        self.price = price

class Mansion(House):
    def __init__(self, address, price, number_of_rooms):
        super().__init__(address, price)
        self.number_of_rooms = number_of_rooms

m = Mansion("123 Street", 2000000, 10)
print(m.address, m.price, m.number_of_rooms)
```
