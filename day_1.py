import re

input_str = "nqninenmvnpsz874 8twofpmpxkvvdnpdnlpkhseven4ncgkb six8shdkdcdgseven8xczqrnnmthreecckfive"

strings_by_line = input_str.split(' ')
print(strings_by_line)

# using re.search() not perfect!
# first_digit = re.search(r'\d', input_str)
# print(first_digit)
# last_digit = re.search(r'\d$', input_str)
# print(last_digit)

# input_str_calibration_value = [first_digit.int(), last_digit.int()]


# using re.findall() works beautifully
str_digits = re.findall(r'\d+', strings_by_line[0])[0]
print(str_digits)

if str_digits:
    first_digit = str_digits[0]
    print(first_digit)
    last_digit = str_digits[-1]
    print(last_digit)
    
input_str_calibration_value = [first_digit+last_digit,]

print(input_str_calibration_value)



