#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 
sentence1 = 'We are really really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def matched_words(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
#symmetric difference !(A ^ B)
#intersection (A ^ B)
    return list(set1.symmetric_difference(set2)), list(set1.intersection(set2))

result = matched_words(sentence1, sentence2)
print(result, end="\n\n\n")


#############################################################################
# calculate number of appearences of each character
import pprint
a = 'Ako by nam bolo dobre keby soms a pripravoval o mesiac a pol skor.'
def count_chars(a):
    char_dictionary = {}
    for character in a:
        char_dictionary.setdefault(character,0) # creates new key if was not before with default 0
        char_dictionary[character] = char_dictionary[character] + 1 #increments
    return char_dictionary
pprint.pprint(count_chars(a))

#############################################################################
#Accessing key and value of dictionary at the same time in for loop
my_dict = {'name':'Ado', 'age': 26}
for key, val in my_dict.items():
    print("{} is key and {} is value".format(key,val ))

#############################################################################
#Print out version of the python you are using
import sys
print(sys.version)

#############################################################################
# Difference between extend and append
a = [1,2,3,4,5,6,7]
b = [8,9,10,11]
a.extend(b)
print(a)
c=[45,65]
a.append(c)
print(a)
print(','.join(str(i) for i in a))

#############################################################################
# for loops comprehensions
nums = [1,2,3,4,5,6,7,8,9,10]

my_list = [n*n for n in nums]
print(my_list)

my_list_1 = [n for n in nums if n%2==0]
print(my_list_1)

my_list_2 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list_2)

set_nums = [1,2,3,1,2,4,2,3,6,5,1,4,8,2,3,6,9,5,4,7,8,1,2,5]

my_set = set(n for n in set_nums)
print(my_set)

#############################################################################
import copy
di = {'dict1':{'name': 'ado'},
      'dict2':{'name': 'marek'}}
shallow_dic = di.copy()
print(shallow_dic)
# zmena v povodnom slovniku sa odrazi na kopirovanom objekte
di['dict1']['name'] = 'BOB'
print(shallow_dic, di)
# funguje to aj opacne.. ked zmenim kopiu tak zmenim aj povodny
shallow_dic['dict1']['name'] = 'Camila'
print(shallow_dic, di, end = '\n\n\n')
#je to preto lebo oba slovniky referencuju rovnaky objekt

from copy import deepcopy
deep_dic = deepcopy(di)
print(deep_dic)
di['dict1']['name'] = 'BOB'
print(deep_dic, di)
deep_dic['dict1']['name'] = 'Ondrej'
print(deep_dic, di)
# pri deepcopy sa to ale nestane lebo to uz neferencuje rovnaky objekt ale kazdy svoj

dicto= {'name':'ado'}
temp_1 = dicto.copy()
print(dicto, temp_1)
dicto['name'] = 'Martin'
print(dicto, temp_1)
# v ramci jednoduchych datovych struktur su ale copy a deepcopy uplne rovnake


#############################################################################
#how to reverse list
s = [10,20,30,5,50,66]
print(list(reversed(s)))    #alt 1
print(s[::-1])              #alt 2


#############################################################################
#print only elements that start with 'j'
names = ['jana','ondrej', 'marek', 'sergej', 'jakub','peto', 'julia']
names = [m for m in names if m[0].lower() == 'j']
print(names)

#############################################################################
# How many different characters are present in this string
a = "This is a sample string with many characters."
b = [1,3,5,4,8,6,4,1,2,3,5,6,9,8,4,5,1,2,6,3,5,4,7,8,9,6,5]
#alternative 1
print("List b obsahuje {} roznych prvkov".format(len(set(a))))
print("List b obsahuje {} roznych prvkov".format(len(set(b))))
import collections
#it is possible to creatte collection whose method can create dictionary
different_characters = collections.Counter(a)
print(len(different_characters))
print(different_characters)
print(different_characters.most_common(2)) # [(' ', 7 ), ('s', 5)]
print(different_characters.get('s')) # get number of occurrences of specific character
# Fidn out how many white spaces are inside the string
print("There is {} white space characters".format(different_characters[' ']))

#############################################################################
# How can you randomize items in the list
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Glog', 'Piece']
shuffle(x)
print(x) #it can not be printed and shuffle inside print for some unknown reason

# Write sorting algortihm for a numerical dataset
x = ['1', '4', '7', '2', '22', '11']
x = sorted([int(num) for num in x])
print(x)

#############################################################################
#factorial via recursion
def factorial(x):
    if x == 0:
        return 1;
    return x * factorial(x-1)
print(factorial(10), end="\n\n")

#############################################################################
#split string into separate elements and then recreatee sentence back
a = "This,is,a,sample string with many characters."
a = a.split(',')# spl
print(a)
a = ' '.join(a)
print(a, end="\n\n")

#############################################################################
# Bubble sort algortihm

def bubble_sort(unsorted_list):
    for j in range(len(unsorted_list)):
        for i in range(len(unsorted_list)-j-1): #-j is included to limit number of iterations when items at end are sorted
                if unsorted_list[i] > unsorted_list[i+1]:
                    unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]

a = [15,2,3,45,8,62,14,95,62,1,4,3]
bubble_sort(a)
print("Sorted by bubblesort {}".format(a), end="\n\n")

#############################################################################
# Write program to print christmass tree with asterixes

def create_tree(floors):
    for i in range(0, floors):
        print((floors-i-1) * ' ' ,(2*i+1) * '*')
create_tree(7)

#############################################################################
# Fibonacci series - review
def fibonacci_sequence(iterations):
    a, b = 0, 1

    for i in range(iterations):
        print(a, end=",")
        a, b = b, a+b

fibonacci_sequence(10)

#############################################################################
# Check if number is prime
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True
print()
print(is_prime(12), is_prime(13), is_prime(21), is_prime(17), end="\n\n")

#############################################################################
# Write code to count number of capital letters in string
a = "Ako By sa ti pacilo Ist na Bahamy V letE."
def count_capital_letters(string):
    count = 0
    for character in string:
        if character.isupper():
            count += 1
    return count
print("Number of capital letter in string is {}". format(count_capital_letters(a)))

#############################################################################
# Looking at the following code, write down the final values of each A0..A6
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#A0 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
A1 = range(10)
#A1 = range(0,10)
A2 = sorted(([i for i in A1 if i in A0]))
#A2 = []
# But if A2 = sorted(([i for i in A1 if i in A0.values()]))
# Then A2 = [1,2,3,4,5]
A3 = sorted([A0[s] for s in A0])
#A3 = [1,2,3,4,5]
A4 = [i for i in A1 if i in A3]
#A4 = [1,2,3,4,5]
A5 = {i:i*i for i in A1}
#A5 = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
A6 = [[i,i*i] for i in A1]
#A6 = [[0,0], [1,1], [2,4], [3,9], [4,16], [5,25], [6,36], [7,49], [8,64], [9,81]]

#############################################################################
# FIZZBUZZ -> change integer in list for new value
# if number is divisible by 3 -> fizz
# if number is dividible by 5 -> buzz
# if number is divisible by 15 -> fizzbuzz

a = [15,36,45,99,46,30,1,75,9,20]

def fizzbuzz_swap(a):
    for index, number in enumerate(a):
        if not number % 3 and not number % 5:
            a[index] = "FizzBuzz"
        elif not number % 3: # number % 3 == 0
            a[index] = "Fizz"
        elif not number % 5: # number % 5 == 0
            a[index] = "Buzz"
    return a

print(fizzbuzz_swap(a))


#############################################################################
#Square list
a = [15,36,45,99,46,30,1,75,9,20]
def square(x):
    return x**2

a = [square(number) for number in a]
print(a)

#display only odd numbers into new list
a = [15,36,45,99,46,30,1,75,9,20]
a = [number for number in a if number % 2]
print(a)

#############################################################################
#Sorting basics
a = [15,36,45,99,46,30,1,75,9,20]
print(sorted(a, reverse=True)) # descending order highest first
print(sorted(a)) # ascending order lowest first

a = ["ado", "onderejev", "lujza", 'September']
# Capital letters are sorted separately at the beginning of the list in ascending order
print(sorted(a, reverse=True)) #['ondrejev', 'lujza', 'ado', 'September']
print(sorted(a)) # ['September', 'ado', 'lujza', 'ondrejev']

a = {'dict1':{'name': 'ado'},
      'dict2':{'name': 'marek'}}
print(sorted(a))

#############################################################################
#Storing only unique characters

import random
all_words = "all the words in the world".split()
def get_random_word(all_words):
    return random.choice(all_words) #function returns random words from a list

#objective is to create function get_unique_words() that would return unique words only
def get_unique_words():
    words = set()
    for i in range(1000):
        words.add(get_random_word(all_words))
    return words

print(get_unique_words()) #variable all_words does not need to be passed bcs it is global

#second alternative using lists that is less efficient
def get_unique_words_in_list_1(): #O(n^2) - terrrible
    words = []
    for i in range(1000): #time complexity O(n)
        word = get_random_word(all_words)
        if word not in words: #time complexity O(n)
            words.append(word)
    return words

def get_unique_words_in_list_2():# O(n)
    words = []
    for i in range(1000):
        words.append(get_random_word(all_words))
    return set(words)#conversion is unnecessary,I can just use set and method add
print(get_unique_words_in_list_1())
print(get_unique_words_in_list_2())

#############################################################################
# Define default values in dictionaries .get() .setdefault()
person1 = {'name':'Ado', 'age': 23, 'height': 225}
person2 = {'nam':'Ado', 'age': 23, 'height': 225}
# Get would find out if there is key and if not returns default parameter 'Person does not have a name'
print(person1.get('name', 'Person does not have a name'))
print(person2.get('name', 'Person does not have a name'))

#Update dictionary with default value
print(person1.setdefault('name', 'Default name'))
print(person2.setdefault('name', 'Default name'))
print(person2, end="\n\n")

#############################################################################
# Your group of 4 people is at the Disney Park and you need to figure out
# all the possibilities how groups of 2 can be created
# Generating combinations and permutations
friends = ['Rachel', 'Ross', 'Joey', 'Chandler']
#Bruteforce
def permutations_BF(input_list):
    permutations = []
    for i in range(0, len(input_list)):
        for j in range(0,len(input_list)):
            if i == j: continue # (Ross, Ross) is invalid you can not go twice
            permutations.append((input_list[i],input_list[j]))
    return permutations
print(permutations_BF(friends))

def combinations_BF(input_list):
    combinations = []
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if i == j: continue
            pair = sorted((input_list[i], input_list[j]))
            if pair not in combinations:
                combinations.append(pair)
    return combinations
print(combinations_BF(friends), end="\n\n")

#Using itertools module
import itertools
def permutations(input_list):
    return list(itertools.permutations(input_list, r=2))#(input_list[i], input_list[j]) argument r=2 specifies group volume

def combinations(input_list):
    return list(itertools.combinations(input_list, r=2))#(input_list[i], input_list[j]) argument r=2 specifies group volume

print(permutations(friends))
print(combinations(friends))

#############################################################################
# List copy differences
names1 = ['Ado', 'kamil', 'Marek']
names2 = names1
names3 = names1[:]

names1[1] = 'Karol'
print("names1: {}\nnames2: {}\nnames3: {}".format(names1,names2,names3))
# names1 and names2 reference the same memory space,thus to create new list there is need for [:]

#############################################################################
# List conversion on string creates element for each character
a = "Biggest"
print(list(a))
a = "Biggest name that could be set"
print(list(a))

#############################################################################
# Algorithm to find average of numbers in list
def average(input_list):
    count_numbers = 0
    for i in input_list:
        count_numbers += i
    return round(count_numbers / len(input_list), 2) #second parameter of round selects number of ndecimal spaces

a = [1,6,4,8,5,12,45,8,45,41,67,14]
print(average(a))

#############################################################################
# Reverse number review
def reverse_number(a):
    a = str(a)
    if a[0] == '-':
        return '-' + a[:0:-1]
    else:
        return a[::-1]

print(reverse_number(-123))
print(reverse_number(357))

#############################################################################
# Calculate number of digits in a number without conversion to the string
#Alternative 1 provides solution if there is a need for separate number_of_digits function
def sum_of_digits(number):
    len_n = number_of_digits(number)
    print("Number of digits of number {} is {}". format(number, len_n))
    count = 0
    for i in range(0, len_n):
        count += number % 10
        number = number // 10
    return count

# Sum of digits of a number
def number_of_digits(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count

print(sum_of_digits(12354))

#Alternative 2 does it all in one while
def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum
print(sum_of_digits(12354), end="\n\n\n")

#############################################################################
# Magic functions in classes
    # create fictional database for a company of their employees and methods to retrieve data
class Employees():
    def __init__(self):
        self._employees = [
            'Martin Slaninka',
            'Milan Klobaska',
            'Ondra Pupek',
            'Sergej Zo Zahranicia',
            'Macejko']

    def __len__(self):
        return len(self._employees)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._employees.pop(item)
        raise TypeError("Invalid identification number od an employee.")

    def __contains__(self, employee):
        return employee in self._employees

    def __iter__(self):# returns and iterator to make looping possible
        while self._employees:
            yield self._employees.pop()

employees = Employees()
print("Number of employees is %d" % len(employees))
print("Latest employee that left the company is %s" % employees[1])
print("Number of employees is %d" % len(employees))

#Check if some emplyee is actually an employee of the company
print('Macejko' in employees)
print('Macko Poh' in employees)

#print all working employees
for employee in employees:
    print(employee)

#############################################################################
# Print number of occurrences of letter l in string - Technical test redHat
a = "Letter l may be kinda lazy to lack and luck is lost."
characters = collections.Counter(a)
l_char = characters.get('l')
print("Character 'l' has occurred {} times in a string.".format(l_char))

#############################################################################
# Difference between python array and list
#Lists contain heterogeneous items
my_list = [1, 'appe', 454]
#Arrays contain only homogeneous items
import array as arr
#i stands for signed int. There are various possibilities -> f=float,b=signed_char
number = arr.array('i',[1,2,3,4,5])
print(number)
number.append(6)
#number.append('apple') This would cause a TypeError --> it is homogeneous
#arrays are iterable
for i in number:
    print(i)

#############################################################################
# Inheritance of classes
class Person(object):
    def __init__(self, name):
        self.name = name
    def reveal_identity(self):
        return self.name

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero,self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        print(super(SuperHero, self).reveal_identity(), end=" : ")
        return self.hero_name
person = Person('Jirka Peter')
print(person.reveal_identity())
hero = SuperHero('Jirka Peter', 'Grumpy_Man')
print(hero.reveal_identity())

#############################################################################
# Check if number is a palindrome without converting it to string
def is_number_palindrome(number):
    palindrome = 0
    back_up_number = number # in the while loop number is modified thus cant be then compared

    while number > 0:
        digit = number % 10 # 123%10 = 3 --> always returns last digit
        palindrome = palindrome * 10 + digit # 0*10 +3 = 3 --> 3*10 + 2 = 32 --> 32*10 +1 =321
        number = number // 10 # 123 //10 = 12 --> 12 // 10 = 1

    return palindrome == back_up_number

print(is_number_palindrome(1233521))

#############################################################################
# Check if number is an Armstrong number - sum of its digits ^ 3 is equal to the number
# 153 is armstrong number bcs 1^3 + 5^3 + 3^3 = 153 (1+125+27)
def is_armstrong_number(number):
    number_back_up = number
    sum = 0
    while number > 0:
        sum += (number % 10) ** 3
        number = number // 10
    return sum == number_back_up

print(is_armstrong_number(153), is_armstrong_number(407), is_armstrong_number(111), end="\n\n")
if is_armstrong_number(153): # == true
    print("Armstrong number")

#############################################################################
# Check if a number is a Perfect number - sum of its divisiblers is the number itself
def is_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

print(is_perfect_number(6), is_perfect_number(7), is_perfect_number(0), is_perfect_number(5), is_perfect_number(28))

#############################################################################
# Check if a number is Strong number - sum of its digits factorials is equal the number itself
def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

def is_strong_number(number):
    number_backup = number
    sum = 0
    while number > 0:
        sum += factorial(number % 10)
        number = number // 10
    return sum == number_backup

print(is_strong_number(145),is_strong_number(14))

#############################################################################
# Find the nth largest number in a list
a = [56,98,4,2,65,84,35,66,42,48]
def find_nth_largest_number(list_numbers, n_tieth):
    return sorted(list_numbers, reverse=True)[n_tieth-1] # needs to be -1 because indexing starts at 0

print(find_nth_largest_number(a, 2))

#############################################################################
# Find number of vowels in a string
a = "This is a Test string to decide number of vowels."
def is_vowel(char):
    if char in "aeoiuAEUIO":
        return True
    return False

def vowels_count(a):
    characters = list(a)
    count = 0
    for i in range(len(characters)):
        if is_vowel(characters[i]) == True:
            count += 1
    return count
print("Number of vowels in the input istring is {}".format(vowels_count(a)))

#############################################################################
# Find matching letters in two strings without use of set().intersection()
a = "This is a Test string to decide number of vowels."
b = "As well as this might be common message."

def matching_characters(string_1, string_2):
    letters_1 = set(list(string_1))
    common = []
    for i in letters_1:
        if i in string_2:
            common.append(i)
    return common

print(matching_characters(a,b))

#############################################################################
# Delete all white spaces from a string
a = "::This is a Test strin,,,g to delete   all white space?s and diacritics!!,."

def remove_diacritics(string):
    for i in ".,:?! _#@":
        string = string.replace(i, '')
    return string
print(remove_diacritics(a))

#############################################################################
# List count method used to find number of appears in the list
a = [1,2,3,4,5,6,7,8,9,7,8,9,4,5,6,1,2,3,4,5,6,7,8,9]
print(a.count(7))
print(sorted(a, reverse=True))

#############################################################################
# List comprehensions basics
# basic binary list
binary = [2**i for i  in range(0,10)]
print(binary)
# nested ifs
temp = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
print(temp)
# if - else
temp = [x**2 if x >= 7 else x for x in range(15)]
print(temp)

# How to work with nested list inside lists using list comprehensions
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
list_of_lists = [i for j in list_of_lists for i in j]
print(list_of_lists)

list_of_lists = [[0 for column in range(4)] for row in range(3)]
print(list_of_lists)
