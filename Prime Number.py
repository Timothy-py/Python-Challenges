# A Python program to determine whether a number entered by the user is a prime number or not
# A prime number is any positive integer that is divisible only by itself and 1

# L1 - This line prompt the user to enter the number to check
# L3 - Creates an empty list named 'list'
# L5 - The for loop is used to pick number in turns within the range of
# the number entered from index 2 to index number-1.
# And each number picked from each index is stored into a variable named 'value'
# L6 - This line divides the number entered by the value and save the remainder in a variable named 'remaider'
# L7 - The append() method puts the remainder into the last index of the list
# L9 - This line prints the content of list so as to see all the remainders
# L11 - The if statement check if there exist 0 among the numbers in list, and if there exist, it outputs L12
# otherwise it outputs L14


number = int(input('Enter the number here : '))

list = []

for value in range(2, number):
    remainder = number % value
    list.append(remainder)

print(list)

if 0 in list:
    print('It is not a prime number')
else:
    print('It is a prime number')
