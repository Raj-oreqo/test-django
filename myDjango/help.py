
# string manipulation example
string = 'hello og helo '

print('{} - {}'.format(string, string[::-1]))

print(dir(string))
print(help(string)) # help function help(class_name) or help(function_name)


a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)


# list 
my_list = ['History', 'Math', 'Physics', 'Chemistry']
print(my_list)
my_list.append('Biology')
print(my_list)
my_list.remove('Math')
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_list.reverse()
print(my_list)
my_list.insert(2, 'Geography')
print(my_list)
my_list.extend(['English', 'Art'])
print(my_list)
my_list.pop(2) # default pop with last element
print(my_list)
index = my_list.index('Physics')
print('Index of Physics:', index)
new_list = ' - '.join(my_list)

# set
my_set = {'H', 'L'}
my_set.add('A')
my_set.intersection_update({'A', 'B', 'C'})
my_set.difference_update({'H', 'L'})
print(my_set)
my_set.discard('A')  # remove 'A' if it exists
my_set.clear()  # clear the set
my_set.difference({'A', 'B', 'C'})  # returns a new set without modifying the original
my_set.intersection({'A', 'B', 'C'})  # returns a new set with common elements
my_set = {'A', 'B', 'C'}
# dictionary

student = {
    'name': 'John',
    'age': 20,
    'courses': ['Math', 'Science'],
    'grades': {'Math': 90, 'Science': 85}
}

print(student.get('name'))  # Accessing value by key
print(student.get('courses', []))  # Accessing with default value if key doesn't exist
print(student.keys())  # Get all keys
print(student.values())  # Get all values
print(student.items())  # Get all key-value pairs
student['age'] = 21  # Update value
print(student)
student['grades']['Math'] = 95  # Update nested dictionary value
print(student)
del student['age']  # Delete key-value pair
print(student)
student['city'] = 'Los Angeles'  # Add new key-value pair
print(student)
student['courses'].append('History')  # Add to list in dictionary
print(student)
print(student.pop('courses'))  # Remove key and return value
print(student)
student.popitem()  # Remove and return the last inserted key-value pair
print(student)
student.update({'name': 'Jane', 'city': 'New York'})  # Update or add multiple key-value pairs
print(student)
print(student.setdefault('country', 'USA'))  # Set default value if key doesn't exist
print(student)
print(student.setdefault('city', 'Los Angeles'))  # No change since 'city' already  exists
print(student)
print(student.get('nonexistent_key', 'Default Value'))  # Accessing a non-existent
# key with a default value
print(student.get('name', 'Default Name'))  # Accessing an existing key with a default value
print(student.get('nonexistent_key'))  # Accessing a non-existent key without   
# a default value
print(student.get('name'))  # Accessing an existing key without a default value
print(student.get('courses', []))  # Accessing a non-existent key with a default value
print(student.get('nonexistent_key', 'Default Value'))  # Accessing a non-existent key with a default value
print(student.get('name', 'Default Name'))  # Accessing an existing key with a default value
print(student.get('nonexistent_key'))  # Accessing a non-existent key without a default value
print(student.get('name'))  # Accessing an existing key without a default value
print(student.get('courses', []))  # Accessing a non-existent key with a default value
print(student.get('nonexistent_key', 'Default Value'))  # Accessing a non-existent key with a default value
print(student.get('name', 'Default Name'))  #   Accessing an existing key with a default value
print(student.get('nonexistent_key'))  # Accessing a non-existent key without a default value
print(student.get('name'))  # Accessing an existing key without a default value

for key, value in student.items():
    print(f"{key}: {value}")  # Iterating through key-value pairs
    
    
    
    
# functions
def greet(*args, name='World', **kwargs):
    print(args)
    print(name)
    print(kwargs)
greet('Hello', 'Hi', name='Alice', age=30, city='Wonderland')
courses = ['Math', 'Science', 'History']
info = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
greet(courses, info)
greet(*courses, **info)
def add_numbers(a, b):
    return a + b


from os import pardir
import sys
print(sys.path) # first current directory, lib path,  then python path, environement variables, third party packages

import datetime
import calendar

# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U


# pip freeze --local  > requirements.txt

# source  project1/bin/activate
# deactivate


# scope LEGB ,# Local, Enclosing, Global, Built-in
# def outer_function():
#     x = 'local'
    
#     def inner_function():
#         nonlocal x  # Access the variable from the enclosing scope
#         x = 'nonlocal'
#         print('Inner:', x)
    
#     inner_function()
#     print('Outer:', x)

# 🧠 When to Use nonlocal
# Inside nested functions

# When you want to update a variable from the outer function

# Often used in closures, decorators, or function factories

def out_outer_function():
    x = 'local'
    
    def outter_function():
        x = 'outer'
        def inner_function():
            nonlocal x
            x = 'inner'
            print('Inner:', x)
        inner_function()
        print('Outer:', x)
    outter_function()
    print('out outer :', x)
out_outer_function()


# EAFP easier to ask for forgiveness than permission
# LBYL look before you leap
person = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
person = {'name': 'Alice', 'age': 30}
try:
    print("I'm {name}. Age {age} from {city}".format(**person))
except KeyError as e:
    print(f"Missing key: {e}")
my_list = ['apple', 'banana', 'cherry']
try:
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("Index out of range. Using last element instead:", my_list[-1])

import os
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Creating a new file.")
    with open('new_file.txt', 'w') as file:
        file.write("This is a new file created because the original was not found.")
        
import os
my_file = 'example.txt'
if os.access(my_file, os.F_OK):
    with open(my_file, 'r') as file:
        content = file.read()
else:
    print(f"{my_file} does not exist. Creating a new file.")
    # with open(my_file, 'w') as file:
    #     file.write("This is a new file created because the original was not found.")

try:
    f = open('example.txt', 'r')
    content = f.read()
except FileNotFoundError:
    print("File not found. Creating a new file.")
    with open('example.txt', 'w') as f:
        f.write("This is a new file created because the original was not found.")
        
finally:
    try:
        f.close()
    except NameError:
        print("File was never opened, so no need to close it.")
    else:
        print("File closed successfully.")

# generator example
x = [y*y for y in range(10)]
print(x)
x = (y*y for y in range(10)) # generator expression ** faster and memory efficient
print(x)
# xrange vs range, iteritems vs items, iterkeys vs keys

        
# first class functions 
## function treated as objects in Python
##  when a function is passed as an argument to another function, returned from a function, or assigned to a variable, it is considered a first-class function.
class decorator_class(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorator class called")
        return self.func(*args, **kwargs)
@decorator_class
def my_function(x, y):
    print(f"Function called with arguments: {x}, {y}")
    return x + y
result = my_function(5, 10)
print(f"Result: {result}")

# class parent class sub class(child class)
# class MyMetaClass:
#     def __init__(cls, base, name, attrs):
#         print(f"Initializing class {name} with base {base}")
#         super().__init__(base, name, attrs)
#     def __new__(cls, base, name, attrs):
#         print(f"Creating class {name} with base {base}")
#         return super().__new__(cls)
# class MyBaseClass(metaclass=MyMetaClass):
#     pass

# MyMetaClass()
# isinstance, issubclass, type, id, dir, help, getattr, setattr, delattr, hasattr
# @classmethod
# @staticmethod
# @property


# system tasks

username = 'raj-suraj-yadav-tt'
# f, s, t = username.split('-')
first, second, kk = username.split('-', 2)
print(f"First part: {first}, Second part: {second}")



# # file
# import glob
# print(glob.glob('*.txt'))  # List all Python files in the current directory
# for file in glob.glob('*.py'):
#     print(file)
my_dict = {}
heroes = ['Superman', 'Batman', 'Wonder', 'Flash', 'Green Lantern']
names = ['Clark', 'Bruce', 'Diana', 'Barry', 'Hal']
for hero, name in zip(heroes, names):
    my_dict[hero] = name
# print(my_dict)
my_dict = {hero: name for hero, name in zip(heroes, names)}

# print(sorted(my_dict.__iter__(), key=lambda x: x[1]))# Sort by values

# for k, v in my_dict.iteritem():
#     print(f"{k}: {v}")  # Print key-value pairs
    

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Employee({self.name!r}, {self.age!r})"

emp1  = Employee("Alice", 30)
emp2 = Employee("Bob", 25)
emp3 = Employee("Charlie", 35)

sorted_employees = sorted([emp1, emp2, emp3], key=lambda e: e.age)

print("Sorted" , sorted_employees)



set1 = {1, 2, 3}
set1.add(4)
set1.add(4)
print(set1)