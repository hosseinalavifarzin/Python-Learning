
users= ["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie"]
add_options=["single add","muli add"]
options = ["new_user", "delete_user", "show list", "Search","total","hello","calc","Exit"]
calc = [
    "Multiply (*)",
    "Divide (/)",
    "Add (+)",
    "Subtract (-)"
]

def hello(name):
    name =input("Enter user: ").strip().lower()
    print(f" hello {name} ")

def option():
    for index,add_option in enumerate(add_options,start=1):
        print(index,add_option)

def show_menu():
    for index, option in enumerate(options, start=1):
        print(index, option)


def total_user():
    print(f"Total users:{len(users)}")

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
                result = Division(num1, num2)
                print(f"{num1} / {num2} = {result}")

            elif calc_choose =="3":
                 result = Addition(num1, num2)
                 print(f"{num1} + {num2} = {result}")

            elif calc_choose =="4":
                result = Subtraction(num1, num2)
                print(f"{num1} - {num2} = {result}")
        
            else:
                print("Invalid choice")
                continue
        except:
            print("Please enter a valid number")

    
        
        again = input("Do another calculation? (y/n): ")
        if again=="n":
            break


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

def delete_user():
    delete_user=input("Enter user: ").lower().split(",")
    if delete_user in users:
        users.remove(delete_user)
        print(f"{delete_user} deleted successfully.")
        show_user()
    else:
            print(f"{delete_user} doesnt exists")

def search_user():
    SEARCH_USER=input("Enter user: ").strip().lower()
    if SEARCH_USER in users:
        print(f"{SEARCH_USER} ✅ User found")
    else:
        print("❌ User not found")

def show_user():
    print("\nUsers:")
    print(", ".join(users))


def multiply (a,b):
    return a*b

def Division(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return None

    return a / b


def Addition (a,b):
        return a+b

def Subtraction (a,b):
        return a-b
     


print("===== User Manager =====")





while True:

    show_menu()
    user_choose=input("choose an option:")
    if user_choose=="1":#add_user
        add_user()
    elif user_choose=="2":#delete_user
        delete_user()

    elif user_choose=="3":#show_user
        show_user()

    elif user_choose=="4":#search_user
        search_user()

    elif user_choose == "5":#total_user
        total_user()

    elif user_choose == "6":#hello
        hello()

    elif user_choose=="7":#calc
       cal()
       
    elif user_choose == "8":#Goodbye
        print("Goodbye!")
        
        break
    else:
        print("Invalid option!")

  