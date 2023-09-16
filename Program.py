import datetime
import os
import json
import uuid


def main(file_name):
    working = True
    while working:
        os.system('CLS')
        print("Чего вы хотите?: ")
        print('1 - показать заметки')
        print('2 - добавить новую заметку')
        print('3 - выйти')
        user_input = input()

        if user_input == '1':
            is_read_not_create_file = read(file_name)

            if is_read_not_create_file:
                user_input = input(
                    "1 - изменить заметку\n2 - удалить заметку\n3 - отфильтровать по дате\nЛюбую другую калавишу - выйти в меню\n")

                if user_input == '1':
                    change(file_name)
                elif user_input == '2':
                    delete(file_name)
                elif user_input == '3':
                    date_filter(file_name)

        elif user_input == '2':
            add(file_name)
        elif user_input == '3':
            print('Завершение работы.')
            working = False
        else:
            input('Некорректная команда!')


def read(file_name):
    try:
        with open(file_name, 'r') as read_file:
            notes = json.load(read_file)

        if bool(notes):
            for note in notes:
                print(note["date"])
                print(note["time"])
                print("  " + str(note["head"]))
                print("  " + str(note["body"]))
                print('\n')
            return True
        else:
            input("Пока нет ниодной заметки. Нажмите любую клавишу.")
            return False

    except:
        with open(file_name, 'w') as write_file:
            json.dump(list(), write_file)
        input("Пока нет ниодной заметки. Нажмите любую клавишу.")
        return False


def add(file_name):
    notes = list()
    try:
        with open(file_name, 'r') as write_file:
            notes = json.load(write_file)
    except:
        with open(file_name, 'w') as write_file:
            json.dump(notes, write_file)

    try:
        note_dict = dict(id=str(uuid.uuid4()),
                         date=datetime.datetime.now().strftime('%y/%m/%d'),
                         time=datetime.datetime.now().strftime('%H:%M:%S'),
                         head=input("Введите заголовок: "),
                         body=input("Введите текст заметки: "))

        notes.append(note_dict)

        with open(file_name, 'w') as write_file:
            json.dump(notes, write_file)

    except:
        input("\nОшибка. Попробуйте снова. Нажмите любую клавишу.")

    input("\nЗаметка сохранена. Нажмите любую клавишу.")


def change(file_name):
    target = input(
        "Введите заголовок заметки, которую хотите поменять: ")

    with open(file_name, 'r') as file_read:
        data = json.load(file_read)

    try:
        for note in data:
            if note["head"] == target:
                print("Что вы хотите поменять?: ")
                print("1 - заголовок")
                print("2 - текст заметки")

                user_сhoice = input()
                changed_note = input("Введите новую информацию: ")

                if user_сhoice == '1':
                    note["head"] = changed_note
                elif user_сhoice == '2':
                    note["body"] = changed_note
                else:
                    print("Такой команды нет.")

                note["date"] = datetime.datetime.now().strftime('%y/%m/%d'),
                note["time"] = datetime.datetime.now().strftime('%H:%M:%S'),
            else:
                print("Такой заметки не найдено.")

        with open(file_name, 'w') as write_file:
            json.dump(data, write_file)

    except:
        print("Ошибка. Попробуйте снова.")

    input("Изменения сохранены. Нажмите любую клавишу.")


def delete(file_name):
    target = input("Введите заголовок заметки, которую хотите удалить.\n")

    with open(file_name, 'r') as read_file:
        data = json.load(read_file)

    data_without_target = list(filter(lambda i: i['head'] != target, data))

    with open(file_name, 'w') as write_file:
        json.dump(data_without_target, write_file)

    input("Заметка удалена. Нажмите любую клавишу.")


def date_filter(file_name):
    with open(file_name, 'r') as read_file:
        data = json.load(read_file)

    print("Отфильтровать от: ")
    try:
        date_start = datetime.datetime(int(input("Год: ")), int(
            input("Месяц: ")), int(input("Число: ")))

        print("До: ")
        date_end = datetime.datetime(int(input("Год: ")), int(
            input("Месяц: ")), int(input("Число: ")))
    except:
        input("Ошибка! Некправильный формат даты. Попробуйте снова.")

    temp_data = list(
        filter(lambda i: datetime.datetime.strptime(i['date'], '%y/%m/%d') >= date_start, data))

    temp_data = list(
        filter(lambda i: datetime.datetime.strptime(i['date'], '%y/%m/%d') <= date_end, data))

    if not temp_data:
        print("Заметок в этот период нет.")
    else:
        for note in temp_data:
            print(note["date"])
            print(note["time"])
            print("  " + str(note["head"]))
            print("  " + str(note["body"]))
            print('\n')

    input("Нажмите любую клавишу.")
