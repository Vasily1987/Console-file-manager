# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
#out_filter = filter(filter_odd_num, numbers)
filter(filter_odd_num, numbers)

#print("Тип объекта out_filter: ", type(out_filter))
#print("Отфильтрованный список: ", list(out_filter))