""" Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede" """


# Two Pointers # Strings
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        first_pointer = 0
        second_pointer = len(s) - 1
        str_list = [char for char in s]
        for first_pointer, value in enumerate(s):
            if first_pointer == second_pointer:
                return "".join(str_list)
            if value in vowels:
                for index in range(second_pointer, -1, -1):
                    if index == first_pointer:
                        return "".join(str_list)
                    if s[index] in vowels:
                        temp = str_list[first_pointer]
                        str_list[first_pointer] = str_list[index]
                        str_list[index] = temp
                        second_pointer = index - 1
                        break

        return "".join(str_list)
