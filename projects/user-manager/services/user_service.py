from data.user_repository import load_users, save_users
#from panels.profile_panel import profile_panel

def change_username(current_user):

    users = load_users()

    new_name = input("New Name: ").strip().lower()

    if new_name == current_user["name"]:
        print("Nothing changed.")
        return

    for user in users:

        if user["name"] != current_user["name"] and user["name"] == new_name:
            print("User already exists.")
            return

    for user in users:

        if user["name"] == current_user["name"]:
            user["name"] = new_name
            break

    save_users(users)

    current_user["name"] = new_name

    print("Name changed successfully.")


def change_password(current_user):

    users = load_users()

    old_password = input("Current Password: ").strip()

    if old_password != current_user["password"]:
        print("Password is incorrect.")
        return

    new_password = input("New Password: ").strip()

    confirm = input("Confirm Password: ").strip()

    if new_password != confirm:
        print("Passwords do not match.")
        return

    for user in users:

        if user["name"] == current_user["name"]:
            user["password"] = new_password
            break

    save_users(users)

    current_user["password"] = new_password

    print("Password changed successfully.")


def change_role(current_user):

    users = load_users()

    new_role = input("New Role: ").strip().lower()

    if new_role == current_user["role"]:
        print("Nothing changed.")
        return

    for user in users:
        if user["name"] == current_user["name"]:
            user["role"] = new_role
            break

    save_users(users)

    current_user["role"] = new_role

    print("Role changed successfully.")
    

def logout(current_user):

    print(f"\nGoodbye {current_user['name']}!")

    return "logout"

def back(current_user):
    return "back"