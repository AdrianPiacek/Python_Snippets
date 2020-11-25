#############################################################################################
# Exercise #1
# because the argument is list = [], that means that list is created
# during function declaration rather than function invocation
def extend_list(elemenet, list = []):
    list.append(elemenet)
    return list
# all calls of extend_list without specified list will append to only one list
list0 = extend_list(1)
list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')
print(list0, list1, list2, list3)

# How to modify extend_list to produce append for separate lists
def extend_list(element, list = None):
    if list is None:
        list = []
    list.append(element)
    return list
list0 = extend_list(1)
list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')
print(list0, list1, list2, list3)

#############################################################################################
# Exercise #2
def multipliers():
    return [lambda x : i*x for i in range(4)]

print(m(2) for m in multipliers())
# [6,6,6,6]
# expected output would be [0,2,4,6], but


#############################################################################################
# Exercise #3
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[10:]) # []
# This code will not result in the IndexError because it uses slicing and not indexing
print(list1[0:15]) # ['a', 'b', 'c', 'd', 'e'] it does not matter taht end index is higher

try:
    print(list1[15])
except IndexError:
    print("This causes an error because it is out of bounds.")

#############################################################################################
# Exercise #4
# What will be the output of following commands

list0 = [ [ ] ] * 5 #Creates 5 list that reference the same one, that is why all the rest is affected
print(list0) # [[],[],[],[],[]]
list0[0].append(10)
print(list0) # [[10],[10],[10],[10],[10]]
list0[1].append(20)
print(list0) # [[10,20],[10,20],[10,20],[10,20],[10,20]]
list0.append(30)
print(list0) # [[10,20],[10,20],[10,20],[10,20],[10,20], 30]

#If list is created with standard syntax it is different
list1 = [[],[],[],[],[]]
print(list1) # [[],[],[],[],[]]
list1[0].append(10)
print(list1) # [[10],[],[],[],[]]
list1[1].append(20)
print(list1) # [[10],[20],[],[],[]]
list1.append(30)
print(list1) # [[10],[20],[],[],[], 30]

#############################################################################################
# Exercise #5
# Given a list of N numbers, use a single list comprehension to produce a new list that only contains values that are
# a) even numbers
# b) are from elements in the original list that had even indices
list0 = [1,5,4,3,6,8,1,2,6,4]

#alternative using enumerate
new_list = [num for index,num in enumerate(list0) if num % 2 == 0 and index % 2 == 0]
print(new_list)

#simpler solution
new_list = [num for num in list0[::2] if num % 2 == 0]
print(new_list, end="\n\n\n")

#############################################################################################
# Exercise #6
# Write a function that prints the least integer that is not present in the given list
# However this integer can not be sum of other elements in the list either.
import itertools
def check_number_bigger_by_1(a,b):
    c = b - a
    if c <= 1:
        return False
    elif c > 1:
        return True


def check_sum_equals_number(input_list, number):
    sum = 0
    for i in range(len(input_list)):
        for j in  input_list[i]:
            sum += j
        if number == sum:
            return True
        else:
            sum = 0

    return False

def check_if_number_is_sum(number, list_slice):
    list_len = len(list_slice)
    for i in range(list_len):
        combinations = list(itertools.combinations(list_slice, i + 2)) # incerement by 2 because at least combination of 2
        if check_sum_equals_number(combinations, number) == True:
            return True
    return False

def find_least_number_missing(input_list):
    input_list = sorted(input_list) # needs to be sorted
    missing_number = - 1
    index = 0
    while index < len(input_list):
        if check_number_bigger_by_1(input_list[index], input_list[index+1]) == True:
            for i in range(1,input_list[index+1] - input_list[index]):
                missing_number = input_list[index] + i
                if check_if_number_is_sum(missing_number, input_list[0:index+1]) == False:
                    return missing_number

        index += 1
    return missing_number

list0 = [1,2,5,7] # least not included is 4
print(find_least_number_missing(list0))

#############################################################################################
a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print(sorted([a[s] for s in a]))

assert sum([1,2,3]) == 6, "Should be 6"
assert sum([1,2,8]) == 6, "Should be 6"

