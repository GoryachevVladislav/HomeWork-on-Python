a1 = float(input("Введите первый элемент арифметической прогрессии: "))
d = float(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите количество элементов арифметической прогрессии: "))

progression = []  # создаем пустой массив для хранения прогрессии

for i in range(n):
    progression.append(a1 + i*d)  # заполняем массив элементами прогрессии

print("Арифметическая прогрессия:", progression)  # выводим полученную прогрессию
