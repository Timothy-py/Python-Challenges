max = -99999999
while(True):
    number = int(input('Enter the numbers here : '))
    if(number == 0):
        break
    for i in range(number+1):
        if(i>max):
            max = i

print('the maximum number is = ',max)
