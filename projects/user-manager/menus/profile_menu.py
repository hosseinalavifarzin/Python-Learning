from services.user_service import (
    change_username,
    change_password,
    change_role,
    back,
)

profile_menu_items = [
    {
        "title": "Change Username",
        "action": change_username
    },
    {
        "title": "Change Password",
        "action": change_password
    },
    {
        "title": "Change Role",
        "action": change_role
    },
    {
        "title": "Back",
        "action": back
    }
]


def show_profile_menu():

    print("\n===== PROFILE =====")

    for index, item in enumerate(profile_menu_items, start=1):
        print(f"{index}. {item['title']}")


def get_profile_menu_choice():

    while True:

        try:
            choice = int(input("\nChoose option: ")) - 1

            if choice < 0 or choice >= len(profile_menu_items):
                print("Invalid option.\n")
                continue

            return choice

        except ValueError:
            print("Please enter a valid number.\n")