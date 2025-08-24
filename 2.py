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
    elif command == 4
    print('4. Введите или удалите данные по оценкам, предметам и ученикам: ')
    n = int(input('Введите данные которые нужно изменить: '))
    data = []
    print('Введите данные: ')
    for i in range(n):
    data = input(f'{i + 1}) ')
    todo.append(data)
    n = int(input('Введите данные, который нужно отредактировать: '))
    task = input('Введите новый данные: ')
    data[n - 1] = task

    n = int(input('Введите индекс данных, которое нужно удалить: '))
    data.pop(n)

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