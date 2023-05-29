import os

clear = lambda: os.system('cls')
clear()

os.chdir('C:/Users/VLAD/Desktop/Rabotaembratya/HWPython')
print(os.getcwd())

def add_user():
    with open('task1.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(input('Введите Фамилия, Имя, Телефон - '))

def read_all_users():
    with open('task1.txt', 'r') as f:
        for line in f:
            print(line.strip())

def search_user():
    with open('task1.txt', 'r') as f:
        search = input("Что ищем? - ")
        for line in f:
            if search in line:
                print(line.strip())

def edit_user():
    search = input("Введите имя или фамилию пользователя для изменения - ")
    users = []
    found = False

    with open('task1.txt', 'r') as f:
        for line in f:
            if search in line:
                users.append(line.strip())
                found = True

    if found:
        print("Найденные пользователи:")
        for i, user in enumerate(users):
            print(f"{i + 1}. {user}")

        user_index = int(input("Введите номер пользователя для изменения - ")) - 1
        if user_index >= 0 and user_index < len(users):
            new_data = input("Введите новые данные пользователя - ")
            users[user_index] = new_data
            with open('task1.txt', 'w') as f:
                for user in users:
                    f.write(user + "\n")
            print("Данные пользователя успешно изменены.")
        else:
            print("Неверный номер пользователя.")
    else:
        print("Пользователь не найден.")

def delete_user():
    search = input("Введите имя или фамилию пользователя для удаления - ")
    users = []
    found = False

    with open('task1.txt', 'r') as f:
        for line in f:
            if search in line:
                users.append(line.strip())
                found = True

    if found:
        print("Найденные пользователи:")
        for i, user in enumerate(users):
            print(f"{i + 1}. {user}")

        user_index = int(input("Введите номер пользователя для удаления - ")) - 1
        if user_index >= 0 and user_index < len(users):
            del users[user_index]
            with open('task1.txt', 'w') as f:
                for user in users:
                    f.write(user + "\n")
            print("Пользователь успешно удален.")
        else:
            print("Неверный номер пользователя.")
    else:
        print("Пользователь не найден.")

def info_func():
    print("\n1. Показать весь справочник")
    print("2. Добавить пользователя")
    print("3. Поиск пользователя")
    print("4. Изменить данные пользователя")
    print("5. Удалить пользователя")
    print("6. Выход")

info_func()
while True:
    user_action = int(input("Выберите функцию, введите цифру: "))

    if user_action == 1:
        read_all_users()
        info_func()
    elif user_action == 2:
        add_user()
        info_func()
    elif user_action == 3:
        search_user()
        info_func()
    elif user_action == 4:
        edit_user()
        info_func()
    elif user_action == 5:
        delete_user()
        info_func()
    elif user_action == 6:
        break
    else:
        print("\n!Нет такой функции!")
        info_func()
