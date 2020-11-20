#Objective is to swap two numbers in separate variables without the use of temporary variable

a = 15
b = 33

print("Value of a = %d\nValue of b = %d" % (a,b))

a,b = b,a

print("Value of new a =%d\nValue of new b = %d" % (a,b))
