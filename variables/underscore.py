# 1)Use in Intrepreter just like a variable
""" >>> 5 + 4
9
>>> _     # stores the result of the above expression
9 """

## 2) ignoring a value
a, _, b = (1, 2, 3)  # a = 1, b = 3
print(a, b)

## ignoring multiple values
## *(variable) used to assign multiple value to a variable as list while unpacking
## it's called "Extended Unpacking", only available in Python 3.x
a, *_, b = (7, 6, 5, 4, 3, 2, 1)
print(a, b)

## 3) Looping
## lopping ten times using _
for _ in range(5):
    print(_)

## 4. Separating Digits of Numbers
## different number systems
## you can also check whether they are correct or not by coverting them into integer using "int" method
million = 1_000_000
binary = 0b_0010
octa = 0o_64
hexa = 0x_23_AB

# 5. Single Preunderscore Value - For Internal Use can't be imported
## filename:- my_functions.py


def func():
    return "datacamp"


def _private_func():
    return 7


""" >>> import my_functions
>>> my_functions.func()
'datacamp'
>>> my_functions._private_func() """


## 6. post underscore single
# To use python keywords as variables or function names
def function(class_):
    pass


##  7. Double Pre Underscore
# Double Pre Underscores are used for the name mangling.
class SecondClass(Sample):

    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden"
        self.__c = "overridden"


obj2 = SecondClass()
print(obj2.a)
print(obj2._b)
print(obj2.__c)  # This will be renamed to _SecondClass__c
print(dir(SecondClass))


# Double Pre underscore for method names
class SimpleClass:

    def __datacamp(self):
        return "datacamp"

    def call_datacamp(self):
        return self.__datacamp()


obj = SimpleClass()
print(obj.call_datacamp())  ## same as above it returns the Dobule pre underscore method
print(obj.__datacamp())
