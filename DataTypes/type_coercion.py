num = 24
decimal = 33.0987
name = "Meghnadh"
str_num = "77"

print(num + int(str_num))
print(str(num) + str_num)

print(num + decimal)  # Result is float


################################################

# Decimal Precision and round off's
# 1) Give me nearest round off
rounded = decimal.__ceil__
print(rounded())

################################################
import math

rounded = math.ceil(decimal)
print(rounded)
a = math.floor(decimal)
print(a)
