def show_profile(current_user):

    print("\n===== PROFILE =====")
    print(f"Name : {current_user['name']}")
    print(f"Role : {current_user['role']}")


def change_password(current_user):

    print("Change password feature is not implemented yet.")


def logout(current_user):

    print(f"\nGoodbye {current_user['name']}!")

    return "logout"

