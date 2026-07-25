
#users= ["ali", "hamed" ,"fateme", "sara" ,"reza","nilo","hanie"]
users=[
    {"name":"hanie",
     "password":24,
     "job":"designer"

},
    {"name":"hossein",
     "password":26,
     "job":"designer"

},
    {"name":"ali",
     "password":20,
     "job":"mentor"

}

]  
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

def sign_in():
    name = input("Enter name: ").strip().lower()
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    for user in users:
        if user["name"] == name:
            print("User already exists.")
            return

    new_user = {
        "name": name,
        "password": password,
        "job": "designer"
    }

    users.append(new_user)

    print("User registered successfully.")
            


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
                name = input("Enter name: ").strip().lower()
                age = int(input("Enter age: "))
                job = input("Enter job: ").strip().lower()

            new_user = {
    "name": name,
    "age": age,
    "job": job
}

            users.append(new_user)

def delete_user():
    name = input("Enter user: ").strip().lower()

    for user in users:
        if user["name"] == name:
            users.remove(user)
            print("Deleted successfully.")
            return

    print("User not found.")

def search_user():
    search = input("Enter user: ").strip().lower()

    found = False

    for user in users:
        if user["name"] == search:
            print(user)
            found = True
            break

    if not found:
        print("User not found.")
def show_user():
    print("\nUsers:")

    for user in users:
        print(
            f'Name: {user["name"]}, '
            f'Age: {user["age"]}, '
            f'Job: {user["job"]}'
        )


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
        sign_in()
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

  