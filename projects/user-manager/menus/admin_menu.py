from services.admin_service import (
    show_users,
    search_user,
    delete_user,
    change_user_role,
    logout,
)

admin_menu_items = [
    {
        "title": "Show Users",
        "action": show_users
    },
    {
        "title": "Search User",
        "action": search_user
    },
    {
        "title": "Delete User",
        "action": delete_user
    },
    {
        "title": "Change User Role",
        "action": change_user_role
    },
    {
        "title": "Logout",
        "action": logout
    }
]


def show_admin_menu():

    print("\n===== ADMIN PANEL =====")

    for index, item in enumerate(admin_menu_items, start=1):
        print(f"{index}. {item['title']}")


def get_admin_menu_choice():

    while True:

        try:

            choice = int(input("\nChoose option: ")) - 1

            if choice < 0 or choice >= len(admin_menu_items):
                print("Invalid option.\n")
                continue

            return choice

        except ValueError:
            print("Please enter a valid number.\n")