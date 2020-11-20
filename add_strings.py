# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
num1 = '364'
num2 = '1836'

def add_strings(num1, num2):
#we may not use direct conversion but function eval() is not direct conversion
    return str(eval(num1) + eval(num2))

print(add_strings(num1, num2))
print()


"""
Main difference in alternative solution is that ASCII representation is considered.
methods ord() convert character to its ASCII representation and in order to get corresponding
digit substraction of ascii value of 0 is required.

"""
def add_strings_alternative(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1 // 10 #decrementing of 10 to the power of

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2 // 10

    return str(n1 + n2)

print(add_strings_alternative(num1, num2))
