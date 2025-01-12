def romanToInt(s):
        romans_to_subtract = ['I','X','C']
        roman_value_dict = {
            'I' : 1, 'V' : 5, 'X':10, 'L': 50, 'C':100,'D':500,'M': 1000
        }
        sub_flag = False
        decimal_value = 0
        number = 0
        skip = False
        for index, roman_numeral in enumerate(s):
            if skip:
                skip = False
            else:
                decimal_value = roman_value_dict[roman_numeral]
                try:
                    next_value = roman_value_dict[s[index+1]]
                    if next_value > decimal_value:
                        decimal_value = next_value - decimal_value
                        number += decimal_value
                        skip = True
                    else:
                        number += decimal_value
                except IndexError:
                    number += decimal_value
                
        return number

decimal = romanToInt("III")
print(decimal)