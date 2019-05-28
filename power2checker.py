## This is a python progam that checks if a number is a positive integer
## It returns True if the number is positive and False otherwise

list = [2**i for i in range(0, 1000)]
while True:
    prompt = input('Enter number here: ')
    try:
        Number = int(prompt)
    except ValueError as e:
        print('Enter a positive integer value')
    finally:
        if Number in list:
            print('True')
        else:
            print('False')
