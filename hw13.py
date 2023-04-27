def power_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a, b-1)

# Запрос ввода чисел A и B у пользователя
A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

# Возведение числа A в степень B с помощью рекурсии
result = power_recursive(A, B)

# Вывод результата
print(f"{A} в степени {B} равно {result}")
