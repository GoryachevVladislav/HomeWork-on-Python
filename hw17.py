def check_rhythm(poem):
    lines = poem.split()  # Разделение стихотворения на строки

    # Получение количества слогов (гласных букв) в каждой строке
    syllables = []
    for line in lines:
        words = line.split('-')  # Разделение строки на слова по дефисам
        syllable_count = sum(1 for word in words for char in word.lower() if char in 'aeiouаеёиоуыэюя')
        syllables.append(syllable_count)

    # Проверка, все ли количества слогов одинаковые
    if len(set(syllables)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


# Пример использования
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
