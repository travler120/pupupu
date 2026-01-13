# # #1.1
# def greet(n):
#     return f'Hello, {n}!'
# n = input('Enter username: ')
# if n == '':
#     print('Please enter correct data')
# else:
#     print(greet(n))

# #1.2
# def square(x):
#     return x ** 2

# try:
#     print(square(float(input('Enter numder\n'))))
# except ValueError:
#     print('Wrong data')

# #1.3
# def max_of_two(a, b): return a if a > b else b 
# a = int(input('Enter numder: ')) 
# b = int(input('Enter numder: ')) 
# print('Maximum number:', max_of_two(a, b))

# #2.1
# def describe_person(name, age=30):
#     return (f'Имя: {name}, Возраст: {age}')
# name = input('Enter name: ')
# a = input('Enter your age: ')
# if a == '':
#     print(describe_person(name))
# else:
#     try:
#         age = int(a)
#         print(describe_person(name, age))
#     except ValueError:
#             print('Wrong data')

# #2.2

def is_prime(number):
    if number < 2:
        return 'Not composite numder and not prime number'
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            return 'Composite numder'
    return 'Prime number'
try:
    number = int(input('Enter numder: '))
    print(is_prime (number))
except ValueError:
    print('Wrong data')