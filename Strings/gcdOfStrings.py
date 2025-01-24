# Leet Code Solution
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: gcd(len(str1), len(str2))]


# My Solution - 0ms
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Take length of string
        smaller_str = str1 if len(str1) < len(str2) else str2
        bigger_str = str2 if smaller_str == str1 else str1
        smaller_len = len(smaller_str)
        bigger_len = len(bigger_str)
        # First check the entire smaller string
        if bigger_len % smaller_len == 0:
            quotient = bigger_len // smaller_len
            if smaller_str * (quotient) == bigger_str:
                return smaller_str

        for number in reversed(range(2, math.ceil(smaller_len // 2) + 1)):
            if smaller_len % number == 0:
                small_quotient = smaller_len // number
                if bigger_len % number == 0:
                    big_quotient = bigger_len // number
                    if smaller_str[:number] * small_quotient == smaller_str:
                        if bigger_str[:number] * big_quotient == bigger_str:
                            if bigger_str[:number] == smaller_str[:number]:
                                return bigger_str[:number]
        return ""
