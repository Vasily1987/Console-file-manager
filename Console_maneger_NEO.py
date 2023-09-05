import os
import platform
import shutil
import pytest
import tempfile
from unittest.mock import patch

def create_folder():
    folder_name = input("Введите имя папки: ")
    try:
        os.mkdir(folder_name)
        print("Папка успешно создана")
    except FileExistsError:
        print("Папка уже существует")

def delete_file(file_name):
    if os.path.exists(file_name):
        if os.path.isfile(file_name):
            os.remove(file_name)
            return "Файл успешно удален"
        else:
            shutil.rmtree(file_name)
            return "Папка успешно удалена"
    else:
        return "Файл/папка не существует"

def copy_file():
    file_name = input("Введите имя файла/папки для копирования: ")
    if os.path.exists(file_name):
        destination = input("Введите путь для сохранения копии: ")
        if os.path.isdir(destination):
            if os.path.isfile(file_name):
                shutil.copy(file_name, destination)
                return "Файл успешно скопирован"
            else:
                shutil.copytree(file_name, destination)
                return "Папка успешно скопирована"
        else:
            return "Указанный путь не существует"
    else:
        return "Файл/папка не существует"

def view_working_directory():
    current_dir = os.getcwd()
    print("Содержимое рабочей директории:")
    for item in os.listdir(current_dir):
        print(item)

def view_only_folders():
    current_dir = os.getcwd()
    folders = []
    for item in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, item)):
            folders.append(item)
    return folders

def view_only_files():
    current_dir = os.getcwd()
    files = []
    for item in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, item)):
            files.append(item)
    return files

def view_system_info():
    print("Информация об операционной системе:")
    print("Операционная система:", platform.system())
    print("Версия операционной системы:", platform.release())

def view_program_creator():
    return print("Создатель программы: Василий")


def change_working_directory():
    new_dir = input("Введите новый путь для рабочей директории: ")
    if os.path.exists(new_dir):
        os.chdir(new_dir)
        return print("Рабочая директория изменена на", new_dir)
    else:
        return print("Указанный путь не существует")

def file_manager_menu():
    while True:
        print("===== Консольный файловый менеджер =====")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Смена рабочей директории")
        print("10. Выход")

        choice = input("Выберите пункт меню: ")
        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file()
        elif choice == "3":
            copy_file()
        elif choice == "4":
            view_working_directory()
        elif choice == "5":
            view_only_folders()
        elif choice == "6":
            view_only_files()
        elif choice == "7":
            view_system_info()
        elif choice == "8":
            view_program_creator()
        elif choice == "9":
            change_working_directory()
        elif choice == "10":
            break
        else:
            print("Неверный выбор пункта меню")


if __name__ == "__main__":
    file_manager_menu()