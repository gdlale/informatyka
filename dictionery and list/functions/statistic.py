from statistics import mean
from functions import users
import os
import time


def count_all_users(data: list[dict]) -> int:
   return len(data)

def count_users_with_missing_name(data: list[dict]) -> int:
    found = 0
    for user in data:
        if not user.get('name'):
            found += 1
    return found

def average_math_for_user(user: dict) -> float | None:
    grades = user.get('grades mathematics')
    if grades:
        return mean(grades)
    elif not grades:
        return None
    
def average_polish_for_user(user: dict) -> float | None:
    grades = user.get('grades polish')
    if grades:
        return mean(grades)
    elif not grades:
        return None

def average_english_for_user(user: dict) -> float | None:
    grades = user.get('grades english')
    if grades:
        return mean(grades)
    if not grades:
        return None

def overall_average_for_user(user: dict) -> float | None:
    grades_math = user.get('grades mathematics')
    grades_polish = user.get('grades polish')
    grades_english = user.get('grades english')
    grades = grades_math + grades_polish + grades_english
    if grades:
        return mean(grades)
    elif not grades:
        return None
    
def subject_average_for_all_users(data: list[dict], subject: str) -> float | None:
    subjects = ['mathematics','polish','english']
    if subject not in subjects:
                print('Invalid subject')
                return None
    grades = []
    key = f"grades {subject}"

    for user in data:
        grades += user.get(key)

    if grades:
        return mean(grades)
    elif not grades:
        return None
        


def best_student_in_subject(data: list[dict], subject: str) -> dict | None:
    subjects = ['mathematics','polish','english']
    if subject not in subjects:
                print('Invalid subject')
                return None
    best_grade = 0
    best_user = None
    key = f"grades {subject}"
    for user in data:
        if not user.get(key):
            pass
        else:
            if mean(user.get(key)) > best_grade:
                best_grade = mean(user.get(key))
                best_user = user

    return best_user


def grade_average_menu(data: list[dict]):
    print(
    """
    ================================================
    \n
    e - exit
    1 - math average
    2 - polish average
    3 - english average
    4 - overall average
    \n
    ================================================
    """)
    
    inp = input('- ').strip().lower()
    if inp == 'e':
        return None
    elif inp == '5':
        subject = input('subject: ').strip().lower()
        subjects = ['mathematics','polish','english']
        if subject not in subjects:
                print('Invalid subject')
                return None    
        if subject_average_for_all_users(data, subject):
            print(f'This subjects average grade is {subject_average_for_all_users(data, subject)}')
        else:
            print('There arent any grades in this subject')
        return None
    id = int(input('id: ').strip().lower())

    user = users.find_user_by_id(data, id)

    if inp == '1':
        if average_math_for_user(user):
            print(f'This users average math grade is: {average_math_for_user(user)}')
        else:
            print('This user doesnt have any grades in this subject')
    elif inp == '2':
        if average_polish_for_user(user):
            print(f'This users average polish grade is: {average_polish_for_user(user)}')
        else:
            print('This user doesnt have any grades in this subject')
    elif inp == '3':
        if average_english_for_user(user):
            print(f'This users average english grade is: {average_english_for_user(user)}')
        else:
            print('This user doesnt have any grades in this subject')
    elif inp == '4':
        if overall_average_for_user(user):
            print(f'This users overall average grade is: {overall_average_for_user(user)}')
        else:
            print('This user doesnt have any grades in this subject')
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("There is no such command")
        time.sleep(1)





