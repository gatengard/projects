grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_st = list(students)
sorted_my_st = sorted(my_st)

my_dict = {sorted_my_st[0]:round(sum(grades[0])/(len(grades[0])),1),
      sorted_my_st[1]:round(sum(grades[1])/(len(grades[1])),1),
      sorted_my_st[2]:round(sum(grades[2])/(len(grades[2])),1),
      sorted_my_st[3]:round(sum(grades[3])/(len(grades[3])),1),
      sorted_my_st[4]:round(sum(grades[4])/(len(grades[4])),1)}
print(students)
name = input('Введите имя ученика: ')
print(f'Средняя оценка {name} = {my_dict[name]}')


