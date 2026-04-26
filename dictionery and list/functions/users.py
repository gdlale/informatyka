from random import randint
import time
import os


def generate_unique_id(data: list[dict]) -> int:
    lst_id = []
    for user in data:
        lst_id.append(user.get("id"))
    new_id = randint(1, 1000000)
    while new_id in lst_id:
        new_id = randint(1, 1000000)
    return new_id


def add_new_user(data: list[dict]) -> dict:
    return {
        "id": generate_unique_id(data),
        "name": input("Enter name: ").strip().lower() or None,
        "surname": input("Enter surname: ").strip().lower() or None,
        "date of birth": input("date of birth: ").strip().lower() or None,
        "grades mathematics": [],
        "grades polish": [],
        "grades english": [],
    }


def print_user(user: dict):
    print("===" * 20)
    for k, v in user.items():
        print(f"{k} ----- {v}")


def find_user_by_id(data: list[dict], user_id: int) -> dict | None:
    for user in data:
        if user.get("id") == user_id:
            return user

    print("Couldnt find an user with a matching id")
    return None


def find_users_by_name(data: list[dict], user_name: str) -> list[dict]:
    found = 0
    found_list = []
    if not user_name:
        for user in data:
            if user.get("name") is None:
                found += 1
                found_list.append(user)
    else:
        for user in data:
            if user.get("name") == user_name:
                found += 1
                found_list.append(user)

    if found == 0:
        print("Couldnt find any users with a matching name")
    else:
        return found_list


def delete_user_by_id(data: list[dict], user_id: int) -> bool:
    for user in data:
        if user.get("id") == user_id:
            data.remove(user)
            print("Deleted the user")
            return True

    print("Couldnt find an user with a matching id")
    return None


def is_name_taken(data: list[dict], name: str, surname: str) -> bool:
    if name == "":
        name = None
    if surname == "":
        surname = None
    for user in data:
        if user.get("name") == name and user.get("surname") == surname:
            print("Found an user with a matching name")
            return True

    print("No users with a matching name found")
    return None


def find_users_menu(data: list[dict]):
    print(
        """
    ================================================
    \n
    e - exit
    1 - find user by id
    2 - find users by name
    \n
    ================================================
    """
    )

    inp = input("- ").strip().lower()
    if inp == "e":
        return None
    if inp == "1":
        id = int(input("id: ").strip().lower())
        user = find_user_by_id(data, id)
        if user is not None:
            print_user(user)
    elif inp == "2":
        name = input("name: ").strip().lower()
        for user in find_users_by_name(data, name):
            print_user(user)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("There is no such command")
        time.sleep(1)
