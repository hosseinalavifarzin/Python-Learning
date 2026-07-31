from services.auth_service import login, register


def exit_program():
    print("Goodbye!")
    exit()

main_menu_items = [
    {
        "title": "Login",
        "action": login,
        "returns_user": True
    },
    {
        "title": "Register",
        "action": register,
        "returns_user": False
    },
    {
        "title": "Exit",
        "action": exit_program,
        "returns_user": False
    }
]

def show_main_menu():
 for index, item in enumerate(main_menu_items , start=1):
    print(f"{index}. {item['title']}")


def get_main_menu_choice():

    while True:

        try:
            choice = int(input("\nChoose option: ")) - 1

            if choice < 0 or choice >= len(main_menu_items):
                print("Invalid option.\n")
                continue

            return choice

        except ValueError:
            print("Please enter a valid number.\n")