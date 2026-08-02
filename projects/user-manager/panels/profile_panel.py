from menus.profile_menu import (
    show_profile_menu,
    get_profile_menu_choice,
    profile_menu_items,
)


def profile_panel(current_user):

    while True:

        print("\n========== PROFILE ==========")
        print(f"Name : {current_user['name']}")
        print(f"Role : {current_user['role']}")

        show_profile_menu()

        choice = get_profile_menu_choice()

        result = profile_menu_items[choice]["action"](current_user)

        if result == "back":
            break