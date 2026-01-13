# 1.1
import math

raw = input("Введите число: ")
try:
    x = float(raw)
    if x < 0:
        raise ValueError("Квадратный корень определён для x >= 0")
    print(math.sqrt(x))
except ValueError as e:
    print(f"Ошибка: {e}")


# 1.2 текущие дата и время
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

