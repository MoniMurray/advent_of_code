import re

input_str = "nqninenmvnpsz874 8twofpmpxkvvdnpdnlpkhseven4ncgkb six8shdkdcdgseven8xczqrnnmthreecckfive"

strings_by_line = input_str.split(' ')
print(input_str.split())

# using re.search() not perfect!
# first_digit = re.search(r'\d', input_str)
# print(first_digit)
# last_digit = re.search(r'\d$', input_str)
# print(last_digit)

# input_str_calibration_value = [first_digit.int(), last_digit.int()]


# using re.findall() works beautifully
# str_digits = re.findall(r'\d+', input_str)[0]
# print(str_digits)

# if str_digits:
#     first_digit = str_digits[0]
#     print(first_digit)
#     last_digit = str_digits[-1]
#     print(last_digit)
    
# input_str_calibration_value = [first_digit+last_digit,]

# print(input_str_calibration_value)

# create a loop to step through strings_by_line's list of strings, adding the first and last digits from each string to the input_str_calibration_value list with each iteration of the loop

for i in input_str:
    str_digits = re.findall(r'\d', i)
    print(str_digits)

#     if str_digits:
#         first_digit = str_digits[0]
#         print(first_digit)
#         last_digit = str_digits[-1]
#         print(last_digit)
    
#     input_str_calibration_value = [first_digit+last_digit,]

# print(input_str_calibration_value)


