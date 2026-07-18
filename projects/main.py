
users= ["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie"]
options = ["new_user", "delete_user", "show list", "Search","total","hello","calc","Exit"]
calc = ["zarb", "tafrigh", "show list", "Search","total","hello","calc","Exit"]
def show_user():
    print("\nUsers:")
    for user in users:
        print(user)


def multiply (a,b):
        c=a*b
        print(f"{a} x {b}={c}")

def Division (a,b):
        c=a/b
        print(f"{a} / {b} = {c}")

def Addition (a,b):
        c=a+b
        print(f"{a} + {b} = {c}")

def Subtraction (a,b):
        c=a+b
        print(f"{a} + {b} = {c}")

        
def hello(name):
    
    print(f" hello {name} ")

print("===== User Manager =====")


for index, option in enumerate(options, start=1):
    print(index, option)


while True:
    user_choose=input("choose an option:")
    if user_choose=="1":
        new_user=input("enter new user:")
        if new_user in users:
            print(f"{new_user} already exists.")
        else:
            users.append(new_user)
            print(f"{new_user} added successfully")
            show_user()

    elif user_choose=="2":
        delete_user=input("enter user:")
        if delete_user in users:
            users.remove(delete_user)
            print(f"{delete_user} deleted successfully.")
            show_user()

        else:
            print(f"{delete_user} doesnt exists")

    elif user_choose=="3":
        show_user()

    elif user_choose=="4":
        SEARCH_USER=input("Enter username")
        if SEARCH_USER in users:
            print(f"{SEARCH_USER} ✅ User found")
        else:
            print("❌ User not found")

    elif user_choose == "5":
        print(f"Total users:{len(users)}")

    elif user_choose == "6":
        name = input("Enter your name: ")
        hello(name)

    elif user_choose=="7":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        multiply(num1, num2)

    elif user_choose == "8":
        print("Goodbye!")
        
        break
    else:
        print("Invalid option!")

