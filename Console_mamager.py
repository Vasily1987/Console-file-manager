
#Программа консольный менеджер
import os
import sys
import shutil


while True:
    print('1. Создать (папку/файл)')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Вывод всех объектов в рабочей папке')
    print('6. Вывод только файлов которые находятся в рабочей папке')
    print('7. Вывести информацию об операционной системе')
    print('8. Cоздатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Cмена рабочей директории')
    print('12. выход')
    choice = input('Выберите пункт меню  ')
    if choice == '1':
        choice_1 = input('Если Вы хотите создать папку нажмите 1, Если вы хотите создать файл нажмите 2  ')
        if choice_1 == '1':
            neime_drict = input('Введите имя папки ')
            os.mkdir(f'{neime_drict}')
        elif choice_1 == '2':
            neime_file = input('Введите имя файла и его раширение  ')
            open(f'{neime_file}', "w")
    elif choice == '2':
          choice_2 = input('Если Вы хотите удалить папку нажмите 1, Если вы хотите удалить файл нажмите 2  ')
          if choice_2 == '1':
            neime_drict = input('Введите имя папки которую хотите удалить ')
            os.rmdir(f'{neime_drict}')
          elif choice_2 == '2':
            spid_file = input('укажите путь к файлу кторый нужно удалить   ')
            os.remove(f'{spid_file}')
    elif choice == '3':
          сhoice_3 = input('Если Вы хотите копировать файл 1, Если вы хотите копировать папку нажмите  2  ')
          if сhoice_3 == '1':
            file_copy = input('Введите имя файла который нужно скопировать    ')
            neme_file = input('Введите имя для скопированного файла  ')
            shutil.copy(f'{file_copy}',f'{neme_file}')
          elif сhoice_3 == '2':
            drictory_copy = input('укажите путь к деректроии которую нужно скопировать ')
            neme_dir = input('укажите путь к новой деректроии и ее имя  ')
            shutil.copytree(f'{drictory_copy}', f'{neme_dir}')
    elif choice == '4':
          print(os.listdir())
    elif choice == '5':
        for dirpath, dirnames, filenames in os.walk("."):
            # перебрать каталоги
            for dirname in dirnames:
                print("Каталог:", os.path.join(dirpath, dirname))
            # перебрать файлы
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))
    elif choice == '6':
        for dirpath, dirnames, filenames in os.walk("."):
            # перебрать файлы
            for filename in filenames:
                print("Файл:", os.path.join(dirpath, filename))
    elif choice == '7':
        print(os.name)
        print(sys.platform, sys.getwindowsversion())
    elif choice == '8':
        print(os.getlogin())
    elif choice == '9':
        import Victori
        Victori.victor()
    elif choice == '10':
        import amaunt
        amaunt.amaunt()
    elif choice == '11':
        import diritori
        diritori.catalog()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')