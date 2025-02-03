avg = 1.5
num, deci = str(avg).split(".")
print(deci)
if len(deci) > 5:
    avg = float(num + "." + deci[:5])
else:
    diff = 5 - len(deci)
    s = str(avg)
    for j in range(diff):
        s += "0"
    avg = float(s)
print(avg)
