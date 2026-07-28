


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