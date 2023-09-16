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
        user_input = int(input())

        if user_input == 1:
            try:
                read(file_name)
                user_input = int(
                    input("1 - изменить файл\n3 - выйти в меню\n"))

                if user_input == 1:
                    change(file_name)
                    input()

            except:
                user_input = int(
                    input("Пока что нет ниодно заметки.\nХотите добавить нажмите - 1.\nВернуться в меню - любую клавишу.\n"))
                if user_input == 1:
                    add(file_name)

        elif user_input == 2:
            add(file_name)
            print("\n")
        elif user_input == 3:
            print('Завершение работы.')
            working = False
        else:
            print('Некорректная команда!')
            print("\n")


def read(file_name):
    with open(file_name, 'r') as read_file:
        notes = json.load(read_file)

    for note in notes:
        print(note["date"])
        print("  " + str(note["head"]))
        print("  " + str(note["body"]))
        print('\n')


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
                         date=str(datetime.datetime.now()),
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

                user_сhoice = int(input())
                changed_note = input("Введите новую информацию: ")

                if user_сhoice == 1:
                    note["head"] = changed_note
                elif user_сhoice == 2:
                    note["body"] = changed_note
                else:
                    print("Такой команды нет.")

                note["date"] = str(datetime.datetime.now())
            else:
                print("Такой заметки не найдено.")

        with open(file_name, 'w') as write_file:
            json.dump(data, write_file)

    except:
        print("Ошибка. Попробуйте снова.")

    input("Изменения сохранены. Нажмите любую клавишу.")


def delete(file_name):
    os.system("CLS")
    target = input("Input the target: ")

    with open(file_name, 'r+') as file:
        data = file.readlines()

        for contact in range(len(data)):
            if target in data[contact]:
                print(data[contact])
                userChoice = input("Delete contact?(Y/N): ").lower()
                if userChoice == "y":
                    print(f"Contact {data[contact]}deleted.")
                    data[contact] = ""

                break
        else:
            print("sorry, not found")

    data = list(filter(None, data))
    with open(file_name, 'w') as file:
        file.writelines(data)

    input("press any key")
