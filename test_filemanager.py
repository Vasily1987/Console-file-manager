import os
import platform
from unittest.mock import patch
import shutil
import tempfile
import pytest
from unittest.mock import patch
from io import StringIO
from Console_maneger_NEO import create_folder, delete_file, copy_file, view_working_directory, view_only_folders, view_only_files, view_system_info, view_program_creator, change_working_directory, file_manager_menu

@pytest.fixture
def temp_folder(tmpdir):
    return tmpdir.mkdir("test_folder")

def test_create_folder(temp_folder, monkeypatch, capsys):
    # Ввод тестовых данных
    folder_name = str(temp_folder)

    # Замена ввода пользователем на тестовые данные
    monkeypatch.setattr('builtins.input', lambda _: folder_name)

    # Вызов функции
    create_folder()

    # Проверка результатов
    captured = capsys.readouterr()
    assert captured.out == "Папка уже существует\n"

def test_create_folder_already_exists(temp_folder, monkeypatch, capsys):
    # Ввод тестовых данных
    folder_name = str(temp_folder)

    # Замена ввода пользователем на тестовые данные
    monkeypatch.setattr('builtins.input', lambda _: folder_name)

    # Создание папки для теста
    temp_folder.mkdir("existing_folder")

    # Вызов функции
    create_folder()

    # Получение вывода функции
    captured = capsys.readouterr()

    # Проверка результатов
    assert captured.out == "Папка уже существует\n"

def test_delete_nonexistent_file_or_folder():
    assert delete_file("nonexistent_file.txt") == "Файл/папка не существует"

def test_delete_existing_file():
    with open("test_file.txt", "w"):
        pass
    assert delete_file("test_file.txt") == "Файл успешно удален"

def test_delete_existing_folder():
    os.makedirs("test_folder", exist_ok=True)
    assert delete_file("test_folder") == "Папка успешно удалена"

def test_delete_file_inside_folder():
    os.makedirs("test_folder", exist_ok=True)
    with open("test_folder/test_file.txt", "w"):
        pass
    assert delete_file("test_folder") == "Папка успешно удалена"

def test_delete_file_inside_subfolder():
    os.makedirs("test_folder/subfolder", exist_ok=True)
    with open("test_folder/subfolder/test_file.txt", "w"):
        pass
    assert delete_file("test_folder") == "Папка успешно удалена"

def test_copy_file(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "test_file")  # Mock user input for file name
    monkeypatch.setattr('os.path.exists', lambda _: True)  # Mock existence of file
    monkeypatch.setattr('builtins.input', lambda _: "test_destination")  # Mock user input for destination path
    monkeypatch.setattr('os.path.isdir', lambda _: True)  # Mock destination path is a directory
    monkeypatch.setattr('os.path.isfile', lambda _: True)  # Mock file_name is a file
    monkeypatch.setattr('shutil.copy', lambda _, __: None)  # Mock shutil.copy function
    assert copy_file() == "Файл успешно скопирован"
    monkeypatch.setattr('os.path.isfile', lambda _: False)  # Mock file_name is not a file
    monkeypatch.setattr('shutil.copytree', lambda _, __: None)  # Mock shutil.copytree function
    assert copy_file() == "Папка успешно скопирована"
    monkeypatch.setattr('os.path.isdir', lambda _: False)  # Mock destination path is not a directory
    assert copy_file() == "Указанный путь не существует"
    monkeypatch.setattr('os.path.exists', lambda _: False)  # Mock file does not exist
    assert copy_file() == "Файл/папка не существует"


def test_view_working_directory(capsys):
    view_working_directory()
    captured = capsys.readouterr()

    assert "Содержимое рабочей директории:" in captured.out
    assert len(captured.out.split('\n')) > 1


# Тест для функции view_only_folders()
def test_view_only_folders():
    folders = view_only_folders()
    assert isinstance(folders, list)
    for folder in folders:
        assert os.path.isdir(folder)

def test_view_only_files():
    assert len(view_only_files()) > 0

    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    for item in view_only_files():
        assert item in files

        full_path = os.path.join(current_dir, item)
        assert os.path.isfile(full_path)


def test_view_system_info(capsys):
    view_system_info()
    captured = capsys.readouterr()
    assert "Информация об операционной системе:" in captured.out
    assert "Операционная система:" in captured.out
    assert "Версия операционной системы:" in captured.out
    assert platform.system() in captured.out
    assert platform.release() in captured.out

def test_view_program_creator(capsys):
    view_program_creator()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Создатель программы: Василий"

def test_change_working_directory(monkeypatch, capsys):
    # Ввод имитируемого значения пользователем
    monkeypatch.setitem(__builtins__, 'input', lambda _: "new_directory")

    # Тестирование существующего пути
    monkeypatch.setattr(os.path, 'exists', lambda _: True)
    os.chdir = lambda path: path
    change_working_directory()

    captured = capsys.readouterr()
    assert "Рабочая директория изменена на new_directory" in captured.out

    # Тестирование несуществующего пути
    monkeypatch.setattr(os.path, 'exists', lambda _: False)
    change_working_directory()

    captured = capsys.readouterr()
    assert "Указанный путь не существует" in captured.out

def test_file_manager_menu(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    file_manager_menu()

    captured = capsys.readouterr()
    assert "===== Консольный файловый менеджер =====" in captured.out
    assert "1. Создать папку" in captured.out
    assert "2. Удалить (файл/папку)" in captured.out
    assert "3. Копировать (файл/папку)" in captured.out
    assert "4. Просмотр содержимого рабочей директории" in captured.out
    assert "5. Посмотреть только папки" in captured.out
    assert "6. Посмотреть только файлы" in captured.out
    assert "7. Просмотр информации об операционной системе" in captured.out
    assert "8. Создатель программы" in captured.out
    assert "9. Смена рабочей директории" in captured.out
    assert "10. Выход" in captured.out
    assert "Неверный выбор пункта меню" not in captured.out