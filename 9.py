import sqlite3
connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS Users (name TEXT);")

def insert_user():
    name = input("Введите имя: ")
    cur.execute(f"INSERT INTO Users (name) VALUES ('{name}');")

def select_users():
    cur.execute("SELECT rowid, name FROM Users;")
    res = cur.fetchall()
    print(res)

def update_user():
    old_name = input("Введите имя для обновления: ")
    new_name = input("Введите новое имя: ")
    cur.execute(f"UPDATE Users SET name='{new_name}' WHERE name='{old_name}';")

def delete_user():
    name_to_delete = input("Введите имя для удаления: ")
    cur.execute(f"DELETE FROM Users WHERE name='{name_to_delete}';")






successful_login = True

if successful_login:
    while True:
        print("1. Добавить пользователя")
        print("2. Просмотреть пользователей")
        print("3. Обновить пользователя")
        print("4. Удалить пользователя")
        print("5. Выйти")

        choice = input("Введите ваш выбор")

        if choice == '1':
            insert_user()
        elif choice == '2':
            select_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Неверный выбор Пожалуйста введите правильный вариант")

    connection.commit()
    connection.close()
