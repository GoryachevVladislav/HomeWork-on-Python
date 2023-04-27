def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a+1, b-1)

# Запрос ввода чисел a и b у пользователя
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Вызов функции sum для нахождения суммы a и b
result = sum(a, b)

# Вывод результата
print(f"Сумма чисел {a} и {b} равна {result}")
    