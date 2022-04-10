# list comprehension
# new_list = [n+1 for n in list]

# conditional list comprehension
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]

#  python sequences = list, range, string, tuple -> they have order

NAMES = [name.upper() for name in names if len(name) > 5]
print(NAMES)

# dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

import random
student_scores = {
    student: random.randint(1, 100) for student in names
}

passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
print(passed_students)


