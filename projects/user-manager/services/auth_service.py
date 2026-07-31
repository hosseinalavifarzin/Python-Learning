from data.user_repository import load_users
def register():
    from data.user_repository import save_users
    users=load_users()
    name = input("Name: ").strip().lower()
    for user in users:
            if user["name"] == name:
                print("User already exists.")
                return
    password = input("Password: ").strip()
    confirm = input("Confirm Password: ").strip()
   

    if password != confirm:
        print("Passwords do not match.")
        return


    role = input("role: ").strip().lower()

    new_user = {
        "name": name,
        "password": password,
        "role": role
    }

    users.append(new_user)

    save_users(users)

    print(f"User added successfully.\n welcom {name}")


def login():
    users=load_users()
    name = input("Name: ").strip().lower()
    password = input("Password: ").strip()
    for user in users:
        if user["name"] == name and password==user["password"]:
            print("=" * 35)
            print(f"Welcome back, {name}!")
            print("Login successful.")
            print("=" * 35)
            return user
    else:
        print("Invalid username or password.")
