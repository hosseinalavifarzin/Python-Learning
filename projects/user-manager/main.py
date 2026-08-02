from menus.main_menu import (
    show_main_menu,
    get_main_menu_choice,
    main_menu_items,
)

from panels.user_panel import user_panel
from panels.admin_panel import admin_panel


def main():

    print("===== USER MANAGER =====")

    while True:

        show_main_menu()

        choice = get_main_menu_choice()

        result = main_menu_items[choice]["action"]()

        if result is None:
            continue

        current_user = result

        if current_user["role"] == "admin":
            admin_panel(current_user)
        else:
            user_panel(current_user)


if __name__ == "__main__":
    main()