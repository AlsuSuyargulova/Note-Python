from create_file import create_note
from note_list import note_list, get_note, get_note_id
from note_modify import delete_data

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
        print("Вариант невеный, повторите попытку ")
        open_note_list()
    else:
        print(note)
        option(note)

def option(note):
    command = str(input("Выберите действия с данной заметкой: \n 1 - удаление заметки \n 2 - редактирование заметки \n"))
    if command == "1":
        note_id = get_note_id(note)
        delete_data(note_id)
        print("Заметка успешно удалена")
        interface()
