# The order of parameters assiging is
# Positional first and Key word args has always to be last.

""" Order of Arguments
The order in which arguments should be provided to the function is crucial:

Positional arguments come first.

Default arguments (=) follow.

*args are next.

Keyword arguments come after positional and default arguments.

**kwargs always come last. """


def example_func(pos1, pos2, kwarg1="default", *args, **kwargs):
    print(f"pos1: {pos1}, pos2: {pos2}, kwarg1: {kwarg1}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


print("----------------- FIRST FUNCTION-----------------")
example_func(1, 2, 3, 4, 5, kwarg2="value", kwarg3="another value")
print("----------------- SECOND FUNCTION-----------------")
example_func(1, 2, hi="Hi", hello="Hello")
print("----------------- THIRD FUNCTION-----------------")
example_func(
    1, 2, "Overridden using position", 4, 5, kwarg0="kwarg0", hi="Hi", hello="Hello"
)

""" 
Output
pos1: 1, pos2: 2, kwarg1: 3
args: (4, 5)
kwargs: {'kwarg2': 'value', 'kwarg3': 'another value'} 
"""


"""Mutiple Ways to Provide Default Values"""


# USing Decorators
def with_defaults(func):
    def wrapper(name, greeting=None):
        if greeting is None:
            greeting = "Hello"
        return func(name, greeting)

    return wrapper


@with_defaults
def greet(name, greeting):
    return f"{greeting}, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!

# Using functools partial
from functools import partial


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


custom_greet = partial(greet, greeting="Hi")

print(custom_greet("Alice"))  # Output: Hi, Alice!
