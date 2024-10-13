def interface():
    print("Добрый день! Вы попали на приложение заметок! \n 1 - запись данных \n 2 - вывод данных")
    command = str(input('Введите число: '))

    while command != '1' and command != '2':
        print("Неправильный ввод")
        command = str(input('Введите число: '))
