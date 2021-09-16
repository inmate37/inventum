#-------------------------------------------------------------------------|
# 1.0 | [SRP]: BAD
#
I__DESCRIPTION: [
'''
    1 Class = 1 Responsibility
    If a class has more than 1 respon, change to 1 respon results to modification of other respon
'''
]
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass

II__WHATS_WRONG: [
'''
    The [Animal] class violates the [SRP]

    [SRP] states that classes should have 1 respon, here we can draw out 2 respons:
        1) Animal [DB] management
        2) Animal properties management

    The [__init__] and [get_name] manage the [Animal] properties while the [save] manages the [Animal] storage on a [DB]

    How will this design cause issues in the future ?
    If the app changes in a way that it affects [DB] management functions
    The classes that make use of [Animal] properties will have to be touched and recompiled to compensate for the new changes

    It’s like a domino effect, touch 1 card it affects all other cards in line
'''
]
#-------------------------------------------------------------------------|
# 1.1 | [SRP]: GOOD
#
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass

class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
[
'''
    When designing our [Classes], we should aim to put related features together
    So whenever they tend to change they change for the same reason
    And we should try to separate features if they will change for different reasons
'''
]
#-------------------------------------------------------------------------|
# 2.0 | [OCP]: BAD
#
I__DESCRIPTION: [
'''
    Adding [NewFunctionality] without changing [ExistingCode]
    If a class has more than 1 respon, change to 1 respon results to modification of other respon
'''
]
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

animals = [
    Animal('Lion'),
    Animal('Mouse'),
    Animal('Snake')
]
def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'Lion':
            print('roar')
        elif animal.name == 'Mouse':
            print('squeak')
        elif animal.name == 'Snake':
            print('hiss')

animal_sound(animals)

II__WHATS_WRONG: [
'''
    Function [animal_sound] does not conform to [OCP] because it cannot be closed against new kinds of [Animals]

    If we add new animal [Snake] we have to modify the [animal_sound] function
    For every new [Animal] new logic is added to the [animal_sound] function

    If statement would be repeated over and over again in the [animal_sound] function each time new [Animal] is added
'''
]
#-------------------------------------------------------------------------|
# 2.1 | [OCP]: GOOD
#
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self): return 'roar'

class Mouse(Animal):
    def make_sound(self): return 'squeak'

class Snake(Animal):
    def make_sound(self): return 'hiss'

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)
[
'''
    Animal now has a virtual method make_sound. We have each animal extend the [Animal] class and implement the virtual [make_sound] method
    Every [Animal] adds its own implementation on how it makes a sound in the [make_sound]
    The [animal_sound] iterates through the array of animal and just calls its [make_sound] method
    Now, if we add a new [Animal], [animal_sound] doesn’t need to change
    All we need to do is add the new animal to the animal array
    [animal_sound] now conforms to the [OCP] principle
'''
]
#-------------------------------------------------------------------------|
# 3.0 | [_____]: GOOD
#
#-------------------------------------------------------------------------|
# 3.1 | [_____]: GOOD
#
#-------------------------------------------------------------------------|
# 4.0 | [_____]: GOOD
#
#-------------------------------------------------------------------------|
# 4.1 | [_____]: GOOD
#
#-------------------------------------------------------------------------|
# 5.0 | [_____]: GOOD
#
#-------------------------------------------------------------------------|
# 5.1 | [_____]: GOOD
#
#-------------------------------------------------------------------------|
# Int | Signed vs Unsigned
#
Signed   | Positive or Negative
Unsigned | Positive only

#-------------------------------------------------------------------------|
# [List] vs [Array]
#
r1 = [1, 'one', {'two': 2}] # List

from array import array as arr
r2 = arr('i', [1,2,3])               # Array | [i] = signed Int, [I] unsigned Int
r2 = arr('b', ['one','two','three']) # Array | [b] signed Char, [B] unsigned Char

List  | stores different-type data
Array | stores      same-type data

#-------------------------------------------------------------------------|
# Objects [UniqueID]
#
id(Object)

All [Objects] has its own [UniqueID]
Assigned to [Object] when created

id is [Object] memory-address and will be different for each time program runs
except for [Objects] that has a constant [UniqueID] like Int from [-5] to [256]

#-------------------------------------------------------------------------|
# [ShallowCopy] vs [DeepCopy]
#
from copy import copy     # [ShallowCopy]
from copy import deepcopy # [DeepCopy]

POINT:
[
    |-----------------------------|-----------------------------------------------------------------------------|
    | Assignment  (=)             | will simply point [newVar] towards existing object                          |
    | ShallowCopy (copy.copy)     | will create [newObj], but [innerObj] will point towards [existingObj]       |
    | ShallowCopy (r2 = r1[:])    |                                                                             |
    | ShallowCopy (r2 = list(r1)) |                                                                             |
    | DeepCopy    (copy.deepcopy) | will create [newObj], and new [innerObj]                                    |
    |-----------------------------|-----------------------------------------------------------------------------|
]
NOTE:
[
    Difference occurs with [nestedStructures] only
]
DEEPDIVE:
[
    >>> r1 = [1,2,3]  # [List1] refers to [Obj1] in memory with address = 140448033652032
    >>> r2 = r1       # [List2] refers to [Obj1] in memory with address = 140448033652032
    >>> r1 is r2      # True | If [r1] changes, [r2] will be changed as well, vice-versa

    >>> r1 = [1,2,3]  # [List1] refers to [Obj1] in memory with address = 140448031834624
    >>> r2 = r2[:]    # [List2] refers to [Obj2] in memory with address = 140448032804608
    >>> r1 is r2      # False | If [r1] changes, [r2] won't be changed, vice-versa

    >>> r1 = [1,2,3]  # [List1] refers to [Obj1] in memory with address = 140448031835968
    >>> r2 = list(r1) # [List2] refers to [Obj2] in memory with address = 140448031835996
    >>> r1 is r2      # False | If [r1] changes, [r2] won't be changed, vice-versa

    >>> r1 = [1,2,3]
    >>> r2 = copy(r1)
    >>> r3 = deepcopy(r1)
    >>> id(r1) # 140377280532800
    >>> id(r2) # 140377279547584
    >>> id(r3) # 140377279610688

    >>> r1 = [1, 2, [4,5,6]]
    >>> r2 = copy(r1)
    >>> r3 = deepcopy(r1)
    >>> id(r1) # 140377280532800
    >>> id(r2) # 140377279547584
    >>> id(r3) # 140377279610688
    >>>
    >>> r1[2].append(6)
    >>> r1 # [1, 2, [3, 4, 5, 6]]
    >>> r2 # [1, 2, [3, 4, 5, 6]]
    >>> r3 # [1, 2, [3, 4, 5]]
]
#-------------------------------------------------------------------------|
# Method Resolution Order (MRO) / New algo (since Python3)
#
NOTE: In Python3: class A: pass == class A(object): pass, all classes inherites from base class (object) by default

#---------------------------------|
# 1 | Legacy-style
#
class A: x = 'a'
class B(A): pass
class C(A): x = 'c'
class D(B, C): pass

>>> D.x # 'a'
>>> D.__mro__
# <class '__main__.D'>
# <class '__main__.B'>
# <class '__main__.A'>
# <class '__main__.C'>
# <class '__main__.A'>

'DiaomondProblem': '''
    |---------|
    |    A    |
    | B  +  C |
    |    D    |
    |---------|
'''
#---------------------------------|
# 2 | New-style
#
class A: x = 'a'
class B(A): pass
class C(A): x = 'c'
class D(B, C): pass

>>> D.x # 'c'
>>> D.__mro__
# <class '__main__.D'>
# <class '__main__.B'>
# <class '__main__.C'>
# <class '__main__.A'>

#-------------------------------------------------------------------------|
# Array (Order-keeping datatype)
#
?
Ordered (Does keep input-order) / r1=arr('i', [3,2,1]) -> array('i', [3,2,1])
Following datatypes: int, float can be stored in list
Supports single datatype within 1 array

from array import array as arr


#-------------------------------------------------------------------------|
# Frozenset (Immutable set)
#
|------------|----------------------------------------------------------|
| Datatype   | frozenset                                                |
|            |                                                          |
| Itself     | Immutable (Hashable)                                     |
| InputOrder | |
|            |                                                          |
| CanStore   | |
|            | |
|            |                                                          |
| MixedTypes | |
| Example    | |
|------------|----------------------------------------------------------|


#-------------------------------------------------------------------------|
# Tuple (Order-keeping datatype)
#
Immutable / Hashable
Ordered (Does keep input-order) / r1=(3,2,1) -> (3,2,1)
Following datatypes: [Any] can be stored in tuple
Supports mixed datatypes within 1 tuple


|------------|----------------------------------------------------------|
| Datatype   | list                                                     |
|            |                                                          |
| Itself     | Mutable (Unhashable)                                     |
| InputOrder | Ordered (Does keep input-order) | r1=[3,2,1] >>> [3,2,1] |
| ByIndex    | True                                                     |
|            |                                                          |
| CanStore   | int, float, str, bool, tuple                             |
|            | list, dict, set                                          |
|            |                                                          |
| MixedTypes | Supports mixed datatypes within 1 list                   |
| Example    | r1=[1, 1.0, '1', True, (1,), [1], {1}, {1:1}]            |
|------------|----------------------------------------------------------|


#-------------------------------------------------------------------------|
# Dict (Order-keeping & KeyValue datatype)
#
Ordered (Does keep input-order) / r1={3:3,2:2,1:1} -> {3:3,2:2,1:1}
Following datatypes: [Any] can be dict values
Following datatypes: [Immutable/Hashable1] can be dict keys
Supports mixed datatypes within 1 dict

# OrderedDict
No need in OrderedDict since Python3.7 all dict are now OrderedDict

#-------------------------------------------------------------------------|
# Set (Unique-values datatype)
#
Unordered (Doesnt keep input-order) / r1={3,2,1} -> {1,2,3}
Following datatypes: [Immutable/Hashable] can be stored in set
Supports mixed datatypes within 1 set
Stores only unique values

>>> r1 = set((1,1,'2', True, 1.2))  # {1, '2', 1.2}
>>> r1 = set((1,1,'2', False, 1.2)) # {False, 1, '2', 1.2}
>>>
>>> r1 = {1, 'two', True}      # {'two', 1}
>>> r2 = set((1, 'two', True)) # {'two', 1}

# UseCase:
>>> r1 = [5, 3, 2, 4, 1]
>>> r2 = list(set(r1)) # [1, 2, 3, 4, 5]

>>> r1 = set((1, 2, 3)) # {1, 2, 3}
>>> r1.add(4)           # {1, 2, 3, 4}
>>> r1.pop()            # 1
>>> r1.pop()            # 2
>>> r1                  # {3, 4}
>>> r1.discard(4)       #
>>> r1                  # {3}

# ValueAccess:
Cannot access individual values in set, only all at once, like:
>>> days = set(('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']))
>>> for day in days:
>>>    print(day)

#-------------------------------------------------------------------------|
# Mutable vs Immutable 
#
Mutable   | List, Dict, Set
Immutable | Tuple, Frozenset, Integer, Float, String, Boolean

# Hashable (Immutable)
object is hashable if has hash value which never changes during its lifetime
it needs __hash__() method
Hashable objects which compare equal must have same hash value
Hashing is a concept in computer science which is used to create high performance,
pseudo random access data structures where large amount of data is to be stored and accessed quickly

#-------------------------------------------------------------------------|
# EPAM
#
# Mutable and Immutable Types - correct examples of immutable types; int snippet -  fails; list snippet - correct; list snippet with [:] - does not know that [:] creates shallow copy
# Deep vs Shallow Copy - ok
# Is vs == - ok
# Dict keys - “int keys are not good keys”;  does not know about immutable types here
# Hash Table - does not know how it organised and works
# Iterator - does not know
# Generator - knows about memory consumption; does not know about return value of yield
Context manager - very shallow understanding
# Thread vs Process - visible in task manager; very shallow understanding
# GIL - very shallow understanding
Name mangling - ok
Several methods with the same name in scope of one class - ok
super() - does not know
# MRO - does not know
# Django ORM: select_related vs prefetch_ related - ok
# Docker - has not had any experience
Git merge vs rebase - does not know

Coding tasks:
The most frequent element in the list - very unoptimised dictionary based solution  has been implemented in very slow manner; adding new (key, value) to the list via dict.update();
Custom generator - quick and confident; optimisation after hint
