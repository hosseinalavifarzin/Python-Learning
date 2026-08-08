


users=[
    {"name":"hanie",
     "age":24,
     "job":"designer"

},
    {"name":"hossein",
     "age":26,
     "job":"designer"

},
    {"name":"ali",
     "age":20,
     "job":"mentor"

}

]


while True:
    
    name=input("Enter new user: ")
    try:
        age=int(input("Enter age: "))
    except:
        print("Please enter a valid number")
        continue
    job=input("Enter job: ")


    new_user = {
    
    "name": name,
    "age": age,
    "job": job
        }
    found=False
    for user in users:
        if user["name"]==name:
            found=True
    if found==True:
        print(f"{new_user} already exists.")
    elif found==False:
        users.append(new_user)
        print(f"{new_user} added successfully") 
        for user in users:
            print(user)
    again = input("Do another calculation? (y/n): ")
    if again=="n":
        print("Goodbye!")
        break
    
'''

if new_user in users:
    print(f"{new_user} already exists.")
else:
    users.append(new_user)
    print(f"{new_user} added successfully")


for user in users:
    #print(student["name"], student["age"], student["job"])
    print(f"Name : {user['name']}")
    print(f"Age  : {user['age']}")
    print(f"Job  : {user['job']}")
    print("-" * 20)

    



    def add_user():
    while True:
            option()
            choose_option=input("choose an option:")
            if choose_option=="1":
                new_user = input("Enter new user: ").strip().lower()
                if new_user in users:
                    print(f"{new_user} already exists.")
                else:
                    users.append(new_user)
                    print(f"{new_user} added successfully")
                    show_user()
            elif choose_option=="2":
                 new_user = input("Enter new users: ").lower().split(",")
                 for user in new_user:
                    users.append(user)
                 print(f"{new_user} added successfully")
                 show_user()
            elif choose_option=="3":
                break


                
calc = [
    "Multiply (*)",
    "Divide (/)",
    "Add (+)",
    "Subtract (-)"
]


# ==========================
# Menu
# ==========================
def load_users():
    users.clear()

    with open("users.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            name, password, job = line.split(",")

            users.append({
                "name": name,
                "password": password,
                "job": job
            })

            
            def add_user():

    while True:
            options()
            choose_option=input("choose an option:")
            if choose_option=="1":
                name = input("Enter name: ").strip().lower()
                age = int(input("Enter age: "))
                job = input("Enter job: ").strip().lower()

                new_user = {
                "name": name,
                "age": age,
                "job": job
                }

                users.append(new_user)
            else:
                print("Invalid option")


            def cal():
   while True:
        for index, cal in enumerate(calc, start=1):
            print(index, cal)

        calc_choose =input("choose an option:")   

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))    

            if calc_choose  == "1":
                result = multiply(num1, num2)
                print(f"{num1} x {num2}={result}")

            elif calc_choose =="2":
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            elif calc_choose =="3":
                 result = add(num1, num2)
                 print(f"{num1} + {num2} = {result}")

            elif calc_choose =="4":
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
        
            else:
                print("Invalid choice")
                continue
        except:
            print("Please enter a valid number")

    
        
        again = input("Do another calculation? (y/n): ")
        if again=="n":
            break


                
def delete_user():
    delete_user=input("Enter user: ").lower().split(",")
    if delete_user in users:
        users.remove(delete_user)
        print(f"{delete_user} deleted successfully.")
        show_user()
    else:
            print(f"{delete_user} doesnt exists")



    name=input("Enter new user: ")
age=int(input("Enter age: "))
job=input("Enter job: ")


new_user = {
    
    "name": name,
    "age": age,
    "job": job
}
    """'''

name = input("Name: ").lower()

print(name)


text = "Python is bad "

text = text.replace("bad", "good")

print(text)


'''
# ==========================
# Data
# ==========================

def main():
    try:
        while True:

            print("===== USER MANAGER =====")

            show_main_menu()

            choice =int( input("Choose option: ")) - 1
        
            if choice=="1":
                register()
                

            elif choice=="2":
                print("This feature is not implemented yet.")
        
            elif choice == "3":
                print("Goodbye!")
            break
    except:
        print("Please enter a valid number.")


users = []

options = [
    "Sign Up",
    "Delete User",
    "Show Users",
    "Search User",
    "Total Users",
    "Hello",
    "Calculator",
    "Exit"
]

calc = [
    "Multiply (*)",
    "Divide (/)",
    "Add (+)",
    "Subtract (-)"
]


# ==========================
# Storage
# ==========================

def load_users():
    global users

    try:
        with open("users.json", "r") as file:
            users = json.load(file)

    except FileNotFoundError:
        users = []


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


# ==========================
# Menu
# ==========================

def show_menu():
    print("\n===== USER MANAGER =====")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


# ==========================
# User Functions
# ==========================

def sign_up():

    name = input("Name: ").strip().lower()
    password = input("Password: ").strip()
    confirm = input("Confirm Password: ").strip()

    if password != confirm:
        print("Passwords do not match.")
        return

    for user in users:
        if user["name"] == name:
            print("User already exists.")
            return

    job = input("Job: ").strip().lower()

    new_user = {
        "name": name,
        "password": password,
        "job": job
    }

    users.append(new_user)

    save_users()

    print("User added successfully.")


def delete_user():

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:
            users.remove(user)

            save_users()

            print("User deleted successfully.")
            return

    print("User not found.")


def show_users():

    if len(users) == 0:
        print("No users.")
        return

    print()

    for user in users:

        print(f"Name     : {user['name']}")
        print(f"Password : {user['password']}")
        print(f"Job      : {user['job']}")
        print("-" * 30)


def search_user():

    name = input("Enter username: ").strip().lower()

    for user in users:

        if user["name"] == name:

            print("\nUser Found\n")

            print(f"Name     : {user['name']}")
            print(f"Password : {user['password']}")
            print(f"Job      : {user['job']}")

            return

    print("User not found.")


def total_users():

    print(f"Total Users : {len(users)}")


def hello():

    name = input("Enter your name: ").title()

    print(f"Hello {name}")


# ==========================
# Calculator
# ==========================

def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return None

    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculator():

    while True:

        print()

        for index, operation in enumerate(calc, start=1):
            print(index, operation)

        choice = input("Choose operation: ")

        try:

            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))

        except ValueError:

            print("Please enter a valid number.")
            continue

        if choice == "1":

            print("Result:", multiply(num1, num2))

        elif choice == "2":

            result = divide(num1, num2)

            if result is None:
                print("Cannot divide by zero.")
            else:
                print("Result:", result)

        elif choice == "3":

            print("Result:", add(num1, num2))

        elif choice == "4":

            print("Result:", subtract(num1, num2))

        else:

            print("Invalid operation.")
            continue

        again = input("Another calculation? (y/n): ").lower()

        if again != "y":
            break


# ==========================
# Main
# ==========================

load_users()

while True:

    show_menu()

    choice = input("\nChoose option: ")

    if choice == "1":

        sign_up()

    elif choice == "2":

        delete_user()

    elif choice == "3":

        show_users()

    elif choice == "4":

        search_user()

    elif choice == "5":

        total_users()

    elif choice == "6":

        hello()

    elif choice == "7":

        calculator()

    elif choice == "8":

        print("Goodbye.")
        break

    else:

        print("Invalid option.")
'''