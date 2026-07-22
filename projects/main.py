users = ["ali", "hamed", "fateme", "sara", "reza", "nilo", "hanie"]

options = [
    "New User",
    "Delete User",
    "Show Users",
    "Search User",
    "Total Users",
    "Hello",
    "Calculator",
    "Exit"
]

add_options = [
    "Single Add",
    "Multi Add",
    "Back"
]

calc = [
    "Multiply (*)",
    "Divide (/)",
    "Add (+)",
    "Subtract (-)"
]


# ==========================
# Menu
# ==========================

def show_menu():
    for index, option in enumerate(options, start=1):
        print(index, option)


def show_add_menu():
    for index, option in enumerate(add_options, start=1):
        print(index, option)


def show_users():
    print("\nUsers:")
    print(", ".join(users))


# ==========================
# User Functions
# ==========================

def hello(name):
    print(f"Hello {name}")


def total_users():
    print(f"Total Users: {len(users)}")


def search_user():
    name = input("Enter username: ").strip().lower()

    if name in users:
        print(f"{name} ✅ User found")
    else:
        print("❌ User not found")


def add_user():

    while True:

        show_add_menu()

        choice = input("Choose option: ")

        if choice == "1":

            new_user = input("Enter username: ").strip().lower()

            if new_user in users:
                print(f"{new_user} already exists.")
            else:
                users.append(new_user)
                print(f"{new_user} added successfully.")

            show_users()

        elif choice == "2":

            names = input("Enter users (comma separated): ").lower().split(",")

            for user in names:

                user = user.strip()

                if user == "":
                    continue

                if user in users:
                    print(f"{user} already exists.")
                else:
                    users.append(user)
                    print(f"{user} added successfully.")

            show_users()

        elif choice == "3":
            break

        else:
            print("Invalid option")


def delete_user():

    names = input("Enter username(s): ").lower().split(",")

    for user in names:

        user = user.strip()

        if user in users:
            users.remove(user)
            print(f"{user} deleted successfully.")
        else:
            print(f"{user} does not exist.")

    show_users()


# ==========================
# Calculator
# ==========================

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return None

    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculator():

    while True:

        for index, operation in enumerate(calc, start=1):
            print(index, operation)

        choice = input("Choose operation: ")

        try:

            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == "1":
            print("Result:", multiply(num1, num2))

        elif choice == "2":
            result = divide(num1, num2)

            if result is not None:
                print("Result:", result)

        elif choice == "3":
            print("Result:", add(num1, num2))

        elif choice == "4":
            print("Result:", subtract(num1, num2))

        else:
            print("Invalid operation")
            continue

        again = input("Another calculation? (y/n): ").lower()

        if again != "y":
            break


# ==========================
# Main Program
# ==========================

print("===== USER MANAGER =====")

while True:

    show_menu()

    choice = input("Choose option: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        delete_user()

    elif choice == "3":
        show_users()

    elif choice == "4":
        search_user()

    elif choice == "5":
        total_users()

    elif choice == "6":
        name = input("Enter your name: ").strip().title()
        hello(name)

    elif choice == "7":
        calculator()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid option")