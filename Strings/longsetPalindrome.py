def palindrome(strng):
    #print(f"checking {strng} is palindrome", end=" ")
    if strng[::-1] == strng:
        #print(": Yes")
        return True
    else:
        #print(": No")
        return False

str1 = "aabbaaccccccc"

substring = ""
largest = {"length": 0, 'string': ""}
for outer_index in range(len(str1)):
    substring = str1[outer_index]
    for inner_index in range(outer_index + 1,len(str1)):
        substring += str1[inner_index]
        if palindrome(substring):
            if len(substring) > largest["length"]:
                largest = {"length": len(substring), "string" : substring}

print(largest)
        