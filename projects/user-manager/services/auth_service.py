from data.user_repository import load_users
def register():
    from data.user_repository import save_users
    users=load_users()
    name = input("Name: ").strip().lower()
    password = input("Password: ").strip()
    confirm = input("Confirm Password: ").strip()
    for user in users:
        if user["name"] == name:
            print("User already exists.")
            return

    if password != confirm:
        print("Passwords do not match.")
        return


    job = input("Job: ").strip().lower()

    new_user = {
        "name": name,
        "password": password,
        "job": job
    }

    users.append(new_user)

    save_users(users)

    print("User added successfully.")
def login():
    pass