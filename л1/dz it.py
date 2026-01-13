# #1
# a = int(input('input number:'))
# for i in range(1, a + 1):
#     print(i)


# #2
try:
    x = int(input('input number:'))
    y = int(input('input number:'))
    if x > y:
        print('the greater number is', x)
    elif x < y:
        print('the greater number is', y)
    else:
        print('error')
except ValueError:
    print('ENTER NUMDER')