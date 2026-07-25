


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