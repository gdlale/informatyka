from functions import data
from functions import users
from functions import statistic
import os
import time 

def program_menu()->None:
        print(
    """
    ================================================
    \n
    e - exit
    1 - add user
    2 - print all data
    3 - find users
    4 - modify users
    5 - average grade calculator
    6 - delete user
    7 - check name avability
    8 - count all users
    9 - count users with missing name
    0 - best student in subject 
    \n
    ================================================
    """)


def main(): 
    loaded_data:list[dict] = data.read_data()
    while True:
        program_menu()
        inp = input("- ").lower().strip()
        if inp == "e":
            print("The program has finished running")
            data.save_data(loaded_data)
            break

        elif inp == "1":
            new_user = users.add_new_user(loaded_data)
            loaded_data.append(new_user)
            data.save_data(loaded_data)

        elif inp == "2":
            data.print_all_data(loaded_data)

        elif inp == "3":
            users.find_users_menu(loaded_data)

        elif inp == "4":
            data.update_attributes_menu(loaded_data)

        elif inp == "5":
            statistic.grade_average_menu(loaded_data)

        elif inp == "6":
            id = int(input('id: ').strip().lower())
            users.delete_user_by_id(loaded_data,id)
            data.save_data(loaded_data)
        elif inp == "7":
            name = input('name: ').strip().lower()
            surname = input('surname: ').strip().lower()
            users.is_name_taken(loaded_data, name, surname)

        elif inp == '8':
            print(statistic.count_all_users(loaded_data))

        elif inp == '9':
            print(statistic.count_users_with_missing_name(loaded_data))
        elif inp == '0':
            subject = input('mathematics/polish/english: ').strip().lower()
            users.print_user(statistic.best_student_in_subject(loaded_data, subject))
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("There is no such command")
            time.sleep(1)


if __name__ == '__main__':
    main()
