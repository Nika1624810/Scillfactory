import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks


for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
Список команд:
1. Добавить/редактировать оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Вывод информации по всем оценкам для определенного ученика
5. Вывести средний балл по каждому предмету определенного ученика
6. Добавить/удалить ученика или предмет
7. Выход из программы
''')

while True:
    command = int(input('Введите команду: '))

    if command == 1:
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks and class_ in students_marks[student]:
            students_marks[student][class_].append(mark)
            print(f'Команда выполнена: Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('Ошибка: неверное имя ученика или предмет')

    elif command == 2:
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {round(marks_sum / marks_count, 2)}')
            print()
        print('Команда выполнена')

    elif command == 3:
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
        print('Команда выполнена')

    elif command == 4:
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Оценки ученика {student}:')
            for class_ in classes:
                print(f'{class_} - {students_marks[student][class_]}')
            print('Команда выполнена')
        else:
            print('Ошибка: такого ученика нет')

    elif command == 5:
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Средний балл по предметам для {student}:')
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {round(marks_sum / marks_count, 2)}')
            print('Команда выполнена')
        else:
            print('Ошибка: такого ученика нет')

    elif command == 6:
        action = input('Хотите добавить или удалить? (add/remove): ')
        type_ = input('Выберите тип (student/class): ')

        if action == 'add' and type_ == 'student':
            new_student = input('Введите имя нового ученика: ')
            if new_student not in students:
                students.append(new_student)
                students.sort()
                students_marks[new_student] = {}
                for class_ in classes:
                    students_marks[new_student][class_] = []
                print(f'Команда выполнена: Ученик {new_student} добавлен')
            else:
                print('Ошибка: такой ученик уже есть')

        elif action == 'add' and type_ == 'class':
            new_class = input('Введите название нового предмета: ')
            if new_class not in classes:
                classes.append(new_class)
                for student in students:
                    students_marks[student][new_class] = []
                print(f'Команда выполнена: Предмет {new_class} добавлен')
            else:
                print('Ошибка: такой предмет уже есть')


        elif action == 'remove' and type_ == 'student':
            rem_student = input('Введите имя ученика для удаления: ')
            if rem_student in students:
                students.remove(rem_student)
                students_marks.pop(rem_student)
                print(f'Команда выполнена: Ученик {rem_student} удален')
            else:
                print('Ошибка: такого ученика нет')

        elif action == 'remove' and type_ == 'class':
            rem_class = input('Введите название предмета для удаления: ')
            if rem_class in classes:
                classes.remove(rem_class)
                for student in students:
                    students_marks[student].pop(rem_class)
                print(f'Команда выполнена: Предмет {rem_class} удален')
            else:
                print('Ошибка: такого предмета нет')

        else:
            print('Ошибка: вы ввели непонятную команду')

    elif command == 7:
        print('Выход из программы')
        break