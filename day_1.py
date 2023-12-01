import re

input_str = 'nqninenmvnpsz874'
# using re.search()
# first_digit = re.search(r'\d', input_str)
# print(first_digit)

# using re.findall()
str_digits = re.findall(r'\d+', input_str)[0]
print(str_digits)

if str_digits:
    first_digit = str_digits[0]
    print(first_digit)
    last_digit = str_digits[-1]
    print(last_digit)
    input_str_calibration_value = [first_digit+last_digit,]

print(input_str_calibration_value)

