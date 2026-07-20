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


name=input("Enter new user: ")
age=int(input("Enter age: "))
job=input("Enter job: ")


new_user = {
    
    "name": name,
    "age": age,
    "job": job
}

for user in users:
   if name in users=="name":
    print(f"{new_user} already exists.")
   else:
    users.append(new_user)
    print(f"{new_user} added successfully") 



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