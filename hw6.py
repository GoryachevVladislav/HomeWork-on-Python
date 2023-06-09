# Вводим сумму и произведение задуманных чисел
S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

# Инициализируем переменные для хранения найденных чисел X и Y
X = 0
Y = 0

# Перебираем все возможные значения чисел X и Y
for x in range(1, 1001):  # числа X от 1 до 1000
    for y in range(1, 1001):  # числа Y от 1 до 1000
        if x + y == S and x * y == P:  # если сумма и произведение соответствуют заданным значениям
            X = x
            Y = y
            break  # выходим из цикла, так как нашли ответ

# Проверяем, были ли найдены числа X и Y
if X == 0 or Y == 0:
    print("Числа X и Y не найдены.")
else:
    print("Число X:", X)
    print("Число Y:", Y)
