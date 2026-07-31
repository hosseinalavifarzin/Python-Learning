from menus.main_menu import (
    show_main_menu,
    get_main_menu_choice,
    main_menu_items,
)

from panels.user_panel import user_panel


def main():

    print("===== USER MANAGER =====")

    while True:

        show_main_menu()

        choice = get_main_menu_choice()

        result = main_menu_items[choice]["action"]()

        if main_menu_items[choice]["returns_user"] and result is not None:
            user_panel(result)


if __name__ == "__main__":
    main()

'''
# ==========================
# Data
# ==========================

def main():
    try:
        while True:

            print("===== USER MANAGER =====")

            show_main_menu()

            choice =int( input("Choose option: ")) - 1
        
            if choice=="1":
                register()
                

            elif choice=="2":
                print("This feature is not implemented yet.")
        
            elif choice == "3":
                print("Goodbye!")
            break
    except:
        print("Please enter a valid number.")


users = []

options = [
    "Sign Up",
    "Delete User",
    "Show Users",
    "Search User",
    "Total Users",
    "Hello",
    "Calculator",
    "Exit"
]

calc = [
    "Multiply (*)",
    "Divide (/)",
    "Add (+)",
    "Subtract (-)"
]


# ==========================
# Storage
# ==========================

def load_users():
    global users

    try:
        with open("users.json", "r") as file:
            users = json.load(file)

    except FileNotFoundError:
        users = []


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


# ==========================
# Menu
# ==========================

def show_menu():
    print("\n===== USER MANAGER =====")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


# ==========================
# User Functions
# ==========================

def sign_up():

    name = input("Name: ").strip().lower()
    password = input("Password: ").strip()
    confirm = input("Confirm Password: ").strip()

    if password != confirm:
        print("Passwords do not match.")
        return

    for user in users:
        if user["name"] == name:
            print("User already exists.")
            return

    job = input("Job: ").strip().lower()

    new_user = {
        "name": name,
        "password": password,
        "job": job
    }

    users.append(new_user)

    save_users()

    print("User added successfully.")


def delete_user():

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:
            users.remove(user)

            save_users()

            print("User deleted successfully.")
            return

    print("User not found.")


def show_users():

    if len(users) == 0:
        print("No users.")
        return

    print()

    for user in users:

        print(f"Name     : {user['name']}")
        print(f"Password : {user['password']}")
        print(f"Job      : {user['job']}")
        print("-" * 30)


def search_user():

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:

            print("\nUser Found\n")

            print(f"Name     : {user['name']}")
            print(f"Password : {user['password']}")
            print(f"Job      : {user['job']}")

            return

    print("User not found.")


def total_users():

    print(f"Total Users : {len(users)}")


def hello():

    name = input("Enter your name: ").title()

    print(f"Hello {name}")


# ==========================
# Calculator
# ==========================

def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return None

    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculator():

    while True:

        print()

        for index, operation in enumerate(calc, start=1):
            print(index, operation)

        choice = input("Choose operation: ")

        try:

            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))

        except ValueError:

            print("Please enter a valid number.")
            continue

        if choice == "1":

            print("Result:", multiply(num1, num2))

        elif choice == "2":

            result = divide(num1, num2)

            if result is None:
                print("Cannot divide by zero.")
            else:
                print("Result:", result)

        elif choice == "3":

            print("Result:", add(num1, num2))

        elif choice == "4":

            print("Result:", subtract(num1, num2))

        else:

            print("Invalid operation.")
            continue

        again = input("Another calculation? (y/n): ").lower()

        if again != "y":
            break


# ==========================
# Main
# ==========================

load_users()

while True:

    show_menu()

    choice = input("\nChoose option: ")

    if choice == "1":

        sign_up()

    elif choice == "2":

        delete_user()

    elif choice == "3":

        show_users()

    elif choice == "4":

        search_user()

    elif choice == "5":

        total_users()

    elif choice == "6":

        hello()

    elif choice == "7":

        calculator()

    elif choice == "8":

        print("Goodbye.")
        break

    else:

        print("Invalid option.")
'''