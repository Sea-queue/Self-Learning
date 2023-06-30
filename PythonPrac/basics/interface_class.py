"""
- its more of a personal preference than being a question of which is
better than the other.

Functional programming avoids changing state and mutable data.
In a functional program, the output of a function should always be
the same, given the same exact inputs to the function. This is called
eliminating side effects in your code.

The main deal with OOP is the ability to encapsulate data from outsiders
Encapsulation is the ability to hide variables within the class from
outside access, which makes it great for security reasons, along with
leaky, unwanted or accidental usage. 

Functional programming use immutable data;
Oject oriented uses the mutable data.
"""


"""
Why class:
To represent more complex data type:

Problems with list:
kirk = ["James Kirk", 34, "Captain", 2265]
mccoy = ["Leonard McCo", "Chief Medical Officer", 2266]

First, it can make larger code files more difficult to manage. You probably 
won't remember the what the data represent for each index.

Second, it can introduce errors if not every employees has the same 
number of elements in the list. In the Mccoy list above, the age is 
missing, so Mccoy[1] is not returning the age.

Class:
A great way to make this type of code more manageable and more 
maintainable is to use classes.

Classes are used to create user-defined data structures, Classes define
funtions called methods which identify the behaviors and actions that an
object created from the class can perform with its data.

While the class is the blueprint, an instance is an object that is built
from a class and contains real data. 
"""

"""
class key word.

Class VS Instance:
the properties that all Dog objects must have are defiend in a method
called .__init__(). Every time a new Dog object is created, .__init__()
sets the inital state of the object by assigning the values of the
object's properties.

you can give .__init__() any number of parameters, but the first 
parameter will always be a variale called self. When a new class instance
is created, the instance is automatically passed to the self parameter
in .__init__() so that new attributes can be defined on the object.

The indentation matters in Python.

Instance Attributes:
Attributes created in .__init__() are called instance attributes. An
instance attribute's value is specific to a particular instance of the 
class. 

Class attributes:
On the other hand, class attributes are attributes that have the same
value for all class instances. You can define a class attribute by 
assigning a value to a variable name outside of .__init__().
Class attributes are defiend directly beneath the first line of the class
name. They must be assigned an inital value. When an instance is created,
class attributes are automatically created and assigned to their inital
values. Use class attributes to define properties that should have the
same value for every class instance. Use instance attributes for 
properties that vary from one instance to another.
"""
class Dog:
    # Class attrubute
    species = "Canis"

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    # Instance method
    def description(self) -> str:
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound="lovuuuu"):
        return f"{self.name} says {sound}"


# instantiating an object.
pabels = Dog("pables", 15)

# access instance attributes with dot notation
print("pabels age: ", pabels.age)

"""
One of the biggest advantages of using classes to organize data is
that instances are guaranteed to have the attributes you expect. So
you can use those attributes with confidence knowing that they will
always return a value.

Cutom objects are mutatble be default. An object is mutable if it can
be altered dynamically. For example, Lists and Dictionaries are mutable
but string and tuples are immutable.
"""

"""
Instance Methods:
functions that are defined inside a class and can only be called from
an instance of that class. Just like .__init()__, an instance method's
first parameter is always self.
"""
print("about pabels: ", pabels.description())
print("pabels sound: ", pabels.speak("English"))


"""
When you print(pabels), you get a cryptic looking message telling you
that miles is a Dog object at the memory address 0x000fab34. This 
message isn't very helpful. You can chagne what gets printed by defining
a special instance method called .__str__().

Dunder methods:
Methods like .__init__() and .__str__() are called dunder methods because
they begin and end with double underscores. There are many dunder methods
that you can use to customize classes in Python.
"""
print("Dog object: ", pabels)


"""
Inherit from other classes in python:
Inheritance is the process by which one class takes on the attributes
and methods of another. Newly formed classes are called child classes,
and the classes that child classes are derived from are called parent class.

child class can override or extend the attributes and methods of parent
classes. 

To create a child class, you create new class with its own name and
then put the name of the parent class in parentheses.
"""

class JackRusselTerrier(Dog):
    def speak(self, sound="Arf") -> str:
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    def speak(self, sound="wocao") -> str:
        return super().speak()

class Bulldog(Dog):
    pass

luna = Bulldog("luna", 9)
jake = JackRusselTerrier("Jake", 1)
print("luna", luna)
# check which class a given object belongs to:
print("what is luna: ", type(luna))
# check if luna is also an instance of the Dog
print("is luna a Dog: ", isinstance(luna, Dog))
print("is jave a BullDog: ", isinstance(jake, Bulldog))

"""
Extend the functionality of a Parent Class:

To override a method defined on the parent class, you define a method
with same name on the child class.
"""
print("how jave talks: ", jake.speak())
print("how jake talks when angry: ", jake.speak("Grrr"))


"""
supert():
when you call super().speak(sound) inside a child class, python search 
the parent class, Dog, for a .speak() method and calls it with the 
variable sound.
"""
tico = Dachshund('tico', 8)
print("tico says: ", tico.speak("krrrr"))

""" 
Interface in Python:

Python's appraoch to interface design is somewhat different when 
compared to languages like Java, Go and C++. These languages all have 
an interface keyword, while python does not. Python further deviates
from other languages in one other aspect. It doesn't require the class
that's implementing the interface to define all of the interface's 
abstract methods.
"""


"""
Informal interfaces:
Incertain circumstances, you may not need the strict rules of a formal
Python interface. Python's dynamic nature allows you to implement an
informal interface. An informal Python interface is a class that defines
methods that can be overridden, but there's no strict enforcement.
"""

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extacting text."""
        pass
    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass

"""
These methods are defined but not implemented. The implementation will
occur once you create concrete classes that inherit from InformalParserInterface.

to use your interface, you must create a concrete class. A concrete class
is a subclass of the interface that provides an implementation of the 
interface's methods. you'll create two concrete classes to implement 
your interface. The first if PdfParser, which you'll use to parse the
text from PDF files:
"""
class PdfParser(InformalParserInterface):
    """Extract text from PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_soucre()"""
        pass
    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass
    
class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_soucre()"""
        pass
    
    def extract_text_from_email(self, full_file_path: str) -> dict:
        """
        A method defiend only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass

"""
So far you've defiend two concrete implementation of the 
InformalPythonInterface. However, note that EmlParser fails to
properly define .extract_text(). If you were to check whether EmlParser
implements InformalParserInterface, then you'd get both true
"""
# true
print("PdfParser is subclass: ", issubclass(PdfParser, InformalParserInterface))
# true
print("EmlParser is subclass: ", issubclass(EmlParser, InformalParserInterface))

"""
This would return True, which poses a bit of a problem since it violates
the definition of an interface.
"""

"""
Formal Interfaces:
Informal interfaces would the wrong approach for larger applications.
To create formal Python interface.

Using abc.ABCMeta
To enforce the subclass instantiation of abstract methods, 
"""

