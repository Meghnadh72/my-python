a = input("Enter a string\n")
b = input("Which value do you want to check ? \n")
if b in a:
    print(f"{b} is in {a} ")
else:
    print(f"{b} is not in {a}")