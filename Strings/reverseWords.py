""" Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s. """


# 1st solution - 7ms (Worst Time)
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.strip().split(" ")
        result = ""
        from functools import reduce

        return reduce(lambda ss, ss1: ss.strip() + " " + ss1.strip(), reversed(ls))


from functools import reduce

str_of_words = "Hello I am Meghnadh"
list_of_words = reversed(str_of_words.strip().split(" "))
reverse = reduce(lambda a, b: a + " " + b, list_of_words)
print(reverse)
