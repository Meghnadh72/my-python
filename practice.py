symbols = "HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG"
symbols.split(",")
print(symbols)

import copy

# Slicing List
a = [(2, 3), {2, 2}, [9, 0]]
b = a.copy()
c = copy.deepcopy(a)
print(a)

_ = 3
g = _
print(g)
a, *_, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, c)
b = 1_00_000
print(2 * b)


rishi = 10


def samplee():
    global rishi
    rishi = 12
    print(f"Inside function rsihi value is : {rishi}")


print(f"Before function rsihi value is : {rishi}")
samplee()
print(f"After function rsihi value is : {rishi}")
