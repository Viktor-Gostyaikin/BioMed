'''
1. На вход программе даётся некоторое целое положительное (т.е. натуральное) число.
Сосчитайте его факториал.
2. На вход программе даётся некоторое натуральное число. Сосчитайте сумму всех
целых чисел от единицы до этого числа включительно.
3. Напишите программу, которая по длинам трёх сторон треугольника определяет,
является ли он равносторонним (все три стороны равны), равнобедренным (только
две стороны равны).
4. Допишите программу из предыдущего задания так, чтобы дополнительно
определялось, является ли треугольник прямоугольным (вспомните теорему
Пифагора) и может ли такой треугольник существовать в принципе (представьте, что
одна сторона чрезвычайно велика, а две остальные очень малы).

'''

'''
Задание 1
    На вход программе даётся некоторое целое положительное (т.е. натуральное) число.
    Сосчитайте его факториал.
'''
import datetime
import locale
from random import random


def get_factorial():

    number = input('Введите натуральное число для вычисления факториала: ')

    try:
        number = int(number)
    except:
        return "Ожидается на вход число"

    if number < 0:
        return "Чило должно быть натуральным!"

    print("Ответ")

    return _get_factorial(number)


def _get_factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * _get_factorial(number-1)

print('Задание 1.')
print(get_factorial())


'''
Задание 2
    На вход программе даётся некоторое натуральное число. Сосчитайте сумму всех
    целых чисел от единицы до этого числа включительно.
'''
import random

def get_sum_int_up_to(number):

    try:
        number = int(number)
        if not number > 0:
            raise
    
        chicken_curry = random.randint(0,2) # 0\1\2

        if chicken_curry == 0:
            sum = 0

            for num in range(number):
                sum += number - num

            return sum

        elif chicken_curry == 1:
            return _get_sum_int_up_to(number)

        else:
            return number * (number-1) / 2

    except:
        return 'Ожидается натуральное число'

def _get_sum_int_up_to(number):
    
    if number == 0:
        return number

    return number + _get_sum_int_up_to(number-1)
    

print('\nЗадание 2. Расчет суммы последовательности целых чисел до заданного числа.')
number = input('Введите натуральное число: ')
print(get_sum_int_up_to(number))


'''
Задание 3
    Напишите программу, которая по длинам трёх сторон треугольника определяет,
    является ли он равносторонним (все три стороны равны), равнобедренным (только
    две стороны равны).
'''

class Triangle():
    
    def __init__(self, a, b, c):

        a = int(a)
        b = int(b)
        c = int(c)

        sides = [a, b, c]
        sides.sort()

        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]
        self.type_triangle = self.check_triangle()


    def check_triangle(self):
        
        type_triangle = 'Треугольник '

        if not self.validate_sides():
            raise Exception('Длины сторон не образуют треугольник')

        if self.a == self.b and self.b == self.c:
            type_triangle += 'равносторонний'
        
        elif self.a == self.b:
            type_triangle += 'равнобедренный'

        elif self.a ** 2 + self.b ** 2 == self.c ** 2:
            type_triangle += 'прямоугольный'
        
        else:
            type_triangle += 'разносторонний'

        return type_triangle

    def validate_sides(self):
        if self.a + self.b >= self.c:
            return True
        
        return False


print('Задание 3. Определение типа треугольника')
sides = input('Введите длины сторон треугольника через пробел: ')
sides = sides.strip().split(' ')
triangle = Triangle(*sides)
print(triangle.type_triangle)


'''
Задание 4.
    Допишите программу из предыдущего задания так, чтобы дополнительно
    определялось, является ли треугольник прямоугольным (вспомните теорему
    Пифагора) и может ли такой треугольник существовать в принципе (представьте, что
    одна сторона чрезвычайно велика, а две остальные очень малы).
'''
locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

def change_format_date(date):

    date = date.strip().split(' ')
    date[1] = date[1][:3]
    date = ' '.join(date)

    try:
        raw_date = datetime.datetime.strptime(date, '%d %b %Y года').date()
        
        return raw_date.strftime('%d.%m.%Y')

    except:
        return 'Ошибка. Введите дату в формате: "2 февраля 2000 года"'


date = input('Введите дату в формате "2 февраля 2000 года": ')
print(change_format_date(date))


'''
Задание 5. Напишите программу, которая будет читать файл 'testinput.txt' в той же папке, что и
    выполняемый скрипт, и выводить встречаемость каждого слова в нём.
'''

def сount_frequency_words(file_path):

    requency_words = {}

    with open(file_path, 'r') as input_file:
        # Читаем первую строку:
        line = input_file.readline()
        # Пока переменная line не пуста, читаем следующую строку,
        # в конце файла она станет пустой и цикл завершится:
        while line != '':
            line = line.split(' ')

            for word in line:
                word = word.strip()

                if word in requency_words:
                    requency_words[word] += 1
                else:
                    requency_words[word] = 1

            line = input_file.readline()

        return requency_words

print(сount_frequency_words('testinput.txt'))

'''Задание 6'''
class Patient():
    '''
    surname     - str - фамилия
    name        - str - имя
    date_birth  - str - дата в формате dd.mm.yyyy
    diagnosis   - str - диагноз МКБ-10
    '''
    mkb10 = {
        'A': 'Некоторые инфекционные и паразитарные болезни',
        'B': 'Некоторые инфекционные и паразитарные болезни',
        'C': 'Новообразования',
        'D': 'Болезни крови, кроветворных органов и отдельные нарушения, вовлекающие иммунный механизм',
        'E': 'Болезни эндокринной системы, расстройства питания и нарушения обмена веществ',
        'F': 'Психические расстройства и расстройства поведения',
        'G': 'Болезни нервной системы',
        'H': ['Болезни глаза и его придаточного аппарата', 'Болезни уха и сосцевидного отростка'],
        'I': 'Болезни системы кровообращения',
        'J': 'Болезни органов дыхания',
        'K': 'Болезни органов пищеварения',
        'L': 'Болезни кожи и подкожной клетчатки',
    }

    def __init__(self, surname, name, date_birth, diagnosis=None):

        date_birth = date_birth.strip().split('.')

        self.surname = surname
        self.name = name
        self.date_birth = datetime.date(year=int(date_birth[2]),
                                        month=int(date_birth[1]),
                                        day=int(date_birth[0]))
        self.diagnosis = diagnosis

    def get_age(self):

        today = datetime.date.today()
        # Получаем количество лет и вычитаем год, если ДР ещё не наступил в этом году
        age = today.year - self.date_birth.year - (
            (today.month, today.day) < (self.date_birth.month, self.date_birth.day))

        return age

    def get_mkb10_class(self):

        mkb10_class = self.diagnosis[0]

        if mkb10_class == 'H':
            index = 0

            if int(self.diagnosis[1]) > 5:
                index = 1

            return self.mkb10[mkb10_class][index]

        return self.mkb10[mkb10_class]

print('\nЗадание 6.')
# Создаём пациента
patient1 = Patient('Мамонтов', 'Аркадий', '02.07.1935', 'H65.2')
# Получаем его возраст
print('Пациенту', patient1.get_age(), 'лет')
# Получаем классификацию болезни
print('Класс диагноза пациента:', patient1.get_mkb10_class())
