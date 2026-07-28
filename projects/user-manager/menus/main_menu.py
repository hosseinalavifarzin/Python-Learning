menu_items = [
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

  for index, item in enumerate(menu_items, start=1):
    print(f"{index}. {item['title']}")