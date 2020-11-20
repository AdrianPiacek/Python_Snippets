# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.


#Brute force way of doing it
def first_unique_char(string):
    for index,i in enumerate(string):
# bcs function is looping through chars chronologically first occurrence with count 0 is result
        if string.count(i) == 1:
            return index
    return -1
print(first_unique_char("alphabet"))
print(first_unique_char("barbados"))
print(first_unique_char("crunchy"))
print()

import collections
def first_unique_char_alterantive1(string):
    #Creates dictionary with characters and their occurrence
    count = collections.Counter(string)
    print(count)
    for index, char in enumerate(string):#enumerate makes it possible to return index without creating temporary var
        if count[char] == 1:
            return index

print(first_unique_char_alterantive1("alphabet"))
print(first_unique_char_alterantive1("barbados"))
print(first_unique_char_alterantive1("crunchy"))
