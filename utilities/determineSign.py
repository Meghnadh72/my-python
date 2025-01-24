import math

num = 0
sign = math.copysign(1, num)

print(sign)

# Compare two numbers and determine their sign
a = -1
b = -1
signa = math.copysign(1, a)
signb = math.copysign(1, b)
if signa == signb:
    print("Same Sign")
else:
    print("Different sign")
