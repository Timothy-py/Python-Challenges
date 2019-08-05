from math import sqrt, log

b = int(input('Enter the base here: = '))
h = int(input('Enter the height here: ='))


def parabola_len(b, h):
    if b > 0 and h > 0:

        l = sqrt(4 * h ** 2) + (b ** 2 / 2 * h) * log(2 * h + sqrt((4 * h ** 2 + b ** 2)) / b)

        print('The length of a parabola of base, %s and height, %s = %s ' % (b, h, l))

    elif b < 0 or h < 0:

        print('Please enter a positive integer value')


parabola_len(b, h)

