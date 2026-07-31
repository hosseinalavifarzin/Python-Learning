from menus.user_menu import show_user_menu,get_user_menu_choice, user_menu_items


def user_panel(current_user):

    while True:

        show_user_menu()

        choice = get_user_menu_choice()

        result = user_menu_items[choice]["action"](current_user)

        if result == "logout":
            break