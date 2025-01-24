s = "anviaj"


def longest_sub_string(s):
    string_formed = ""
    len_finished = 0
    sub_string_longest = ""
    for char in s:
        if char not in string_formed:
            string_formed += char
            if len(string_formed) > len(sub_string_longest):
                sub_string_longest = string_formed
        else:
            next_sub = string_formed[string_formed.find(char) + 1 :]
            possible_next_sub_len = len(next_sub)
            if possible_next_sub_len > len(string_formed):
                break
            else:
                string_formed = string_formed[string_formed.find(char) + 1 :]
                string_formed += char
        len_finished += 1
    return len(sub_string_longest)


print(longest_sub_string(s))
