from services.auth_service import login, register


def exit_program():
    print("Goodbye!")
    exit()

main_menu_items  = [
    {
        "title": "Login",
        "action": login
    },
    {
        "title": "Register",
        "action": register
    },
    {
        "title": "Exit",
        "action": exit_program
    }
]

def show_main_menu():

  for index, item in enumerate(main_menu_items , start=1):
    print(f"{index}. {item['title']}")


