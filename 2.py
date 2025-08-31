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
        for student in students: # 1 итерация: student = 'Александра'
            students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
            # цикл по предметам
            for class_ in classes: # 1 итерация: class_ = 'Математика'
                marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
                students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
        # выводим получившийся словарь с оценками:
        for student in students:
            print(f'''{student}
            {students_marks[student]}''')
            while True:
                command = int(input('Введите команду: '))
                if command == 1:
                    print('1. Добавить оценку ученика по предмету')
                    # считываем имя ученика
                    student = input('Введите имя ученика: ')
                    # считываем название предмета
                    class_ = input('Введите предмет: ')
                    # считываем оценку
                    mark = int(input('Введите оценку: '))
                    # если данные введены верно
                    if (student in
    students_marks.keys() and class_ in
    students_marks[student].keys()):
                        # добавляем новую оценку для ученика по предмету
                        students_marks[student][class_].append(mark)
                        print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                    # неверно введены название предмета или имя ученика
                    else:
                        print('ОШИБКА: неверное имя ученика или название предмета')
                elif command == 4:
                    elif command == 1
                    print('1. Введите или удалите данные по оценкам, предметам и ученикам: ')
                    print(f'Введите данные которые нужно изменить: ')
                    # считываем элемент, который нужно удалить
                    data = input('Введите данные, которого нужно удалить: ')
                 # проверка на вхождение элемента в список
                if data in list:  # элемент есть в списке
                # удаляем элемент из списка
                list.remove(data)
                print('Данные удалены из списка.')
                else:  # элемента в списке нет
                        print('Данных в списке нет.')
                # выведем получившийся список
                        print(f'Список данных: {data}')
                        print('Измененные данные:')
                        print(data)
           elif command == 2
                    print('2. Вывод информации по всем оценкам для определенного ученика ')
                        # считываем имя ученика
                    student = 'Александра'
                        # сгенерируем данные по оценкам:
                    for student in students:  # 1 итерация: student = 'Александра'
                        students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
                    print(f'''{student}
                        {students_marks[student]}''')
                        elif command == 3
                            print('3. Добавьте вывод среднего балла по каждому предмету по определенному ученику')
                            #цикл по предметам
                            for class_in classes:
                            #считываем имя ученика
                                student=input('Введите имя ученика')
                            #находим сумму по предмету
                        marks_sum=sum(student_marks[student][class_])
                                #находим количество оценок по предмету
                        marks_count = len(students_marks[student][class_])
                                # выводим средний балл по предмету
                        print(' Выход из программы')
                        break