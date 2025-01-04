""" a = int(input("enter a number"))
if  a % 5 == 0:
  print(f"{a} is  a muliple of 5")
else:
  print(f"{a} is not a muliple of 5")

 
 """

a = int(input("enter a number"))
s = str(a)
if s[-1] == '0' or s[-1] == '5':
    print(f"{a} is multiple of 5")
else:
    print(f"{a} is not mutiple of 5 ")
