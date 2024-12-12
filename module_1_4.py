# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_4.py' и напишите весь код в нём.
#
# 2. Организуйте программу:
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста

# 3. Работа с методами строк:
# Используя методы строк, выполните следующие действия:
# Выведите строку my_string в верхнем регистре.
# Выведите строку my_string в нижнем регистре.
# Измените строку my_string, удалив все пробелы.
# Выведите первый символ строки my_string.
# Выведите последний символ строки my_string.

# Примечания:
# Для вывода значений на экран используйте функцию print().
# Для вызова методов строк используйте операцию точки '.'.
# Пример результата выполнения программы:
#
# Код:
# name = input()
# print(name.upper())
# Ввод в консоль:
# Urban
# Вывод на консоль:
# URBAN

my_string = input('write any text: ')
print(f'there are {len(my_string)} characters in the text "{my_string}"')
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ',''))
print(my_string[0])
print(my_string[-1])


