n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))

set1 = set()
set2 = set()

# Заполнение первого множества
for i in range(n):
    elem = int(input("Введите элемент {}: ".format(i+1)))
    set1.add(elem)

# Заполнение второго множества
for i in range(m):
    elem = int(input("Введите элемент {}: ".format(i+1)))
    set2.add(elem)

# Поиск пересечения множеств
intersect = sorted(list(set1 & set2))

# Вывод результата
print("Элементы, встречающиеся в обоих множествах:", intersect)
