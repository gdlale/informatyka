import json
import os
import time

def save_data(data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def read_data():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)

def print_all_data(data:list[dict]):
    for el in data:
        print("==="*20)
        for k,v in el.items():
            print(f"{k} ----- {v}")

def print_user(user: dict):
    print("==="*20)
    for k, v in user.items():
        print(f"{k} ----- {v}")


def add_or_remove_grades(data: list[dict],user_id: int, subject: str, operation: str, grade: int)->None:
    subjects = ['mathematics','polish','english']
    if subject not in subjects:
        print('Invalid subject')
        return
    for user in data:
        if user.get('id') == user_id:
            key = f"grades {subject}"
            
            if operation == 'add':
                user[key].append(grade)
                print(f"Added {grade} to {subject}")
            elif operation == 'remove':
                if grade in user[key]:
                    user[key].remove(grade)
                    print(f"Removed {grade} from {subject}")
                else:
                    print(f'Grade not found in {subject}')
            else:
                print('Invalid operation')
            return      

    print('Couldnt find an user with a matching id')

            
def update_user_name(data: list[dict], user_id: int, new_name: str) -> bool:
    for user in data:
        if user.get('id') == user_id:
            user.update({'name': new_name})
            return True
        
    print('Couldnt find an user with a matching id')
    return False

def update_user_surname(data: list[dict], user_id: int, new_surname: str) -> bool:
    for user in data:
        if user.get('id') == user_id:
            user.update({'surname': new_surname})
            return True
        
    print('Couldnt find an user with a matching id')
    return False

def update_user_birth_date(data: list[dict], user_id: int, new_birth_date: str) -> bool:
    for user in data:
        if user.get('id') == user_id:
            user.update({'date of birth': new_birth_date})
            return True


def update_attributes_menu(data: list[dict]):
    print(
    """
    ================================================
    \n
    e - exit
    1 - add / remove grades
    2 - update user name
    3 - update user surname
    4 - update user date of birth
    \n
    ================================================
    """)
    
    inp = input('- ').strip().lower()
    if inp == 'e':
        return None
    if inp == '1':
        id = int(input('id: '))
        subject = input('mathematics/polish/english: ').strip().lower()
        operation = input('add/remove: ').strip().lower()
        grade = int(input('grade: '))
        add_or_remove_grades(data, id, subject, operation, grade)
    elif inp == '2':
        id = int(input('id: ').strip().lower())
        name = input('name: ').strip().lower()
        update_user_name(data,id,name)
        save_data(data)
    elif inp == '3':
        id = int(input('id: ').strip().lower())
        surname = input('surname: ').strip().lower()
        update_user_surname(data, id, surname)
        save_data(data)
    elif inp == '4':
        id = int(input('id: ').strip().lower())
        birth_date = input('date of birth: ').strip().lower()
        update_user_birth_date(data, id, birth_date)
        save_data(data)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("There is no such command")
        time.sleep(1)


