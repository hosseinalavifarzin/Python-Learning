from data.user_repository import load_users ,save_users


def show_users(current_user):

    print("\n===== USERS =====")

    users = load_users()

    if not users:
        print("No users found.")
        return

    for index, user in enumerate(users, start=1):
        print(f"{index}. {user['name']} ({user['role']})")

    print()

def search_user(current_user):

    users = load_users()

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:

            print("\nUser Found\n")

            print(f"Name     : {user['name']}")
            print(f"Password : {user['password']}")
            print(f"role      : {user['role']}")

            return

    print("User not found.")

def delete_user(current_user):

    users = load_users()

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:

            if user["name"] == current_user["name"]:
                print("You cannot delete your own account.")
                return

            confirm = input("Are you sure? (y/n): ").strip().lower()

            if confirm != "y":
                print("Delete canceled.")
                return

            users.remove(user)

            save_users(users)

            print("User deleted successfully.")
            return

    print("User not found.")

def change_user_role(current_user):

    users = load_users()

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:

            if user["name"] == current_user["name"]:
                print("You cannot change your own role.")
                return

            print(f"\nName : {user['name']}")
            print(f"Role : {user['role']}")

            new_role = input("Enter new role (admin/user): ").strip().lower()

            if new_role not in ["admin", "user"]:
                print("Invalid role.")
                return

            if new_role == user["role"]:
                print("Nothing changed.")
                return

            confirm = input("Are you sure? (y/n): ").strip().lower()

            if confirm != "y":
                print("Change canceled.")
                return

            user["role"] = new_role

            save_users(users)

            print("Role changed successfully.")
            return

    print("User not found.")

def logout(current_user):

    print("\nLogged out successfully.\n")

    return "logout"