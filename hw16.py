def find_indexes(array, min_value, max_value):
    """Функция находит индексы элементов массива, значения которых принадлежат заданному диапазону"""
    indexes = []
    for i in range(len(array)):
        if min_value <= array[i] <= max_value:
            indexes.append(i)
    return indexes


my_array = input("Введите массив чисел через пробел: ").split()
my_array = [int(i) for i in my_array]
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
result = find_indexes(my_array, min_value, max_value)
print(f"Индексы элементов массива со значениями от {min_value} до {max_value}: {result}")
