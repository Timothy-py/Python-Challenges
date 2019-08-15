###############################################
# Question 1
# A program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

# finalList = []
# for num in range(2000, 3200+1):
#     if num%7 == 0 and num%5 != 0:
#         finalList.append(num)
# for i in finalList:
#     print(i, end=',')

################################################
# Question 2
# A program which can compute the factorial of a given numbers.

# number = int(input('Enter an integer'))
# multiplier = 1
# for num in range(1, number+1):
#     multiplier *= num
# print(multiplier)

################################################
# Question 3
# With a given integral number n, a program to generate a dictionary that contains (i, i*i) such that i,
# is an integral number between 1 and n (both included). and then the program should print the dictionary.

# int_num = int(input('Enter an integer'))
# int_dico = {}
# for num in range(1, int_num+1):
#     key = num
#     value = num*num
#     int_dico[key] = value
#
# print(int_dico)

###############################################
# Question 4
# A program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.

# list = []
# print('input "stop" to end')
# while True:
#     number = input('Enter number here: ')
#     if number == 'stop':
#         break
#     else:
#         list.append(number)
#
# print(list, tuple(list))

##############################################

###############
# Question 5
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also include simple test function to test the class methods.


class String:
    # def __init__(self):
    #     self.string = ''

    def getString(self):
        self.string = input('Enter a string here: ')

    def printString(self):
        print(self.string.upper())


x = String()
x.getString()
x.printString()
##############################################
# Question 6
# A program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

# from math import sqrt
# C, H, D = 50, 30, input('enter a comma-separated value here : ')
# D = D.split(',')
# print(D)
# for num in D:
#     Q = sqrt((2*C*int(num))//H)
#     print(round(Q))
#
##############################################
# Question 7
# A program that takes two digits ixj and generates a two-dimensional array
# array_str = input('Enter a two dimension of array here: ')
# array_dim = [int(x) for x in array_str.split('x')]
#
# rowNum = array_dim[0]
# colNum = array_dim[1]
#
# multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
# multiList[1][2] = 4
# print(multiList)

###############################################
# Question 8
# A program that accepts a comma separated sequence of names as input and
# print the names in a comma-separated sequence after sorting them alphabetically
# name_string = input('Enter sequence of names here ')
# names = name_string.split(', ')
# print(sorted(names))

###############################################
# Question 9
# A program that accepts a sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
# word_str = ''
# while True:
#     prompt = input('Enter sentences here : ')
#     if prompt != '':
#         word_str += prompt
#     else:
#         break
#     print(word_str.upper())

###############################################
# Question 10
# A program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# prompt = input('Enter text strings here: ')
# parsed_text = [word for word in sorted(prompt.split(' '))]
# parsed_word = []
# for word in parsed_text:
#     if word not in parsed_word:
#         parsed_word.append(word)
#
# print(parsed_word)
''' or use set() on parsed_text instead of the for code suit '''

###############################################
# Question 11








