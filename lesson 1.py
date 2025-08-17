import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
	4. Добавить возможность удалять и редактировать данные по оценкам, предметам и ученикам
	5. Вывод информации по всем оценкам для определенного ученика
	6. Добавьте вывод среднего балла по каждому предмету по определенному ученику
        7. Выход из программы
        ''')

print('1. Добавить оценку ученика по предмету')
# считываем имя ученика
student = input('Введите имя ученика: ')
# считываем название предмета
class_ = input('Введите предмет: ')
# считываем оценку
mark = int(input('Введите оценку: '))
# если данные введены верно
if student in students_marks.keys() and class_ in students_marks[student].keys():
    # добавляем новую оценку для ученика по предмету
    students_marks[student][class_].append(mark)
    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
# неверно введены название предмета или имя ученика
else:
    print('ОШИБКА: неверное имя ученика или название предмета')

# считываем название предмета
class_ = input('Введите предмет: ')
# считываем оценку
mark = int(input('Введите оценку: '))
# если данные введены верно
if student in students_marks.keys() and class_ in students_marks[student].keys():
    # добавляем новую оценку для ученика по предмету
    students_marks[student][class_].append(mark)
    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
# неверно введены название предмета или имя ученика
else:
    print('ОШИБКА: неверное имя ученика или название предмета')
elif command == 2:
print('2. Вывести средний балл по всем предметам по каждому ученику')
# цикл по ученикам
for student in students:
    print(student)
    # цикл по предметам
    for class_ in classes:
        # находим сумму оценок по предмету
        marks_sum = sum(students_marks[student][class_])
        # находим количество оценок по предмету
        marks_count = len(students_marks[student][class_])
        # выводим средний балл по предмету
        print(f'{class_} - {marks_sum // marks_count}')
    print()
elif command == 3:
print('3. Вывести все оценки по всем ученикам')
# выводим словарь с оценками:
# цикл по ученикам
for student in students:
    print(student)
    # цикл по предметам
    for class_ in classes:
        print(f'\t{class_} - {students_marks[student][class_]}')
    print()
    elif command == 4
print('4. Введите или удалите данные по оценкам, предметам и ученикам: '))
# цикл по предметам
for class_ in classes:
    print(class_)
# цикл по оценкам
for marks in marks:
    print(marks)
# цикл по ученикам
for student in students:
    print(student)

class_ = int(input('Введите номер предмета, которое нужно отредактировать: '))
class_ = input('Введите новый предмет: ')
class_ = int(input('Введите индекс предмета, которое нужно удалить: '))
class_.pop()
marks = int(input('Введите номер предмета, которое нужно отредактировать: '))
marks = input('Введите новый предмет: ')
marks = int(input('Введите индекс предмета, которое нужно удалить: '))
marks.pop()
student = int(input('Введите номер предмета, которое нужно отредактировать: '))
student = input('Введите новый предмет: ')
student = int(input('Введите индекс предмета, которое нужно удалить: '))
student.pop()

print('Новые данные по оценкам, предметам и ученикам:')
print()
elif command == 5
print('5. Вывод информации по всем оценкам для определенного ученика ')
# считываем имя ученика
student = 'Александра'
# сгенерируем данные по оценкам:
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
print(f'''{student}
            {students_marks[student]}''')
elif command == 6
print('6. Добавьте вывод среднего балла по каждому предмету по определенному ученику')
# цикл по предметам
for class_in classes:
# считываем имя ученика
    student = input('Введите имя ученика')
# находим сумму по предмету
marks_sum = sum(student_marks[student][class_])
# находим количество оценок по предмету
marks_count = len(students_marks[student][class_])
# выводим средний балл по предмету
elif command == 7: \
    print('7. Выход из программы')
break