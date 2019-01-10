"""print("Hello  phiwa")
print("Spam and Eggs...")
2+2
2*(3+4)
input("Enter number:")
print("phiwayinkosi")

"VICTOR"+'NGEMA'
print("phiwa"+","+"ngema")
print("spam"*3)

print(float(input("enter number:"))+float(input("enter number:")))

if 10>5:
    print("mongezi")

x=4
if x==5:
    print("yes")
else:
    print("No")


i=1

while i<=5:
    print(i)
    i+=1

print("finished")

words=["hello","phiwa","!"]

print(words[0])
print(words[1])
print(words[2])

nums=[1,2,3]
nums.append(4)
print(nums)

def luc():
    print("spam")
    print("spam")
    print("spam")

luc()

def add_numbers(x,y):
    total=x+y
    return total
    print("this won't be printed")

print(add_numbers(4,5))

def func(x):
    res=0
    for i in range(x):
        res+=i
    return res
print(func(4))

for i in range(3):
    print(i)
"""


"""
try:
    num1=7
    num2=0
    print(num1/num2)
    print("calculation done")
except ZeroDivisionError:
        print("Error occured")
        print("due to ZeroDivisionError")

try:
    num=4
    print("phiwa"+num)
except:
    print("different data types") """
"""
print(1)
raise ValueError
print(2)"""

"""
name="123"
raise NameError("can't collect the number")
"""
"""try:
    num=5/0
except:
    print("An error occured")
raise
"""
#myfile=open("phiwa.txt") #opening and closing the file
#myfile.close()
"""
#write mode

open("phiwa.txt","r+")"""
#binary write mode
#open("phiwa.txt","wb")


#Reading a content in the file 
#file=open("phiwa.txt","r")       OR
"""file=open("phiwa.txt")
cont=file.read()
print(cont)
file.close()"""
#print(open("phiwa.txt","r"))
"""
opening=open("phiwa.txt")
print(opening.read())
opening.close()"""
                #READING FILES
opening=open("phiwa.txt")
print(opening.read(20))
opening.close()
            #WRITING A FILE
file=open("phiwa.txt","w")
file.write("the multi-billionaire")
file.close()

filee=open("phiwa.txt","r")
print(filee.read())
filee.close()

            #WRITING FILES
msg="Hello Phiwayinkosi"
files=open("phiwa.txt","w")
amountwritten=files.write(msg)
print(amountwritten)
files.close()

            #NONE
def phiwa():
    print("phiwa")

var=phiwa()
print(var)

            #DICTIONAIRES
#Each element in a dictionary is represented by a key:value pair
ages ={"Dave":24,"Mary":50,"Mr":30}
print(ages["Dave"])
print(ages["Mr"])
'''
test={}
print(test[0])
'''
            #DICTIONAIRES FUNCTIONS
squares={1:1,2:4,3:'error',4:16}
squares[8]=64
squares[5]=9
print(squares)
#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
            #USING GET IN DICTIONAIRES
fib={1:1,2:1,3:2,4:3}
print(fib.get(7,5))
print(fib)


            #LIST SLICES
square=[0,1,2,3,5,8,4,9,10,11]
print(square[2:6])
print(square[0:1])
print(square[:3])
print(square[6:])
print(square[::2])
print(square[2:6:3])
print(square[1:-2])
print(square[::-1])

sqs=[0,1,4,9,16,25,36,49,64,81]
print(sqs[7:5:-1])

            #List Comprehensions
cubes=[i**3 for i in range(5)]

print(cubes)

            #String Formatting
print("{0}{1}{0}".format("abra","cad"))

'''Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.'''
            #Strings Functions
print(",".join(["phiwa","victor","ngema"]))
print("Hello ME".replace("ME","world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence".endswith("sentence"))
print("this is a sentence".upper())
print("AN ALL CAPS SENTENCE".lower())
print("spam,eggs,ham".split(","))
                #Numeric Functions
'''To find the maximum or minimum of some numbers or a list, you can use max or min.
To find the distance of a number from zero (its absolute value), use abs.
To round a number to a certain number of decimal places, use round.
To find the total of a list, use sum. '''
                #list functions
nums=[55,44,33,22,11]

for v in enumerate(nums):
    print(v)

numss=[-1,2,-3,4,-5]
if all([abs(i)<3 for i in nums]):
    print(1)
else:
    print(2)


numm=(55,44,33,22)
print(max(min(numm[:2]),abs(-42)))

            #Functional Programming
'''Functional programming is a style of programming that (as the name suggests) is based around functions.  '''
def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five,10))
#The function is not pure, because it changed the state of some_list.

            #Lambdas
'''They can only do things that require a single expression
- usually equivalent to a single line of code '''
    #named function
def polynomial(x):
    return x**2+5*x+4

print(polynomial(-4))
   #lambda
print((lambda x:x**2 + 5*x+4)(-4))

'''Lambda functions can be assigned to variables, and used like normal functions. '''
double=lambda x:x*2
print(double(7))

        #map
'''The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.  '''
nu=[11,22,33,44,55]
result=list(map(lambda x:x+5,nu))
print(result)
#To convert the result into a list, we used list explicitly.
            #GENERATORS
#Generators are a type of iterable, like lists or tuples
#They can be created using functions and the yield statement.

def countdown():
    i=5
    while i>0:
        yield i
        i-=1

for i in countdown():
    print(i)

'''they can still be iterated through with for loops. The yield statement is used to define a generator, replacing the return of a
function to provide a result to its caller without destroying local variables '''

'''Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage.
Furthermore, we do not need to wait until all the elements have been generated before we start to use them. '''

                        #RECURSION
# the base case is when we have 1!=1.The base case acts as the exit condition of the recursion.
                    #example of timeerror recursion
'''
def sum_to(x):
    return x+sum_to(x-1)

print(sum_to(5))
'''

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(4))

                    #SETS
#sets are data structures similar to lists or dictionaries
'''They are unordered, which means that they can't be indexed. 
They cannot contain duplicate elements.'''

nums={1,2,1,3,1,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

'''The union operator | combines two sets to form a new one containing items in either. 
The intersection operator & gets items only in both. 
The difference operator - gets items in the first set but not in the second. 
The symmetric difference operator ^ gets items in either set, but not both. '''

first={1,2,3,4,5,6}
second={4,5,6,7,8,9}

print(first|second)
print(first & second)
print (first-second)
print (second-first)
print(first^second)

#Python supports the following data structures: lists, dictionaries, tuples, sets.

#Use tuples when your data cannot change
#Use a set if you need uniqueness for the elements
#Use lists if you have a collection of data that does not need random access
                    #itertools
'''
The module itertools is a standard library that contains several functions that are useful in functional programming. 
One type of function it produces is infinite iterators. 
The function count counts up infinitely from a value. 
The function cycle infinitely iterates through an iterable (for instance a list or string). 
The function repeat repeats an object, either infinitely or a specific number of times.
'''



from itertools import product,accumulate,takewhile
numsr= list(accumulate(range(8)))
print(numsr)
print(list(takewhile(lambda x:x<=6,numsr)))
'''
a={1,2}
print(len(list(product(range(3),a))))'''

numb={1,2,3,4,5,6}
numb={0,1,2,3}&numb
numb=filter(lambda x:x>1,numb)
print(len(list(numb)))

def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
print(power(2,3))

                #classes
'''Classes are created using the keyword class and an indented block, which contains class methods (which are functions).  '''

''' __init__ this is called when an instance (object) of the class is created ,using the class name as a function'''
# Within a method definition, self refers to the instance calling the method
#. The __init__ method is called the class constructor.
class cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs


felix=cat("ginger",4)
rover=cat("dog-colored",4)
stumpy=cat("brown",3)

print(felix.legs)

class Dog:
    legs=4
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self): #always put self in parameters
        print("Woof!")


fido=Dog("Fido","brown")
print(fido.name)
fido.bark()
print (fido.legs)

                    #inheritance
#Inheritance provides a way to share functionality between classes.

class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fidoo=Dog("Fido","brown")
print(fidoo.color)
fidoo.bark()


class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c=C()
c.method()
c.another_method()
c.third_method()
                #Magic Methods
#Magic methods are special methods which have double underscores at the beginning and end of their names. 
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector2D(self.x + other.x,self.y+other.y)

first=Vector2D(5,7)
second=Vector2D(3,9)

result=first+second
print(result.x)
print(result.y)
'''
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
'''
                    #Object Lifecycle
'''
The first stage of the life-cycle of an object is the definition of the class to which it belongs.
The next stage is the instantiation of an instance, when __init__ is called.
Memory is allocated to store the instance. Just before this occurs, the __new__ method of the class is called.
This is usually overridden only in special cases.
'''
class Queue:
    def __init__(self,contents):
        self._hiddenlist=list(contents)

    def push(self,value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue=Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

            #data handling
'''
The purpose of this isn't to ensure that they are kept private,
but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name.
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
'''

class Spamm:
    __egg=7

    def print_egg(self):
        print(self.__egg)

s=Spamm()
s.print_egg()
print(s._Spamm__egg) #any defined class name 
#print(s.__egg)

            #OOP
class Employee:
    raise_amount=1.04
    num_of_employee=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.'+ last + '@company.com'

        Employee.num_of_employee+=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod

    def set_raise_amt(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

    def __repr__(self): #used for debugging  and logging 
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self): #used for readable representation of an object and meet to be used as a display in the end-user
        return '{}-{}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
    
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

print(emp_1 + emp_2)

print (emp_1.fullname())
print(len(emp_1))
#another option
Employee.fullname(emp_1)

print(emp_1.__dict__)
emp_1.raise_amount=1.05

print(emp_1.raise_amount)
print(emp_1.num_of_employee)
Employee.set_raise_amt(1.07)
#Employee.raise_amount=1.06
print(emp_2.raise_amount)

emp_str_1='John-Doe-70000'
emp_str_2='Steve-Smith-30000'
emp_str_3='Jane-Doe-90000'

new_emp_1=Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)            


import datetime
my_date=datetime.date(2018,1,7)

print(Employee.is_workday(my_date))
#static method behave just like regular function there do not pass  class argument or self 

#print(help(new_emp_1))

dev_1=Developer('Corey','Schafer',5000,'Python')
dev_2=Developer('Test','Employee',6000,'Java')

print(dev_1.email)
print(dev_1.prog_lang) 


#print(emp_1)

#print(repr(emp_1))
#print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

'''
print(int.__add__(1,2)) # similar to 1+2
print(str.__add__('a','b')) #similar to a+b '''


class employee2:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last


    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first=None
        self.last=None
        
emp_1=employee2('John','Smith')
emp_1.fullname ='Corey Schafer'
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname


                #Properties
class Pizza:
    def __init__(self,toppings):
        self.toppings=toppings
        self._pineapple_allowed=False


    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter

    def pineapple_allowed(self,value):
        if value:
            password=input("Enter the password:")
            if password=="Sw0rdf1sh!":
                self._pineapple_allowed=value

            else:
                raise ValueError("Alert!Intruder!")

pizza=Pizza(["cheese","tomato"])

print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)



















