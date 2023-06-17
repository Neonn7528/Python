"""Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной"""



def view_contacts(): # чтениe и вывода данных
    with open("phonebook.csv", "r") as file:
        data = file.readlines()
        for line in data:
            print(line.strip())

def add_contact(): #сохранениe новой записи в файл
    surname = input("Введите фамилию: ").title()
    name = input("Введите имя: ").title()
    phone = input("Введите номер телефона: ")
    descr = input("Введите описание: ").lower()
    with open("phonebook.csv", "a") as file:
        file.write(f"{surname} {name} {phone}, {descr}\n")
    print("Контакт сохранён\n")

def search_contacts_by_surname(): #поиск записей по фамилии
    surname = input("Введите фамилию для поиска: ")
    with open("phonebook.csv", "r") as file:
        data = file.readlines()
        found = False
        for line in data:
            if surname in line:
                print(line.strip())
                found = True
        if not found:
            print("Контакты с такой фамилией не найдены\n")

def export_contacts(): # экспорт данных
    with open("phonebook.csv", "r") as source:
        with open("phonebook_export.csv", "w") as target:
            target.write(source.read())
    print("Данные успешно экспортированы в файл")

def import_contacts(): # импорт даных
    with open("phonebook_import.csv", "r") as source:
        with open("phonebook.csv", "a") as target:
            target.write(source.read())
    print("Данные успешно импортированы из файла\n")

while True:
    choice = input("Выберите действие:\n1 - Просмотреть список контактов\n2 - Добавить новый контакт\n3 - Поиск контактов по фамилии\n4 - Экспорт контактов\n5 - Импорт контактов\n6 - Выход\n")
    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contacts_by_surname()
    elif choice == "4":
        export_contacts()
    elif choice == "5":
        import_contacts()
    elif choice == "6":
        break
    else:
        print("Некорректный ввод")
