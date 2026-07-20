
users= ["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie"]
options = ["new_user", "delete_user", "show list", "Search","total","hello","calc","Exit"]
calc = [
    "Multiply (*)",
    "Divide (/)",
    "Add (+)",
    "Subtract (-)"
]

def hello(name):
    
    print(f" hello {name} ")


def show_menu():
    for index, option in enumerate(options, start=1):
        print(index, option)


def show_user():
    print("\nUsers:")
    for user in users:
        print(user)

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
        
    elif user_choose == "8":
        print("Goodbye!")
        
        break
    else:
        print("Invalid option!")

  