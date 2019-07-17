# A  python program to compute Fibonacci Series

list1 = [1]
number = int(input('Enter the number to find here : '))



def fibonacci(number):
    n = 2
    for i in range(1, number + 1):
        list1.append(i)
    print(list1)
    while n <= number:
        list1[n] = list1[n - 1] + list1[n - 2]
        n += 1
    print(list1)


fibonacci(number)


# list2 = [x for x in range(5)]
# print(list2)
# list3 = list[(map(lambda x: x**2, list2))]
# print(list3)