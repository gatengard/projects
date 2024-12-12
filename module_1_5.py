# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_5.py' и напишите весь код в нём.
#
# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

immutable_var = (1, 2.1, 'gray', [3,4])
print(immutable_var)
# кортеж неизменный список, список внутри кортежа менять можно
immutable_var[3][1] = 5
print(immutable_var)
mutable_list = [2, 4.2, 'black', (1,2)]
print(mutable_list)
mutable_list[3] = '5'
print(mutable_list)
mutable_list.remove("black")
print(mutable_list)
mutable_list.append("white")
print(mutable_list)
mutable_list[0:2] = 4, 8.4, 'rock'
print(mutable_list)