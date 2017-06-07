num = int(input('Enter the number:'))

while num != 1:
    if num % 3 == 0:
        num = num / 3
        print('0', num)
    elif num % 3 == 1:
        num = (num - 1) /3
        print('-1', num)
    else:
        num = (num + 1) /3
        print('+1', num)
