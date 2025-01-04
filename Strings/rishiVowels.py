count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
name = input("Enter your name: ")
for each_letter in name:
    for each_vowel in vowels:
        if each_letter == each_vowel:
            count += 1
print("Out of {} letters, {} has {} vowels".format(len(name), name, count))
print(f"No of Vowels {count}")
    