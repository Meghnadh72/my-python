in_string = input("Enter your string to show alternate ascii strings")
print(in_string)
print(in_string[1])
in_string = bytes(in_string,'utf-8')
print(in_string[1])
#or 
for index in range(0,len(in_string),2):
    print(in_string[index]) 
