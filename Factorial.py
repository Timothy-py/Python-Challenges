# A Python program to print the factorial of a number

# L1 - This line of code creates a variable named 'multiplier' which will
# be used to save the successive multiplications and it
# is initialized to 1 because it will be used to do the first multiplication
# L3 - Prompt the user to enter a number and save the number in a variable named 'number'
# L5 - The for loop is used to take each number in the range of number entered from 1 to number inclusive
# L6 - This line is the same as writing multiplier = multiplier * i, which implies that it takes the value of i and
# multiplied it with multiplier(which is initially 1) and in turn save the result in the multiplier variable
# L7 - The print() function is used to print the output with the help of the format() method, the curly braces
#  {}  are called placeholders
multiplier = 1

number = int(input('Enter the number here :'))

for i in range(1, number+1):
    multiplier *= i

print('{}! is = {}'.format(number, multiplier))