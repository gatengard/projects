# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
#
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

quantiti = 12
print ("Количество выполненных ДЗ =", quantiti, "шт")
time = 1.5
print("количество затраченных часов =",time)
course = "python"
print ("название курса -", course)
timeOfHoweWorkInMinuts = (time * 60) / quantiti
timeOfHomework = time / quantiti
print("среднее время выполнения задачи", timeOfHoweWorkInMinuts, "мин")

print("Курс:",course, ",Всего задач:", quantiti, ",затрачено часов:",time, ",среднее время выполнения",timeOfHomework, "часа")
print(f'Курс: {course}, Всего задач: {quantiti}, Затрачено часов: {time}, Среднее время выполнения: {timeOfHoweWorkInMinuts} минут')
# эксперимент аналогового ввода кода и названий переменных, не мастхэв