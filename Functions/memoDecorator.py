# Write a decorator function to memoize a calculation


def memoize(func):
    cache = {}

    def memorize_result(*args):  # args are tuple here
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result  # tuple is used as key (immutable)
            return result

    return memorize_result


@memoize
def add(a, b):
    return a + b


print(add(2, 3))
print(add(2, 3))  # Return cached result
print(add(2, 4))  # Computes again since change of args
