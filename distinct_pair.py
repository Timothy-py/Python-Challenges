def odd(self, product):
    if product:
        return True

sequence = []
print('Enter sequence of numbers ')

while True:
    prompt_no = input('Enter a number here: ')
    if prompt_no != 'stop' or 'STOP':
        try:
            int(prompt_no)
        except ValueError as error:
            print(error)
            print('Please enter a positive integer value')
        else:
            sequence.append(prompt_no)
    else:
        for number in sequence:
            for n in range(0, sequence[-1]):
                product = number * n
                if product is odd():
                    print('{} * {} = {}'.format(number, n, product))
                else:
                    pass







