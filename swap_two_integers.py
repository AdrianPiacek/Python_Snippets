################################################################
# Objective is to swap two numbers in separate variables without the use of temporary variable
# Python assignment method
a = 15
b = 33
print("Value of a = %d\nValue of b = %d" % (a,b))
def swap_numbers_1(a,b):
    a,b = b,a
    return list([a, b])

new = swap_numbers_1(a,b)
print("Swap_1\na = {}\nb = {}".format(new[0],new[1]),end="\n\n")

################################################################
# Using addition and subtraction
# May result in temporary solution that may be out of integer range
a = 15
b = 33
def swap_numbers_2(a, b):
    a = a + b   # 15 + 33 = 48
    b = a - b   # 48 - 33 = 15
    a = a - b   # 48 - 15 = 33
    return list([a,b])
new = swap_numbers_2(a,b)
print("Swap_2\na = {}\nb = {}".format(new[0],new[1]),end="\n\n")

################################################################
# Using multiplication and division
# Method does not work if one of the numbers is 0
# May result in temporary solution that may be out of integer range
a = 15
b = 33
def swap_numbers_3(a, b):
    a = a * b   # 15 * 33 = 495
    b = a // b  # 495 // 33 = 15 --> integer division bcs reminder is useless
    a = a // b  # 495 // 15 = 33
    return list([a,b])
new = swap_numbers_3(a,b)
print("Swap_3\na = {}\nb = {}".format(new[0],new[1]),end="\n\n")

################################################################
# Using bit XOR
#   A   B   XOR
#   0   0   0
#   0   1   1
#   1   0   1
#   1   1   0
# Bits need to differ to achieve 1
a = 15  # 0000 1111
b = 33  # 0001 1111
def swap_numbers_4(a, b):
    a = a ^ b   #a = 0001 0000
    b = a ^ b   #b = 0000 1111
    a = a ^ b   #a = 0001 1111
    return list([a,b])
new = swap_numbers_4(a,b)
print("Swap_4\na = {}\nb = {}".format(new[0],new[1]),end="\n\n")

