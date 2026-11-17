'''
class means blue print 
'''
'''
class class_name:
    # block of code
'''

class greeting:
    def greet():
        return "Welcome to the python class"

greet1 = greeting.greet()
# print(f"{greet1} Abishek")

# Constructor -> which is a type of class that helps the class to call parameter defaultly
# Parent class
class Animal:
    def __init__(self, sound, meals):
        self.sound = sound
        self.meals = meals
    def dog(self):
        return f"Dog used to {self.sound} and have a fav food like {self.meals}"
    def cat(self):
        return f"Cat used to {self.sound} and have a fav food like {self.meals}"

Dog1 = Animal("Bark", "Bones").dog()
Cat1 = Animal("Meow", "Milk").cat()
# print(Dog1,"\n", Cat1)
'''
Abstract class 
'''
class Animal_cow(Animal):
    def dog(self):
        return f"Dog used to make sound like {self.sound} and have a fav food like {self.meals}"
    def cow(self):
        return f"Cow used to make sound like{self.sound} amd have a fav food like {self.meals}"

dog2 = Animal_cow("Bark", "Bones").dog()
cow1 = Animal_cow("Gaaaa","Grass").cow()
# print(dog2, "\n",cow1)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}")
        result = func(*args,**kwargs)
        return result
    return wrapper
@my_decorator
def my_function():
    print("Inside function")

'''
local variable  --> private variable -> we need to create 
protected variable --> 
global variable  -> public variable -> our noraml created variable
'''
'''
Encapsulation
'''
class car:
    def __init__(self, fuel : int, models):
        self.__fuel = fuel
        self.model = models
    def car1(self):
        return f"This car model {self.model} have {self.__fuel} fuel liter"
car2 = car(15, "TATA").car1()
# print(car2)
'''
polimorphism
'''
class cat:
    def make_sound(self):
        return "Meow"
class dog:
    def make_sound(self):
        return "Bark"

def animals(animal):
    return (animal.make_sound())

# print(animals(cat()))
# print(animals(dog()))
'''
Inheritance
'''
class school:
    def python():
        return "you are in python class"

class college(school):
    def ISTN():
        return "You are reading from ISTN "
'''
Data class
'''
from dataclasses import dataclass
@dataclass
class Dataclass:
    id : int
    title : str
    description : str

task = Dataclass(id=1, title= "python class", description="Dashain Batch")
# print(task)
'''
OOP -> Object orientend programming
1. Abstract
2. Inheritance
3. Polimorphism
4. Encaptulation
'''
'''
super class
Derived/sub class
overriding
overloading
'''
class sweet:
    def __init__(self,name, categories):
        self.name = name
        self.category = categories
    def eat(self):
        return f"Eating a cookies {self.name} of {self.category}"

class cupcake(sweet):
    def __init__(self,name, calories):
        super().__init__(name, calories)

    def add_chocolate(self):
        return f"Adding Dark chocolate"

'''
overiding method -> child class inherit the method of parent class
'''
class buisness:
    def staff():
        return "There are almost 500 staffs in ABC company"

class startup(buisness):
    def staff():
        return "There are almost 50 staffs in XYZ company"

'''
overloading method -> multiple method with same name but different parameter
'''
class house:
    def rent(self, utitlities, paint, assets="car"):
        if assets == "car" :
            return f"we made the house in {self.paint}"
        else :
            return f"Invalid assets"
    def rent(self, accesories, gas):
        pass

'''
pass -> move ahead
break -> stop
continue -> 1 step ahead 
'''