all_students = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        all_students.append(self)

    def rate_lect(self, lecturer, course, grade):
        """ Выставление оценок лекторам """

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def midl_grades_count(self):
        """ Подсчет среднего балла студента """

        sum_grade = 0
        count_grade = 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            count_grade += len(grade)
        return round(sum_grade / count_grade, 2)

    def __str__(self):
        """ Информация о студенте """

        return f'Студент\nИмя: {self.name} \nФамилия: {self.surname}' \
               f'\nСредняя оценка за домашние задания: {self.midl_grades_count()}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: Введение в программирование'

    def __lt__(self, other):
        """ Сравнение студентов по показателю среднего балла """

        if isinstance(other, Student):
            return self.midl_grades_count() < other.midl_grades_count()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


all_lecturers = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        all_lecturers.append(self)

    def midl_grades_count(self):
        """ Подсчет среднего балла лектора """

        sum_grade = 0
        count_grade = 0
        for grade in self.grades.values():
            sum_grade += sum(grade)
            count_grade += len(grade)
        return round(sum_grade / count_grade, 2)

    def __str__(self):
        """ Информация о лекторе """

        return f'Лектор\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.midl_grades_count()}'

    def __lt__(self, other):
        """ Сравнение лекторов по показателю среднего балла """

        if isinstance(other, Lecturer):
            return self.midl_grades_count() < other.midl_grades_count()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)
        self.courses_review = []

    def rate_hw(self, student, course, grade):
        """ Выставление оценок студентам """

        if isinstance(
                student, Student
        ) and course in self.courses_review and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """ Информация о проверяющем """

        return f'Проверяющий\nИмя: {self.name} \nФамилия: {self.surname}'


student_1 = Student('Петр', 'Сорокин', 'm')  # новый студент
student_1.courses_in_progress += ['Python']  # добавлен курс студенту
student_2 = Student('Наталия', 'Сидорова', 'f')  # новый студент
student_2.courses_in_progress += ['Git', 'Python', 'JavaScript']  # добавлены курсы студенту

reviewer_1 = Reviewer('Вася', 'Пупкин')  # новый проверяющий
reviewer_1.courses_review += ['Python', 'Git']  # добавлены курсы для рецензирования
reviewer_2 = Reviewer('Оля', 'Соловьева')  # новый проверяющий
reviewer_2.courses_review += ['Python', 'Git', 'JavaScript']  # добавлены курсы для рецензирования

lecturer_1 = Lecturer('Маша', 'Иванова')  # новый лектор
lecturer_1.courses_attached += ['Python', 'Git']  # добавлен курс лектору
lecturer_2 = Lecturer('Игорь', 'Семенов')  # новый лектор
lecturer_2.courses_attached += ['Python', 'JavaScript']  # добавлены курсы лектору

student_1.rate_lect(lecturer_1, 'Python', 10)  # студент ставит оценку лектору
student_2.rate_lect(lecturer_1, 'Git', 9)  # студент ставит оценку лектору
student_2.rate_lect(lecturer_2, 'Python', 7)  # студент ставит оценку лектору
student_2.rate_lect(lecturer_2, 'JavaScript', 6)  # студент ставит оценку лектору

reviewer_1.rate_hw(student_2, 'Python', 7)  # проверяющий ставит оценку студенту
reviewer_1.rate_hw(student_2, 'Git', 8)  # проверяющий ставит оценку студенту
reviewer_2.rate_hw(student_1, 'Python', 6)  # проверяющий ставит оценку студенту
reviewer_1.rate_hw(student_1, 'Python', 9)  # проверяющий ставит оценку студенту
reviewer_2.rate_hw(student_2, 'JavaScript', 10)  # проверяющий ставит оценку студенту

print(reviewer_1)  # информация о первом проверяющем
print()
print(reviewer_2)  # информация о втором проверяющем
print()

print(lecturer_1)  # информация о первом лекторе
print()
print(lecturer_2)  # информация о втором лекторе
print()

print(student_1)  # информация о первом лекторе
print()
print(student_2)  # информация о втором лекторе
print()

print(lecturer_1 < lecturer_2)  # сравнение лекторов по среднему баллу
print()
print(student_1 < student_2)  # сравнение студентов по среднему баллу
print()


# для подсчета средней оценки за домашние задания по всем студентам в рамках
# конкретного курса (в качестве аргументов принимаем список студентов и название курса);


def course_midl_grade(data_list, course):
    """ Подсчет средней оценки по всем студентам """

    for person in data_list:
        count_person = 0
        midl_grade_persons = 0

        if course in person.grades.keys():
            count_person += 1
            for cour, grade in person.grades.items():
                midl_grade_persons += sum(grade) / len(grade)

    print(midl_grade_persons)
    print(count_person)

    # for person in data_list:
    #     if course in person.grades.keys():
    #         count_person += 1
    #         for grade in person.grades.values():
    #             midl_grade_persons += sum(grade) / len(grade)
    #             print(sum(grade))
    # print(count_person)

    # return round(midl_grade_persons / count_person, 2)


print(student_1.grades)
print(student_2.grades)

print(course_midl_grade(all_students, 'Git'))
print(course_midl_grade(all_students, 'Python'))

# print(full_midl_grade(all_lecturers))

