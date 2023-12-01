import re

# use the splitlines() to read and split a file by lines
input_str = open("input.yml", "r")
strings_by_line = input_str.read()
print(strings_by_line.splitlines())
input_str.close()


# using re.findall() works beautifully
# str_digits = re.findall(r'\d+', strings_by_line)[-1]
# print(str_digits)

# if str_digits:
#     first_digit = str_digits[0]
#     print(first_digit)
#     last_digit = str_digits[-1]
#     print(last_digit)
    
# input_str_calibration_value = [first_digit+last_digit,]

# print(input_str_calibration_value)

# create a loop to step through strings_by_line's list of strings

str_digits = re.findall(r'\d+', strings_by_line)
input_str_calibration_value = []

for d in str_digits:
    
    first_digit = d[0]
    # print(first_digit)
    last_digit = d[-1]
    # print(last_digit)
        
    # add the first and last digits from each string line to the input_str_calibration_value list with each iteration of the loop, converting from str to int
    input_str_calibration_value.append(int(first_digit+last_digit))

# sum the list
star_1 = sum(input_str_calibration_value)
print(star_1)


