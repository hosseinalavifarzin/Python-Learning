from menus.admin_menu import (
    show_admin_menu,
    get_admin_menu_choice,
    admin_menu_items,
)


def admin_panel(current_user):

    while True:

        show_admin_menu()

        choice = get_admin_menu_choice()

        result = admin_menu_items[choice]["action"](current_user)

        if result == "logout":
            break