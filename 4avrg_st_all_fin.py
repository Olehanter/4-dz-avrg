# courses_study
students_list = [
    {"name": "Василий", "surname": "Теркин", "gender": "м", "courses": 'Python', "grade": [8, 8, 9], "exam": 8},
    {"name": "Мария", "surname": "Павлова", "gender": "ж", "courses": 'Python', "grade": [7, 8, 8, 7, 8], "exam": 9},
    {"name": "Ирина", "surname": "Андреева", "gender": "ж", "courses": 'Python', "grade": [9, 9, 8, 10, 10],
     "exam": 7},
    {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "courses": 'Python', "grade": [7, 8, 8, 9, 8],
     "exam": 10},
    {"name": "Иван", "surname": "Васильев", "gender": "м", "courses": 'Python', "grade": [9, 8, 9, 6], "exam": 5},
    {"name": "Роман", "surname": "Золотарев", "gender": "м", "courses": 'Python', "grade": [8, 9, 9, 6, 9], "exam": 6}
]
lecturer_list = [
    {"name": "Пётр", "surname": "Фёдоров", "gender": "м", "courses": 'Python', "grade": [8, 8, 9, 10, 10], "exam": 8},
    {"name": "Мария", "surname": "Иванова", "gender": "ж", "courses": 'Python', "grade": [7, 8, 8, 7, 8, 9, 9],
     "exam": 9},
    {"name": "Григорий", "surname": "Андросян", "gender": "ж", "courses": 'Python', "grade": [9, 9, 8, 10, 10, 8, 8],
     "exam": 7}
]

class Student:
    def __init__(self, name, surname ):
        self.name = name
        self.surname = surname
        self.courses = []
        self.grades = {}
        self.students = []

class Lecturer:
    def __init__(self, name, surname ):
        self.name = name
        self.surname = surname
        self.courses = []
        self.grades = {}
        self.students = []

def avrg_grade(students, courses):
    sum_hw = 0
    counter = 0
    if courses in ['Python']:
        for student in students:
            if (student['courses'] == courses):
                sum_hw += sum(student['grade']) / len(student['grade'])
                counter += 1
        return round(sum_hw / counter, 2)
    return 'Были введены недопустимые символы'

print()
print(avrg_grade(students_list, 'Python'))
print(avrg_grade(lecturer_list, 'Python'))
