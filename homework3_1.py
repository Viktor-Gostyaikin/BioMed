'''
1. Прочитайте из строк файла 'testinput.txt' в той же папке, что и выполняемый скрипт,
    по одному числу и посчитайте сумму только чётных чисел в нём.
2. Напишите программу, которая будет принимать из input() два числа, разделённые
    пробелом, и делить первое на второе, не допуская ошибку деления на ноль.
3. Вычислите возраст человека, исходя из сегодняшней даты и введённой через input()
    даты рождения в формате '01.01.1900'.
4. Переведите формат даты из текстового формата типа '2 февраля 2000 года' в
    числовой типа '02.02.2000'.
5. Напишите программу, которая будет читать файл 'testinput.txt' в той же папке, что и
    выполняемый скрипт, и выводить встречаемость каждого слова в нём.
6. Доп. задание. Написать класс, описывающий пациента
'''

'''
Задание 1
    Прочитайте из строк файла 'testinput.txt' в той же папке, что и выполняемый скрипт,
    по одному числу и посчитайте сумму только чётных чисел в нём.
'''

def get_sum_even_numbers(file_path):
    sum_even_numbers = 0

    with open(file_path, 'r') as input_file:
        # Читаем первую строку:
        line = input_file.readline()
        # Пока переменная line не пуста, читаем следующую строку,
        # в конце файла она станет пустой и цикл завершится:
        while line != '':
            try:
                n = int(line)
                if n%2 == 0:
                    sum_even_numbers += n
            except:
                print('В строке указано не число:', line)
            
            line = input_file.readline()

        return sum_even_numbers

print('Задание 1.', '\nСумма четных чисел в файле:', get_sum_even_numbers('testinput.txt'))


'''
Задание 2
Напишите программу, которая будет принимать из input() два числа, разделённые
    пробелом, и делить первое на второе, не допуская ошибку деления на ноль.
'''

def dividing_two_nums():
    input_nums  = input('Деление двух чисел.\nВведите два числа через пробел: ')
    raw_nums    = input_nums.strip().split(' ')

    if len(raw_nums) != 2:
        print('Ошибка. Введите два числа')
        return

    try:
        num1 = int(raw_nums[0])
        num2 = int(raw_nums[1])

        if num2 != 0:
            print('Ответ:', num1/num2)
        else:
            print('Невозможно делить на ноль!')

    except:
        print('Ошибка. Введите два числа')

print('\nЗадание 2.')
dividing_two_nums()


'''
Задание 3
Вычислите возраст человека, исходя из сегодняшней даты и введённой через input()
    даты рождения в формате '01.01.1900'.
'''
import datetime as dt

def get_age():
    date_birth = input('Введите дату рождения в формате дд.мм.гггг: ')
    date_birth = date_birth.strip()

    try:
        date_birth = dt.datetime.strptime(date_birth, '%d.%m.%Y').date()
        today = dt.date.today()
        
        # Получаем количество лет и вычитаем год, если ДР ещё не наступил в этом году
        age = today.year - date_birth.year - (
            (today.month, today.day) < (date_birth.month, date_birth.day))

        return age
    except:
        print('Ошибка. Введите дату в формате: дд.мм.гггг!')

print('\nЗадание 3.')
print('Возраст:', get_age())


'''
Задание 4.
Переведите формат даты из текстового формата типа '2 февраля 2000 года' в
    числовой типа '02.02.2000'.
'''
import datetime as dt
import locale


locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

def change_format_date(date):

    date = date.strip().split(' ')
    date[1] = date[1][:3]
    date = ' '.join(date)

    try:
        raw_date = dt.datetime.strptime(date, '%d %b %Y года').date()
        
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

import datetime


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

# print('\nЗадание 6.')
# # Создаём пациента
# patient1 = Patient('Мамонтов', 'Аркадий', '02.07.1935', 'H65.2')
# # Получаем его возраст
# print('Пациенту', patient1.get_age(), 'лет')
# # Получаем классификацию болезни
# print('Класс диагноза пациента:', patient1.get_mkb10_class())
