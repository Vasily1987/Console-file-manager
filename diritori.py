# Импорт модуля os
import os



def catalog():
    print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    path = input('Введите путь к новому каталогу    ')
    try:
        os.chdir(path)
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Каталог: {0} не существует".format(path))
    except NotADirectoryError:
        print("{0} не каталог".format(path))
    except PermissionError:
        print("У вас нет прав на изменение {0}".format(path))

