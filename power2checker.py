list = [2**i for i in range(1, 1000)]
while True:
    prompt = input('Enter number here: ')
    try:
        Number = int(prompt)
    except ValueError as e:
        print(e)
    else:
        if (Number*-1) != -Number:
            print('Hey Dude! Enter a valid positive integer value')
        else:
            if Number in list:
                print('True')
            else:
                print('False')
    finally:
        pass
