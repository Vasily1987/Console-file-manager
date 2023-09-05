# Тестирование функции filter
import math

import pytest


def test_filter():
    # Тестирование фильтрации четных чисел
    numbers = [1, 2, 3, 4, 5, 6]
    filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    assert filtered_numbers == [2, 4, 6]
    # Тестирование фильтрации строк по длине
    strings = ["apple", "banana", "cherry", "date"]
    filtered_strings = list(filter(lambda x: len(x) > 5, strings))
    assert filtered_strings == ["banana", "cherry"]
# Еще примеры
def is_positive(x):
    return x > 0

def is_even(x):
    return x % 2 == 0

def is_uppercase(s):
    return s.isupper()

def test_filter_numbers():
    numbers = [1, -2, 0, 4, -5, 6]
    filtered_numbers = list(filter(is_positive, numbers))
    assert filtered_numbers == [1, 4, 6]

def test_filter_even_numbers():
    numbers = [1, -2, 0, 4, -5, 6]
    filtered_numbers = list(filter(is_even, numbers))
    assert filtered_numbers == [-2, 0, 4, 6]

def test_filter_uppercase_strings():
    strings = ['HELLO', 'WORLD', 'python', 'TEST']
    filtered_strings = list(filter(is_uppercase, strings))
    assert filtered_strings == ['HELLO', 'WORLD', 'TEST']

# Тестирование функции map
def test_map():
    # Тестирование удвоения чисел
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    assert doubled_numbers == [2, 4, 6, 8, 10]

    # Тестирование приведения строк к верхнему регистру
    strings = ["apple", "banana", "cherry"]
    uppercase_strings = list(map(lambda x: x.upper(), strings))
    assert uppercase_strings == ["APPLE", "BANANA", "CHERRY"]
# Еще примеры
def square(x):
    return x ** 2
def capitalize(s):
    return s.capitalize()

def test_map_numbers():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    assert squared_numbers == [1, 4, 9, 16, 25]

def test_map_strings():
    strings = ['hello', 'world', 'python']
    capitalized_strings = list(map(capitalize, strings))
    assert capitalized_strings == ['Hello', 'World', 'Python']

# Тестирование функции sorted
def test_sorted_function():
    numbers = [5, 2, 7, 1, 9]
    expected_result = [1, 2, 5, 7, 9]
    result = sorted(numbers)
    assert result == expected_result

def test_sorted_strings():
    strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    expected_result = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    result = sorted(strings)
    assert result == expected_result

def test_sorted_dict():
    dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
    expected_result = [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    result = sorted(dict_list, key=lambda x: x['age'])
    assert result == expected_result

#Тест функции ip
def test_pi():
    expected_result = 3.141592653589793
    result = math.pi
    assert result == expected_result

#Тест фунции sqrt
def test_sqrt():
    number = 16
    expected_result = 4
    result = math.sqrt(number)
    assert result == expected_result
#Тест функции pow
def test_pow():
    base = 2
    exponent = 3
    expected_result = 8
    result = math.pow(base, exponent)
    assert result == expected_result

#Тест функции hypot
def test_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(0, 0) == 0
    assert math.hypot(-5, 12) == 13
    assert math.hypot(8, 15) == 17
    assert math.hypot(6.5, 4.5) == 7.905694150420948

def test_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(0, 0) == 0
    assert math.hypot(-5, 12) == 13
    assert math.hypot(8, 15) == 17
    assert math.hypot(6.5, 4.5) == pytest.approx(7.905, abs=1e-3)

