__author__ = 'Ivanov Andrei'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()
print('Задание №1')

a = ['яблоко', 'банан', 'киви', 'арбуз', 'фейхоа']
n = 0
for i in range(len(a)):
    n += 1
    print(n,'{:>8}'.format(a[i]))

print("*" * 10)
# или таким образом(на этот вариант решения случайно наткнулся)

for x in a:
   print('{}. {:>6}'.format(a.index(x) + 1, x))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('Задание №2')
list_1 = [1, 36.6, 3.14, 'Yes', "Gamsat", True]
list_2 = [1, 2, 3, "Yes", True, False]
for i in list_2:
    if i in list_1:
        list_1.remove(i)
print(list_1)
#for i in list_1:
#    if i in list_2:
 #       list_2.remove(i)
#print(list_2)
print("*" * 10)
# или то же самое, но немного по-другому
for i in list_1:
    for j in list_2:
        if i == j:
            list_1.remove(i)
print(list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print('Задание №3')
list = []
for i in range(10):
    list.append(i)
#print(list)

new_list = []
for j in list:
    if j % 2 == 0:
        new_list.append(j / 4)
    else:
        new_list.append(j * 2)
print('Получили НОВЫЙ список :', new_list)
print("*" * 10)
# или то же самое, но немного по-другому
new_list = []
for i in list:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)
print('Получили НОВЫЙ список :', new_list)
