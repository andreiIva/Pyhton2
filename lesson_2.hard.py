__author__ = 'ivanov andrei'
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print('задание №1')

Y = equation.split()
num_x = float(Y[2].replace('x', '')) * float(x)
y = num_x + float(Y[-1])

print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года
# Пример корректной даты
date = '01.11.1985'
# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'
print('задание №2')

date = '01.11.1985'
print('Пример корректной даты', date)
data = (input('Введите дату:'))
day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
   '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
   '11': 'одинадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
   '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
   '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
   '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
   '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое',
   '31': 'тридцать первое'}

month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
    '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
#

#number_of_days_in_a_month = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


data_new = data.split('.')

if len(data_new[0]) == 2 and len(data_new[1]) == 2 and len(data_new[2]) == 4:

    if 1 <= int(data_new[0]) <= (30 or 31) and 1 <= int(data_new[1]) <= 12 and 1 <= int(data_new[2]) <= 9999:
    #if int(data_new[0]) in range(1, 31) and int(data_new[1]) in range(1, 12) and int(data_new[2]) in (1, 9999):
        print('Дата введена верно!')
    else:
        print('Вы ошиблись при вводе дня(месяца или года)\n '
              'Свертесь с образцом.')

else:
    print('Попробуйте ввести еще раз, возможно Вы были невнимательны\n '
          'Свертесь с образцом.')


print('Вы ввели {} {} {} года'.format(day[data_new[0]], month[data_new[1]], data_new[2]))



# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже
#
# Пример:
# Вход: 13
# Выход: 6 2
# Вход: 11
# Выход: 5 3
print('задание №3')

number = int(input("Введите номер комнаты: "))
number_stage = 1
serial_number_left_stage = 1# учитываем, что есть 1 комната на первом этаже
block = 1

while number >= serial_number_left_stage + block ** 2:
    serial_number_left_stage = serial_number_left_stage + block ** 2
    number_stage += block
    block += 1

number_stage += ((number - serial_number_left_stage) // block)
serial_number_left_stage = int((number - serial_number_left_stage) % block + 1)

print(number_stage, serial_number_left_stage)