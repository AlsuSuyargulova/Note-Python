from create_file import create_note
from note_list import note_list, get_note, get_note_id
from note_modify import delete_data, edite

def interface():
    print("Добрый день! Вы попали на приложение заметок! \n 1 - запись данных \n 2 - вывод данных")
    command = str(input('Введите число: '))

    while command != "1" and command != "2":
        print("Неправильный ввод")
        command = str(input('Введите число: '))

    if command == "1": 
        create_note()

    elif command == "2": 
        open_note_list()

def open_note_list():
    note_list()
    command = str(input('Выберите номер заметки: '))
    note = get_note(command)

    if note == "0":
        print("Вариант неверный, повторите попытку ")
        open_note_list()
    else:
        print("Заголвок:")
        print(f"{note["Title"]}")
        print("Текст:")
        print(f"{note["Body"]}")
        option(note)

def option(note):
    command = str(input("Выберите действия с данной заметкой: \n 1 - удаление заметки \n 2 - редактирование заметки \n"))
    while command != "1" and command != "2":
        print("Неправильный ввод")
        command = str(input('Введите число: '))

    if command == "1":
        note_id = get_note_id(note)
        delete_data(note_id)
        print("Заметка успешно удалена!")
        interface()

    elif command == "2":
        edite_note(note)

def edite_note(note):
    print(note["Title"])
    command_title = str(input("Вывожу заголовок заметки, для сохранения - enter \n"))
    print(note["Body"])
    command_body = str(input("Вывожу текст заметки, для сохранения - enter \n"))

    if command_title != "":
        note["Title"] = command_title

    if command_body != "":
        note["Body"] = command_body

    edite(note)
    print("Заметка успешно отредактирована!")