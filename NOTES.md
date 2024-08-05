// NOTES.md

# Object-Oriented Programming 2 Notes

## Inheritance
Inheritance is the process where one classes inherits attributes and methods from another class. While some languages such as Java prohibit it, classes can inherit from multiple parent classes. (In general, classes usually only inherit from one class)

* Inheritance describes an _Is-A_ relationship.
* A _deck_ __is a__ _group of cards_ and the _hand_ __is a__ _group of cards_. However, a _deck_ __is NOT a__ _hand_.
* __Abstract Classes__ (as opposed to concrete classes) are never instantiated by themselves. These classes are written solely for the purpose of inheritance. Oftentimes, these classes have __abstract methods__ which cannot fully function within the Abstract Class; instead, they rely on data in the respective sub-classes.
* Inheritance often reveals itself during the design process when multiple classes have similar attributes or methods.

```python
class Mammal: # abstract parent class

    def __init__(self, genus, species, common_name):
        self.genus = genus
        self.species = species
        self.name = common_name
        self.cry_sound = None

    def setCry(self, sound):
        self.cry_sound = sound

    def Cry(self):
        return self.cry_sound

class Dog(Mammal): # Concrete child class

    def __init__(self, common_name):
        Mammal.__init__("Canis", "Lupis", common_name)
        self.setCry("Bark!")

    def playFetch(self):
        pass

class Cat(Mammal): #concrete child class

    def __init__(self, common_name):
        Mammal.__init__("Felis", "Catus", common_name)
        self.setCry("Meow")

    def takeNap(self):
        pass

HUSKY = Dog("Husky")
SIAMESE = Cat("Siamese")
HUSKY.cry # return Bark!
HUSKY.cry # return Meow
```

## Public, Private, and Semi-Private attributes and methods
Python is an open object-oriented programming language, which means that attributes and methods are public by _default_. Therefore, the rest of the program can access attributes and methods without an interfacing method. (Objects in python lack encapsulation by default). Python uses the underscore character to indicate whether an attribute or method is public, private, or semi-private.
*__Public__ properties do not require underscores at the start of the property name. In general, attributes should never be public, and only specific methods that manipulate attributes or retrieve values should be public.
```python
class Main:
    def __init__(self):
        self.__value = "hello world" # private attribute
        
    def getValue(self):
        #public method
        return self.__value
```
* __Private__ properties are not accessible outside the project. To indicate that a property is private _two underscores- are used at the beginning of the attribute or method name.
* NOTE: Magic Variables are not the same as private attributes.
```python
class Main:
    def __init__(self):
        self.public = "hello"
        self.__private = "world"    

    def publicMethod(self):
        return self.__private
        
    def __privateMethod(self):
        return self.public + self.__private
```

* Semi-private properties (a.k.a partially-protected) are visible to subclasses for the class (but not the child of the child class). Semi-private properties are still inaccessible to the rest of the program.
```python
class Main:
    def __init__(self):
        self.public = "hello"
        self.__private = "world"
        self._semiprivate = "hello world"

class SubClass(Main):
    def __init__(self):
        Main.__init__()
        
    def newMethod(self):
        self._semiprivate = "new text "
        self.public = "new hello"
        # updates the attributes in main
    def newMethod2(self):
        self.__private = "new world"
        # create a new variable in SubClass instead of overwriting the values in Main. 

```

## Polymorphism 
Polymorphism is the ability to have the same methods in different classes that may modify an inherited method to perform specific tasks in the subclass. Oftentimes, the tasks of each sub-class are similar, but require modifications to operate as expected.

The primary advantage of polymorphism is a reduction in complexity in the main program code. By using the same method names for similar types of objects, the objects can be easily switched in the program and other team members will understand what the intended effect is.

```python
class Main:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def setXY(self, x, y):
        self.__x = x
        self.__y = y

class SubClass:
    def __init__(self, x, y):
        Main.__init__(self, x, y)
    
    def setXY(self, x, y):
        # make all values >= 0
        x = x
        y = y
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        Main.setXY(self, x, y)
```

By preserving the name of the method, during development, multiple versions of the same method can be prototyped before finalizing the source code without having to change code in the main program code. 







