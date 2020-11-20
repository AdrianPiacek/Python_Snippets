# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse_integer(x):
    string_x = str(x)
    if string_x[0] == '-':
        #conversion to integer is rather optional but due to function name it is applied
        return int('-' + string_x[:0:-1])
    else:
        return int(string_x[::-1])


print(reverse_integer(-543))
print(reverse_integer(123))

"""Explanation: 
- Slices have third parameter set by default to 1, thus in reverse string manipulation stride of -1 is required.
- First character determines whether number is positive or not.
"""




