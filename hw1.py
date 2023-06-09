# Ввод трехзначного числа
num = input("Введите трехзначное число: ")

# Проверка на корректность ввода
if not num.isdigit() or len(num) != 3:
    print("Ошибка: введите трехзначное число!")
else:
    # Преобразование строки в целое число
    num = int(num)
    
    # Разделение числа на цифры
    one1 = num // 100
    two2 = (num // 10) % 10
    three3 = num % 10
    
    # Вычисление суммы цифр
    sum_of_digits = one1 + two2 + three3
    
    # Вывод результата
    print(f"Сумма цифр числа {num} равна {sum_of_digits}")
