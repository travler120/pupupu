# def Main():
# #Zadanie 1.1
#     def greet(name):
#         return f'Привет, {name}'

#     name = input('Введите своё имя пользователя: ')
#     if name == ' ':
#         print('Ошибка, введите корректные данные ')
#         return
#     print(greet(name))
# #Zadanie 1.2
#     def square(number):
#         return number ** 2
#     number = input('Введите своё число: ')
#     try:
#         x = float(number)
#         print('Квадрат числа: ', square(x))
#     except ValueError:
#         print('Число некорректное')
# #Zadanie 1.3
 # def describe_person(name, age=30):
 #     print(f'Ваше имя: {name}, Ваш возраст: {age}')
   # name = input('Введите ваше имя')
 # age1 = input('Введите ваш возраст: ')
 # if age1 == '':
#     describe_person(name)
 # else:
 #     try:
 #         age = int(age1)
 #         describe_person(name, age)
 #     except ValueError:
 #         print('Введите корректные значения')


# Main()

# #Zadanie 2.1
# from math import sqrt
# number = int(input('Введите простое число: '))
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(sqrt(number) + 1)):
#         if number % i == 0:
#             return False
#         return True
# if is_prime(number) == True:
#     print('Число простое')
# else:
#     print('Число не простое')



# def describe_person():
#     name = input('Введите имя: ')  # запрашиваем имя [attached_file:1]
#     while True:                     # крутимся, пока не введут корректный возраст [attached_file:1]
#         age_str = input('Введите возраст: ')  # строковый ввод [attached_file:1]
#         if age_str.isdigit():                 # проверяем, что это целое неотрицательное число [attached_file:1]
#             age = int(age_str)                # преобразование к int [attached_file:1]
#             break                             # выходим из цикла [attached_file:1]
#         print('Возраст должен быть числом. Попробуйте ещё раз.')  # подсказка [attached_file:1]

#     return f'Имя: {name}, Возраст: {age}'     # формируем итоговую строку [attached_file:1]

# print(describe_person())                      # запускаем [attached_file:1]


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



# def describe_person(name, age=30):
#         print(f'Ваше имя: {name}, Ваш возраст: {age}')
# name = input('Введите ваше имя')
# age1 = input('Введите ваш возраст: ')
# if age1 == '':
#     describe_person(name)
# else:
#     try:
#         age = int(age1)
#         describe_person(name, age)
#     except ValueError:
#         print('Введите корректные значения')

# from math import sqrt
# number = int(input('Введите простое число: '))
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(sqrt(number) + 1)):
#         if number % i == 0:
#             return False
#         return True
# if is_prime(number) == True:
#     print('Число простое')
# else:
#     print('Число не простое')

# def is_prime(number):
#     if number < 1:
#         return 'сложное число'
#     for d in range(2, int(number ** 0.5) + 1):
#         if number % d == 0:
#             return False
#     return 'простое'
# number = int(input('Введие число: '))
# print(is_prime (number))
# def is_prime(number):
#     if number == 1:
#         return 'One'
#     if number == 0:
#         return 'Zero'
#     for d in range(2, int(number ** 0.5) + 1):
#         if number % d == 0:
#             return 'Composite numder'
#     return 'Prime number'

# number = int(input('Введие число: '))
# print(is_prime (number))
# def make_example_txt(path="example.txt"):
#     try:
#         open(path, "r", encoding="utf-8").close()
#     except FileNotFoundError:
#         with open(path, "w", encoding="utf-8") as f:
#             f.write("Первая строка\nВторая строка\nТретья строка\nЧетвёртая строка\n")

# def read_file(path="example.txt", mode="all", n=10):
#     with open(path, "r", encoding="utf-8") as f:
#         if mode == "all":
#             print(f.read())
#         elif mode == "lines":
#             for i, line in enumerate(f, 1):
#                 print(f"{i}: {line.rstrip()}")
#         elif mode == "size":
#             while chunk := f.read(n):
#                 print(chunk)
#         else:
#             print("mode: all | lines | size")

# if __name__ == "__main__":
#     make_example_txt()
#     read_file(mode="all")
#     print()
#     read_file(mode="lines")
#     print()
#     read_file(mode="size", n=10)



    # except FileNotFoundError:
    #     with open(path, "w", encoding="utf-8") as f:
    #         f.write("Первая строка\nВторая строка\nТретья строка\nЧетвёртая строка\n")


# def make_example_txt(path="example.txt"):
#      open(path, "r", encoding="utf-8").close()
# def read_file(path="example.txt", mode="all", n=10):
#     with open(path, "r", encoding="utf-8") as f:
#         if mode == "all":
#             print(f.read())
#         elif mode == "lines":
#             for i, line in enumerate(f, 1):
#                 print(f"{i}: {line.rstrip()}")
#         elif mode == "size":
#             while chunk := f.read(n):
#                 print(chunk)
#         else:
#             print("mode: all | lines | size")

# if __name__ == "__main__":
#     make_example_txt()
#     read_file(mode="all")
#     print()
#     read_file(mode="lines")
#     print()
#     read_file(mode="size", n=15)


# def read_block():
#     print("\nВведите текст (пустая строка — конец):")
#     lines = []
#     while True:
#         s = input()
#         if s == "":
#             break
#         lines.append(s)
#     return "\n".join(lines) + ("\n" if lines else "")

# def run_once():
#     mode = input("1 — перезаписать, 2 — добавить: ").strip()
#     mode = "w" if mode == "1" else "a"
#     data = read_block()
#     with open("user_input.txt", mode, encoding="utf-8") as f:
#         f.write(data)
#     print("Готово.")

# def main():
#     while True:
#         run_once()
#         again = input("Ещё раз? (д/н): ").strip().lower()
#         if again not in ("д", "y", "yes", "да"):
#             break

# if __name__ == "__main__":
#     main()

# def get_mode() -> str:
#     """Запрос у пользователя: перезаписать или добавить."""
#     mode = input("1 — перезаписать, 2 — добавить: ").strip()
#     return "w" if mode == "1" else "a"


# def read_lines_from_user() -> list[str]:
#     """Чтение строк из ввода до пустой строки."""
#     print("\nВведите текст (пустая строка — конец):")
#     lines = []
#     while True:
#         s = input()
#         if s == "":
#             break
#         lines.append(s)
#     return lines


# def write_user_input(path: str = "user_input.txt") -> None:
#     """Запись введённых пользователем строк в файл."""
#     mode = get_mode()
#     lines = read_lines_from_user()
#     with open(path, mode, encoding="utf-8") as f:
#         f.write("\n".join(lines) + ("\n" if lines else ""))


# if __name__ == "__main__":
#     write_user_input()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
circle = Circle(3)
print(f"Текущий радиус: {circle.get_radius()}")
circle.set_radius(5)
print(f"Новый радиус: {circle.get_radius()}")