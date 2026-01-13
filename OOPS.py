# class Heroes:
#     def names(self, name):
#         return f"{name} "

# Constructor
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def print(self,fee):
#         print(f"his name is {self.name} and age is {self.age}")
#         print(f"he should pay {fee}")
    
# c1 = Student("ankur", "20")
# c1.print(25000)


# Variables #
# class variable
# class Cars:
#     wheels = 4
#     def names(self, brand):
#         return f"my car is {brand}"
    
#     c1 = Cars()
#     print(c1.names("bugati"))
#     print(c1.wheels)

# class cars:
#     wheels = 4
#     @classmethod
#     def name(cls):
#         return cls.wheels
    
# c1 = cars()

# class Calculator:
#     @staticmethod
#     def add(x, y):
#         return x + y
#     @staticmethod
#     def mult(x, y):
#         return x * y
    
# c1 = Calculator()
# print(c1.add(5, 6))
# print(c1.mult(5, 6))


# class Bank:
#     def __init__(self, AccHolder, Age, Balance):
#         self.AccHolder = AccHolder
#         self.Age = Age
#         self.Balance = Balance

#     def balance_enquary(self):
#         return f"{self.AccHolder} have {self.Balance} Balance"
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.Balance += amount

#     def withdraw(self, amount):
#         if amount < self.Balance:
#             self.Balance -= amount
#         else:
#             return "insufficient balance"
        
# c = Bank("Ankur", 20, 800000000000)

# print(c.Balance)
# c.deposit(5000)
# c.withdraw(8000)
# print(c.balance_enquary())


# class Bank:
#     def __init__(self, name, salary, age):
#         self.name = name
#         self.__salary = salary
#         self._age = age

#         def balance_enquary(self):
#             return f"{self.name} have {self.__salary} Balance"
        
#         def deposit(self, amount):
#             if amount > 0:
#                 self.__salary += amount
        
#         def withdraw(self, amount):
#             if amount < self.__salary:
#                 self.__salary -= amount
#             else:
#                 return "Insufficient balance"
            

# c = Bank("Ankur", 20000000, 20)

# print(c.__salary)
# c.deposit(5000)
# c.withdraw(8000)
# print(c.balance_enquary())


# class Heroes:
#     def __init__(self, name, movie):
#         self._name = name
#         self.movie = movie

#     def __update(self, name, movie):
#         self.name = name
#         self._movie = movie

#     def show(self):
#         return f"{self.name} is the hero in {self._movie}"
    
#     def print(self):
#         return self.__update()
    
# c = Heroes("SpiderMan", "Avengers")
# c.__update("MJ", "Spier Man")



# Inheritance is a mechanosm where the child class can access the attribute methods and their behaviour in the parent classred


# class Animal:
#     def __init__(self, name, verdict):
#         self.name = name
#         self.verdict = verdict

# class Hero(Animal):
#     def show(self):
#         return f"{self.name} acted in Animal and it is a {self.verdict} movie"
    
# c = Hero("Ranvir Kapoor", "Blocbuster")
# print(c.show())


# class parul:
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
#     def fee(self):
#         print("fee for IEP is 500000")
#         print("fee for CSE is 400000")

# class CSE(parul):
#     def show(self, course):
#         if self.course == course:
#             return f"{self.name} is studying in parul in {self.course}"
        
# class IEP(parul):
#     def show(self, course):
#         if self.course == course:
#             return f"{self.name} is studying in parul in {self.course}"
        
# a = IEP("Sonal", "IEP")
# b = CSE("Sonal", "CSE")

# print(a.show("CSE"))
# print(b.show("IEP"))

# class Food:
#     def __init__ (self, name, place):
#         self.name = name
#         self.place = place

#     def check(self, name):
#         indian = ["idli", "sambar", "biryani"]
#         chinese = ["noodles", "mandarine", "Cockroach"]
#         japan  = ["raman", "Sushi", "Macha"]

#         if name in indian:
#             return f"{self.name} is an indian food"
        
#         elif name in chinese:
#             return f"{self.name} is a chinese food"
        
#         else:
#             return f"{self.name} is a japanese food"
        
# class Indian(Food):
#     def print(self, name1):
#         return Food.check
    
# class Japanese(Indian):
#     def print(self, name2):
#         return Food.check
    
# class Grandfather:
#     def __init__(self, name, work):
#         self.name = name
#         self.work = work

#     def show(self):
#         return f"{self.name} is doing a job of {self.work}"
    
# class Boy(Grandfather):
#     def show(self):
#         return Grandfather.show(self)
    
# class Girl(Grandfather):
#     def show(self):
#         return Grandfather.show(self)
    
# a = Boy("Mahendra Saw", "Farmer")
# b = Girl("Jagdish Saw", )
# print(a.show())

# class A:
#     def showA(self):
#         print("class A")

# class B(A):
#     def showB(self):
#         print("class B")

# class C(A):
#     def showC(self):
#         print("class C")

# class D(B,C):
#     def showD(self):
#         print("class D")

# obj = D()

# print(obj.showA())
# print(obj.showB())
# print(obj.showC())
# print(obj.showD())

# lambda x : x * x
# r = int(input())
# y = lambda

# Square = lambda x:x * x
# print(Square(5))


# class cars:
#     wheels = 4
#     @staticmethod
#     def add(x,y):
#         return x+y
#     @classmethod
#     def show(cls):
#         return cls.wheels
#     def __init__(self, color, brand):
#         self.name = color
#         self.brand = brand
#     def flex(self):
#         return f"my color is {self.brand} and color {self.name}"
    
# obj = cars("black", "bmw")
# print(obj.show())
# print(obj.flex())
# print(obj.add(5, 6))


# class Bank:
#     def __init__(self, Name, Age, Balance):
#         self.Name = Name
#         self._Age = Age
#         self.__Balance = Balance
#     def __Balance(self, Balance)


# class Animal:
#     def __init__(self, name, action):
#         print(f"The action of the animal is {action} and the animal name is {name}")
    
# class dog(Animal):
#     def __init__(self, breed, action ):
#         return super().__init__(breed, action)
#         print(f"The dog breed is {breed} and it does {action}")
# obj = dog("pamerian", "woof-woof")
# print(obj)

# class Animal:
#     def __init__(self):
#         print("animal can talk")
    
# class dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("dog will bark")
# obj = dog()
# print(obj)

# class Animal:
#     def __init__(self):
#         print("animal can talk")
#     def work(self):
#         return " the animal walk"
    
# class dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("dog will bark")
#     def work(self):
#         super().__init__()
#         return "the dog will walk with four legs"
# obj = dog()
# print(obj.work)

from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass

class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate")

class HDFC(Bank):
    def interest_rate(self):
        print("HDFC interest rate")

b1 = SBI()
b2 = HDFC()

print(b1.interest_rate())