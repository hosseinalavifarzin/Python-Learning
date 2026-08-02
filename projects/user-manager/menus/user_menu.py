from services.user_service import  change_password, logout
from panels.profile_panel import profile_panel
user_menu_items = [
   {
    "title": "Profile",
    "action": profile_panel
},
    {
        "title": "Change Password",
        "action": change_password
    },
    {
        "title": "Logout",
        "action": logout
    }
]


def show_user_menu():

    print("\n===== USER PANEL =====")

    for index, item in enumerate(user_menu_items, start=1):
        print(f"{index}. {item['title']}")


def get_user_menu_choice():

    while True:

        try:
            choice = int(input("\nChoose option: ")) - 1

            if choice < 0 or choice >= len(user_menu_items):
                print("Invalid option.\n")
                continue

            return choice

        except ValueError:
            print("Please enter a valid number.\n")