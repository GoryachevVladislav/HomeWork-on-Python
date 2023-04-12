# Ввод номера билета
ticket_number = input("Введите номер билета (шестизначное число): ")

# Проверка на корректность ввода
if not ticket_number.isdigit() or len(ticket_number) != 6:
    print("Ошибка: введите шестизначное число!")
else:
    # Преобразование строки в целое число
    ticket_number = int(ticket_number)
    
    # Разделение номера билета на цифры
    digit1 = ticket_number // 100000
    digit2 = (ticket_number // 10000) % 10
    digit3 = (ticket_number // 1000) % 10
    digit4 = (ticket_number // 100) % 10
    digit5 = (ticket_number // 10) % 10
    digit6 = ticket_number % 10
    
    # Вычисление сумм первых трех и последних трех цифр
    sum1 = digit1 + digit2 + digit3
    sum2 = digit4 + digit5 + digit6
    
    # Проверка на счастливый билет
    if sum1 == sum2:
        print("Да, это счастливый билет!")
    else:
        print("Нет, это не счастливый билет.")
